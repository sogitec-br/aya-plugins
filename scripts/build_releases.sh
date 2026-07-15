#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
VERSION="$(tr -d '[:space:]' < "$ROOT/VERSION")"
DIST="$ROOT/dist"
PLUGIN="$ROOT/plugins/aya-sogi"
TMP="$(mktemp -d)"

cleanup() {
  rm -rf "$TMP"
}
trap cleanup EXIT

python3 "$ROOT/scripts/validate_repository.py"
mkdir -p "$DIST"
find "$DIST" -maxdepth 1 -type f \( -name 'AYA-SOGI-*.zip' -o -name 'SHA256SUMS.txt' \) -delete

CLAUDE_STAGE="$TMP/claude"
mkdir -p "$CLAUDE_STAGE"
cp -R "$PLUGIN/.claude-plugin" "$CLAUDE_STAGE/.claude-plugin"
cp -R "$PLUGIN/skills" "$CLAUDE_STAGE/skills"
cp -R "$PLUGIN/references" "$CLAUDE_STAGE/references"
cp "$ROOT/LICENSE" "$ROOT/NOTICE" "$ROOT/TERMS_OF_USE.md" "$ROOT/PRIVACY.md" "$CLAUDE_STAGE/"

CODEX_STAGE="$TMP/codex"
mkdir -p "$CODEX_STAGE/.agents/plugins" "$CODEX_STAGE/plugins/aya-sogi"
cp "$ROOT/.agents/plugins/marketplace.json" "$CODEX_STAGE/.agents/plugins/marketplace.json"
cp -R "$PLUGIN/.codex-plugin" "$CODEX_STAGE/plugins/aya-sogi/.codex-plugin"
cp "$PLUGIN/.mcp.json" "$CODEX_STAGE/plugins/aya-sogi/.mcp.json"
cp -R "$PLUGIN/skills" "$CODEX_STAGE/plugins/aya-sogi/skills"
cp -R "$PLUGIN/references" "$CODEX_STAGE/plugins/aya-sogi/references"
cp "$ROOT/LICENSE" "$ROOT/NOTICE" "$ROOT/TERMS_OF_USE.md" "$ROOT/PRIVACY.md" "$CODEX_STAGE/"

(
  cd "$CLAUDE_STAGE"
  COPYFILE_DISABLE=1 zip -q -r "$DIST/AYA-SOGI-CLAUDE-v$VERSION.zip" . \
    -x '*/.DS_Store' '*/._*'
)

(
  cd "$CODEX_STAGE"
  COPYFILE_DISABLE=1 zip -q -r "$DIST/AYA-SOGI-CODEX-v$VERSION.zip" . \
    -x '*/.DS_Store' '*/._*'
)

unzip -tq "$DIST/AYA-SOGI-CLAUDE-v$VERSION.zip"
unzip -tq "$DIST/AYA-SOGI-CODEX-v$VERSION.zip"

if command -v sha256sum >/dev/null 2>&1; then
  (
    cd "$DIST"
    sha256sum "AYA-SOGI-CLAUDE-v$VERSION.zip" "AYA-SOGI-CODEX-v$VERSION.zip" > SHA256SUMS.txt
  )
else
  (
    cd "$DIST"
    shasum -a 256 "AYA-SOGI-CLAUDE-v$VERSION.zip" "AYA-SOGI-CODEX-v$VERSION.zip" > SHA256SUMS.txt
  )
fi

echo "Releases geradas em $DIST"
