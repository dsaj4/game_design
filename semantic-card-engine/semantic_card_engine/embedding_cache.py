from __future__ import annotations

from dataclasses import dataclass
import hashlib
from importlib.metadata import version as package_version
import json
import math
from pathlib import Path
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .experiment import ExperimentConfig


CACHE_SCHEMA_VERSION = "semantic-embedding-cache-v0"
TEMPLATE_VERSION = "semantic-card-zh-v0"
DEFAULT_MODEL_ID = "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"
DEFAULT_MODEL_REVISION = "e8f8c211226b894fcb81acc59f3b34ba3efd5f42"
DEFAULT_MODEL_LICENSE = "apache-2.0"


class EmbeddingCacheError(ValueError):
    pass


@dataclass(frozen=True)
class EmbeddingEntry:
    text: str
    text_sha256: str
    vector: tuple[float, ...]


@dataclass(frozen=True)
class EmbeddingCache:
    schema_version: str
    template_version: str
    model_id: str
    model_revision: str
    model_license: str
    dimension: int
    normalized: bool
    runtime_versions: dict[str, str]
    entries: dict[str, EmbeddingEntry]
    digest: str

    def vector(self, entry_id: str) -> tuple[float, ...]:
        try:
            return self.entries[entry_id].vector
        except KeyError as error:
            raise EmbeddingCacheError(
                f"embedding cache is missing entry: {entry_id}"
            ) from error


def build_embedding_texts(config: ExperimentConfig) -> dict[str, str]:
    texts: dict[str, str] = {}
    role_labels = {
        "concept": "卡牌合成材料",
        "action": "玩家施加的合成动作",
        "core": "影响合成方向的核心卡",
    }
    for role, entities in (
        ("concept", config.concepts),
        ("action", config.actions),
        ("core", config.cores),
    ):
        for entity_id in sorted(entities):
            entity = entities[entity_id]
            texts[f"neutral:{role}:{entity_id}"] = (
                f"{entity.name}：{entity.definition}"
            )
            texts[f"role:{role}:{entity_id}"] = (
                f"{role_labels[role]}“{entity.name}”：{entity.definition}"
            )

    for effect_op in config.effect_ops:
        texts[f"effect:{effect_op}"] = (
            f"卡牌战斗效果“{effect_op}”：{config.effect_definitions[effect_op]}"
        )

    for concept_id in sorted(config.concepts):
        concept = config.concepts[concept_id]
        for action_id in sorted(config.actions):
            action = config.actions[action_id]
            for core_id in sorted(config.cores):
                core = config.cores[core_id]
                texts[f"structured:{concept_id}:{action_id}:{core_id}"] = (
                    f"在卡牌合成中，核心卡“{core.name}”（{core.definition}）"
                    f"对材料“{concept.name}”（{concept.definition}）"
                    f"施加动作“{action.name}”（{action.definition}）。"
                    "描述这个组合形成的战斗效果。"
                )
    return dict(sorted(texts.items()))


def build_embedding_cache(
    config: ExperimentConfig,
    model_id: str = DEFAULT_MODEL_ID,
    model_revision: str = DEFAULT_MODEL_REVISION,
) -> dict[str, object]:
    if not model_id or len(model_revision) != 40:
        raise EmbeddingCacheError("model id and exact 40-character revision are required")
    try:
        import torch
        from sentence_transformers import SentenceTransformer
    except ImportError as error:
        raise EmbeddingCacheError(
            "build-embeddings requires the embedding-build optional dependency"
        ) from error

    torch.set_num_threads(1)
    torch.use_deterministic_algorithms(True)
    texts = build_embedding_texts(config)
    entry_ids = list(texts)
    model = SentenceTransformer(
        model_id,
        revision=model_revision,
        device="cpu",
        trust_remote_code=False,
    )
    encoded = model.encode(
        [texts[entry_id] for entry_id in entry_ids],
        batch_size=16,
        show_progress_bar=False,
        convert_to_numpy=True,
        normalize_embeddings=True,
    )
    if len(encoded) != len(entry_ids):
        raise EmbeddingCacheError("model returned an unexpected number of embeddings")
    dimension = int(encoded.shape[1])
    entries = {
        entry_id: {
            "text": texts[entry_id],
            "text_sha256": _text_digest(texts[entry_id]),
            "vector": [round(float(value), 8) for value in vector],
        }
        for entry_id, vector in zip(entry_ids, encoded, strict=True)
    }
    payload: dict[str, object] = {
        "schema_version": CACHE_SCHEMA_VERSION,
        "template_version": TEMPLATE_VERSION,
        "model": {
            "id": model_id,
            "revision": model_revision,
            "license": DEFAULT_MODEL_LICENSE,
            "dimension": dimension,
            "normalized": True,
        },
        "runtime_versions": {
            "sentence-transformers": package_version("sentence-transformers"),
            "torch": package_version("torch"),
            "transformers": package_version("transformers"),
        },
        "entries": entries,
    }
    payload["digest"] = hashlib.sha256(_canonical_json(payload)).hexdigest()
    return payload


