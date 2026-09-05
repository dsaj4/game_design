"use strict";

const fs = require("node:fs");

const targetPath = process.argv[2];
if (!targetPath) {
  throw new Error("Usage: node format-json.js <json-path>");
}

const value = JSON.parse(fs.readFileSync(targetPath, "utf8"));
fs.writeFileSync(targetPath, `${JSON.stringify(value, null, 2)}\n`, "utf8");
