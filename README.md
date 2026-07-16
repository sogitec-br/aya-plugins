# AYA Plugins

Plugins oficiais da AYA para Codex e Claude Code, conectados ao MCP SOGI/CEPPEM.

> **Beta:** a versão `0.2.x` usa `https://mcp.dev.ceppem.com/mcp`. Utilize somente com contas e
> dados autorizados para o ambiente de desenvolvimento.

## O que a AYA oferece

- consulta ao Agentic RAG de metodologia SOGI/CEPPEM;
- descoberta de consultas operacionais autorizadas;
- análises de portfólio, retenção e pipeline de pedidos usando o contrato vivo do MCP;
- relatórios com proveniência e minimização de dados pessoais;
- cadastro de cliente com validação, prévia, aprovação explícita e proteção contra repetição;
- autenticação OAuth individual, sem credenciais dentro do plugin.

## Instalação no Codex

Adicione o marketplace público uma vez:

```bash
codex plugin marketplace add sogitec-br/aya-plugins
codex plugin add aya-sogi@aya-plugins
```

Depois, abra uma tarefa no Codex e autentique sua própria conta SOGI quando solicitado. Ao concluir
o primeiro OAuth, abra outra tarefa no mesmo projeto para carregar as tools autenticadas.

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

```text
Prepare o cadastro deste cliente para eu revisar antes da execução.
```

Consultas são somente leitura. Cadastro é uma capacidade de escrita separada: preparar não cria o
cliente, a mesma pessoa revisa e aprova a prévia no navegador e somente depois a AyA executa o
`operation_id`. Nunca use um cadastro real para testar a conexão.

Cada pessoa deve autenticar sua própria conta. Nunca envie senha, token, cookie ou header em uma
conversa, issue ou arquivo do projeto.

## Skills incluídas

- `aya-start` e `aya-doctor`: onboarding e diagnóstico de plugin, MCP e OAuth;
- `sogi-discovery` e `sogi-operations`: contrato vivo e consultas operacionais de leitura;
- `sogi-methodology`: conhecimento oficial recuperado pelo Agentic RAG;
- `sogi-portfolio-analysis`: saúde, receita, concentração e geografia da carteira;
- `sogi-retention-analysis`: inatividade, churn, risco, retenção e reativação;
- `sogi-order-pipeline`: funil, status, valores e gargalos de pedidos;
- `sogi-customer-registration`: preparação, aprovação e execução de cadastro;
- `sogi-reporting`: proveniência e governança para relatórios e exportações.

As skills de negócio usam apenas as tools públicas do MCP. Elas não copiam o runtime de agentes do
CEPPEM nem dependem de nomes de campos, IDs, códigos de status ou ferramentas de visualização
fixos.

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