def write_embedding_cache(path: Path | str, payload: dict[str, object]) -> None:
    output_path = Path(path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
        newline="\n",
    )


def load_embedding_cache(
    path: Path | str,
    config: ExperimentConfig,
) -> EmbeddingCache:
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    digest = str(data.get("digest", ""))
    digest_payload = {key: value for key, value in data.items() if key != "digest"}
    expected_digest = hashlib.sha256(_canonical_json(digest_payload)).hexdigest()
    if not digest or digest != expected_digest:
        raise EmbeddingCacheError("embedding cache digest does not match its content")
    if data.get("schema_version") != CACHE_SCHEMA_VERSION:
        raise EmbeddingCacheError("unsupported embedding cache schema")
    if data.get("template_version") != TEMPLATE_VERSION:
        raise EmbeddingCacheError("embedding cache template version is stale")

    model = data.get("model", {})
    model_id = str(model.get("id", ""))
    model_revision = str(model.get("revision", ""))
    model_license = str(model.get("license", ""))
    dimension = int(model.get("dimension", 0))
    normalized = bool(model.get("normalized", False))
    if (
        not model_id
        or len(model_revision) != 40
        or not model_license
        or dimension < 1
        or not normalized
    ):
        raise EmbeddingCacheError("embedding cache has invalid model metadata")

    expected_texts = build_embedding_texts(config)
    raw_entries = data.get("entries", {})
    if set(raw_entries) != set(expected_texts):
        raise EmbeddingCacheError("embedding cache entries do not match experiment texts")
    entries: dict[str, EmbeddingEntry] = {}
    for entry_id, expected_text in expected_texts.items():
        raw_entry = raw_entries[entry_id]
        text = str(raw_entry.get("text", ""))
        text_sha256 = str(raw_entry.get("text_sha256", ""))
        vector = tuple(float(value) for value in raw_entry.get("vector", []))
        if text != expected_text or text_sha256 != _text_digest(text):
            raise EmbeddingCacheError(f"embedding text is stale: {entry_id}")
        if len(vector) != dimension:
            raise EmbeddingCacheError(f"embedding dimension mismatch: {entry_id}")
        norm = math.sqrt(sum(value * value for value in vector))
        if not math.isclose(norm, 1.0, rel_tol=0, abs_tol=0.0001):
            raise EmbeddingCacheError(f"embedding is not normalized: {entry_id}")
        entries[entry_id] = EmbeddingEntry(text, text_sha256, vector)

    return EmbeddingCache(
        schema_version=CACHE_SCHEMA_VERSION,
        template_version=TEMPLATE_VERSION,
        model_id=model_id,
        model_revision=model_revision,
        model_license=model_license,
        dimension=dimension,
        normalized=normalized,
        runtime_versions={
            str(key): str(value)
            for key, value in data.get("runtime_versions", {}).items()
        },
        entries=entries,
        digest=digest,
    )


def _text_digest(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def _canonical_json(value: object) -> bytes:
    return json.dumps(
        value,
        ensure_ascii=False,
        separators=(",", ":"),
        sort_keys=True,
    ).encode("utf-8")
