#!/usr/bin/env python3
"""Validate the public AYA plugin repository without third-party dependencies."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent.parent
PLUGIN = ROOT / "plugins" / "aya-sogi"
EXPECTED_MCP_URL = "https://mcp.dev.ceppem.com/mcp"
EXPECTED_AVATAR = "./assets/aya-agent-avatar.jpg"
EXPECTED_SKILLS = {
    "aya-doctor",
    "aya-start",
    "sogi-customer-registration",
    "sogi-discovery",
    "sogi-methodology",
    "sogi-operations",
    "sogi-order-pipeline",
    "sogi-portfolio-analysis",
    "sogi-reporting",
    "sogi-retention-analysis",
}
SEMVER = re.compile(r"^(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)(?:-[0-9A-Za-z.-]+)?$")
SECRET_PATTERNS = {
    "private key": re.compile(r"BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY"),
    "OpenAI-style secret": re.compile(r"\bsk-[A-Za-z0-9_-]{20,}\b"),
    "GitHub token": re.compile(r"\bgh[pousr]_[A-Za-z0-9]{20,}\b"),
    "AWS access key": re.compile(r"\bAKIA[0-9A-Z]{16}\b"),
}


def load_json(path: Path, errors: list[str]) -> dict[str, Any]:
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        errors.append(f"{path.relative_to(ROOT)}: JSON inválido: {exc}")
        return {}
    if not isinstance(payload, dict):
        errors.append(f"{path.relative_to(ROOT)}: a raiz deve ser um objeto JSON")
        return {}
    return payload


def require_paths(errors: list[str]) -> None:
    required = [
        ROOT / "LICENSE",
        ROOT / "NOTICE",
        ROOT / "PRIVACY.md",
        ROOT / "TERMS_OF_USE.md",
        ROOT / "VERSION",
        ROOT / ".agents" / "plugins" / "marketplace.json",
        ROOT / ".claude-plugin" / "marketplace.json",
        PLUGIN / ".codex-plugin" / "plugin.json",
        PLUGIN / ".claude-plugin" / "plugin.json",
        PLUGIN / ".mcp.json",
        PLUGIN / "assets" / "aya-agent-avatar.jpg",
        PLUGIN / "skills",
        PLUGIN / "references",
        PLUGIN / "references" / "analysis-playbooks.md",
        PLUGIN / "references" / "customer-registration.md",
    ]
    for path in required:
        if not path.exists():
            errors.append(f"arquivo obrigatório ausente: {path.relative_to(ROOT)}")


def validate_manifests(errors: list[str]) -> None:
    version = (ROOT / "VERSION").read_text(encoding="utf-8").strip()
    if SEMVER.fullmatch(version) is None:
        errors.append(f"VERSION não é SemVer estrito: {version!r}")

    codex = load_json(PLUGIN / ".codex-plugin" / "plugin.json", errors)
    claude = load_json(PLUGIN / ".claude-plugin" / "plugin.json", errors)
    mcp = load_json(PLUGIN / ".mcp.json", errors)
    codex_market = load_json(ROOT / ".agents" / "plugins" / "marketplace.json", errors)
    claude_market = load_json(ROOT / ".claude-plugin" / "marketplace.json", errors)

    for label, manifest in (("Codex", codex), ("Claude", claude)):
        if manifest.get("name") != "aya-sogi":
            errors.append(f"manifesto {label}: name deve ser 'aya-sogi'")
        if manifest.get("version") != version:
            errors.append(f"manifesto {label}: version deve ser {version!r}")
        if not manifest.get("description"):
            errors.append(f"manifesto {label}: description é obrigatório")
        author = manifest.get("author")
        if not isinstance(author, dict) or not author.get("name"):
            errors.append(f"manifesto {label}: author.name é obrigatório")

    if codex.get("interface", {}).get("displayName") != "AyA":
        errors.append("manifesto Codex: interface.displayName deve ser 'AyA'")
    if claude.get("displayName") != "AyA":
        errors.append("manifesto Claude: displayName deve ser 'AyA'")

    if codex.get("mcpServers") != "./.mcp.json":
        errors.append("manifesto Codex deve apontar mcpServers para './.mcp.json'")

    codex_interface = codex.get("interface", {})
    if set(codex_interface.get("capabilities", [])) != {"Read", "Write"}:
        errors.append("manifesto Codex: capabilities deve conter Read e Write")
    for field in ("composerIcon", "logo", "logoDark"):
        if codex_interface.get(field) != EXPECTED_AVATAR:
            errors.append(f"manifesto Codex: interface.{field} deve apontar para {EXPECTED_AVATAR!r}")

    codex_url = mcp.get("mcpServers", {}).get("sogi", {}).get("url")
    claude_url = claude.get("mcpServers", {}).get("sogi", {}).get("url")
    if codex_url != EXPECTED_MCP_URL:
        errors.append(f".mcp.json deve usar {EXPECTED_MCP_URL}")
    if claude_url != EXPECTED_MCP_URL:
        errors.append(f"manifesto Claude deve usar {EXPECTED_MCP_URL}")

    if codex_market.get("name") != "aya-plugins":
        errors.append("marketplace Codex deve se chamar 'aya-plugins'")
    if claude_market.get("name") != "aya-plugins":
        errors.append("marketplace Claude deve se chamar 'aya-plugins'")

    codex_plugins = codex_market.get("plugins", [])
    if not isinstance(codex_plugins, list) or len(codex_plugins) != 1:
        errors.append("marketplace Codex deve conter exatamente um plugin")
    else:
        entry = codex_plugins[0]
        if entry.get("name") != "aya-sogi":
            errors.append("entrada Codex deve se chamar 'aya-sogi'")
        if entry.get("source", {}).get("path") != "./plugins/aya-sogi":
            errors.append("entrada Codex deve apontar para './plugins/aya-sogi'")

    claude_plugins = claude_market.get("plugins", [])
    if not isinstance(claude_plugins, list) or len(claude_plugins) != 1:
        errors.append("marketplace Claude deve conter exatamente um plugin")
    else:
        entry = claude_plugins[0]
        if entry.get("name") != "aya-sogi":
            errors.append("entrada Claude deve se chamar 'aya-sogi'")
        if entry.get("displayName") != "AyA":
            errors.append("entrada Claude: displayName deve ser 'AyA'")
        if entry.get("source") != "./plugins/aya-sogi":
            errors.append("entrada Claude deve apontar para './plugins/aya-sogi'")


def parse_frontmatter(path: Path, errors: list[str]) -> dict[str, str]:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        errors.append(f"{path.relative_to(ROOT)}: frontmatter ausente")
        return {}
    end = text.find("\n---\n", 4)
    if end < 0:
        errors.append(f"{path.relative_to(ROOT)}: frontmatter não foi fechado")
        return {}
    values: dict[str, str] = {}
    for line in text[4:end].splitlines():
        if ":" in line:
            key, value = line.split(":", 1)
            values[key.strip()] = value.strip()
    return values


def validate_skills(errors: list[str]) -> None:
    names: set[str] = set()
    skill_files = sorted((PLUGIN / "skills").glob("*/SKILL.md"))
    if not skill_files:
        errors.append("nenhuma skill encontrada")
        return
    for path in skill_files:
        metadata = parse_frontmatter(path, errors)
        name = metadata.get("name", "")
        description = metadata.get("description", "")
        skill_text = path.read_text(encoding="utf-8")
        if name != path.parent.name:
            errors.append(f"{path.relative_to(ROOT)}: name deve ser {path.parent.name!r}")
        if not description:
            errors.append(f"{path.relative_to(ROOT)}: description é obrigatória")
        if "TODO" in skill_text:
            errors.append(f"{path.relative_to(ROOT)}: placeholder TODO não permitido")
        if name in names:
            errors.append(f"skill duplicada: {name}")
        names.add(name)

        openai = path.parent / "agents" / "openai.yaml"
        if not openai.is_file():
            errors.append(f"{openai.relative_to(ROOT)}: metadados de interface ausentes")
            continue
        openai_text = openai.read_text(encoding="utf-8")
        if f"${name}" not in openai_text:
            errors.append(
                f"{openai.relative_to(ROOT)}: default_prompt deve mencionar ${name}"
            )
        if 'value: "sogi"' not in openai_text or EXPECTED_MCP_URL not in openai_text:
            errors.append(f"{openai.relative_to(ROOT)}: dependência MCP SOGI inválida")

    if names != EXPECTED_SKILLS:
        missing = sorted(EXPECTED_SKILLS - names)
        extra = sorted(names - EXPECTED_SKILLS)
        if missing:
            errors.append(f"skills obrigatórias ausentes: {', '.join(missing)}")
        if extra:
            errors.append(f"skills inesperadas: {', '.join(extra)}")


def validate_public_tree(errors: list[str]) -> None:
    forbidden_names = {".env", "settings.local.json"}
    for path in ROOT.rglob("*"):
        if ".git" in path.parts or "dist" in path.parts:
            continue
        relative = path.relative_to(ROOT)
        if path.is_symlink():
            errors.append(f"symlink não permitido: {relative}")
            continue
        if path.is_file() and (path.name in forbidden_names or path.suffix in {".pem", ".key", ".p12", ".pfx"}):
            errors.append(f"arquivo proibido: {relative}")
            continue
        if not path.is_file():
            continue
        try:
            content = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        for label, pattern in SECRET_PATTERNS.items():
            if pattern.search(content):
                errors.append(f"possível {label} em {relative}")


def main() -> int:
    errors: list[str] = []
    require_paths(errors)
    if not errors:
        validate_manifests(errors)
        validate_skills(errors)
    validate_public_tree(errors)

    if errors:
        print("Validação falhou:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    skill_count = len(list((PLUGIN / "skills").glob("*/SKILL.md")))
    print(f"Validação concluída: AyA {(ROOT / 'VERSION').read_text().strip()}, {skill_count} skills.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
