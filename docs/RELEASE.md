# Processo de release

## Versionamento

A versão deve ser idêntica em:

- `VERSION`;
- `plugins/aya-sogi/.codex-plugin/plugin.json`;
- `plugins/aya-sogi/.claude-plugin/plugin.json`;
- `CHANGELOG.md`;
- tag Git `vX.Y.Z`.

## Validação local

```bash
python3 scripts/validate_repository.py
python3 /caminho/plugin-creator/scripts/validate_plugin.py plugins/aya-sogi
claude plugin validate plugins/aya-sogi
bash scripts/build_releases.sh
```

O segundo comando usa o validador oficial disponível no ambiente de desenvolvimento do Codex.

## Artefatos

O build gera:

```text
dist/AYA-SOGI-CLAUDE-vX.Y.Z.zip
dist/AYA-SOGI-CODEX-vX.Y.Z.zip
dist/SHA256SUMS.txt
```

O ZIP Claude contém o plugin com `.claude-plugin/plugin.json` na raiz. O ZIP Codex contém o
marketplace portátil e o plugin com `.codex-plugin/plugin.json` e `.mcp.json`.

## Publicação

1. atualizar versão e changelog;
2. abrir pull request;
3. aguardar validações;
4. revisar licença, privacidade e ausência de segredos;
5. fazer merge em `main`;
6. criar e enviar a tag `vX.Y.Z`;
7. o workflow cria a GitHub Release e anexa os artefatos;
8. validar instalação em contas novas de Codex e Claude;
9. validar OAuth, metodologia e uma intenção autorizada somente leitura;
10. validar a preparação de cadastro com dados sintéticos e confirmar que nenhum POST ocorre sem
    aprovação; uma execução real exige um cenário de teste previamente autorizado.

## Rollback

Não reutilize uma versão antiga. Reverta o comportamento, incremente a versão patch, documente o
rollback no changelog e publique novos artefatos.
