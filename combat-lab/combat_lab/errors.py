class CombatLabError(Exception):
    """Base error for the combat prototype."""


class CatalogError(CombatLabError):
    """Raised when card data violates the executable schema."""


class IllegalAction(CombatLabError):
    """Raised when a declared combo cannot legally resolve."""

