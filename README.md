# AYA Plugins

Plugins oficiais da AYA para Codex e Claude Code, conectados ao MCP SOGI/CEPPEM.

> **Beta:** a versão `0.1.x` usa `https://mcp.dev.ceppem.com/mcp`. Utilize somente com contas e
> dados autorizados para o ambiente de desenvolvimento.

## O que a AYA oferece

- consulta ao Agentic RAG de metodologia SOGI/CEPPEM;
- descoberta de consultas operacionais autorizadas;
- execução somente leitura usando o contrato devolvido pelo MCP;
- análises e relatórios com proveniência e minimização de dados pessoais;
- autenticação OAuth individual, sem credenciais dentro do plugin.

## Instalação no Codex

Adicione o marketplace público uma vez:

```bash
codex plugin marketplace add sogitec-br/aya-plugins
codex plugin add aya-sogi@aya-plugins
```

Depois, abra uma nova tarefa no Codex e autentique sua própria conta SOGI quando solicitado.

## Instalação no Claude Code

No Claude Code, execute:

```text
/plugin marketplace add sogitec-br/aya-plugins
/plugin install aya-sogi@aya-plugins
/reload-plugins
```

No Claude Code Desktop, também é possível usar o gerenciador visual de plugins em sessões locais
ou SSH.

## Uso

O usuário não precisa conhecer tools, schemas ou identificadores internos. Exemplos:

```text
Explique este indicador com base na metodologia oficial.
```

```text
Mostre a distribuição dos pedidos por status no período autorizado.
```

```text
Analise os dados observados segundo a metodologia CEPPEM.
```

Cada pessoa deve autenticar sua própria conta. Nunca envie senha, token, cookie ou header em uma
conversa, issue ou arquivo do projeto.

## Documentação

- [Instalação no Codex](docs/INSTALL_CODEX.md)
- [Instalação no Claude Code](docs/INSTALL_CLAUDE.md)
- [Guia do usuário](docs/USER_GUIDE.md)
- [Arquitetura e limites de segurança](docs/ARCHITECTURE.md)
- [Processo de release](docs/RELEASE.md)
- [Política de privacidade](PRIVACY.md)
- [Termos de uso](TERMS_OF_USE.md)
- [Segurança](SECURITY.md)

## Visibilidade e licença

Este repositório é publicamente visível para transparência e distribuição, mas **não é open
source**. O código, as skills, os prompts, as configurações e a documentação são proprietários.

A única permissão concedida é a instalação e execução de uma cópia oficial e não modificada do
plugin por um usuário autorizado. Reutilização, modificação, redistribuição, sublicenciamento e
criação de derivados são proibidos. Consulte [LICENSE](LICENSE) e
[TERMS_OF_USE.md](TERMS_OF_USE.md).

## Desenvolvimento

Contribuições públicas de código não são aceitas sem autorização prévia. Mantenedores autorizados
devem seguir [CONTRIBUTING.md](CONTRIBUTING.md) e executar:

```bash
python3 scripts/validate_repository.py
bash scripts/build_releases.sh
```
