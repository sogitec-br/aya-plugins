# Migração do MCP AyA: inventário e critérios de corte

Estado verificado em 22/09/2026 (ambiente de desenvolvimento Nutrata). O plugin
`aya-sogi` 0.2.1 continua configurado para o broker Python em
`https://mcp.dev.ceppem.com/mcp`. A URL publicada do MCP Go dessa instalação é
`https://api.nutrata.dev.sogivendas.com.br/api/v1/ai/mcp`. **Não trocar a URL do
plugin apenas porque o Go já anuncia OAuth:** faltam equivalência das capacidades
do plugin e aceite do fluxo completo nos clientes alvo. O endpoint Go é específico
da instalação Nutrata; o plugin distribuído não pode assumir que todas as contas
pertencem a essa instalação.

## Inventário da fonte mantida neste repositório

| Consumidor ou referência | Local | Autenticação e uso atual | Destino/decisão |
| --- | --- | --- | --- |
| Codex, configuração MCP efetiva | `plugins/aya-sogi/.mcp.json` | HTTP com OAuth individual do broker Python; sem segredo no plugin | URL por instalação e novo OAuth Go somente após os critérios abaixo |
| Claude, configuração MCP efetiva | `plugins/aya-sogi/.claude-plugin/plugin.json` | Mesmo endpoint e OAuth | Mesmo corte, validado no Claude |
| Metadados das dez skills Codex | `plugins/aya-sogi/skills/*/agents/openai.yaml` | Cada dependência MCP `sogi` repete a URL antiga | Atualizar junto dos dois manifestos, após compatibilidade |
| Validador | `scripts/validate_repository.py` (`EXPECTED_MCP_URL`) | Exige a URL antiga nos manifestos e nas dez skills | Alterar apenas no mesmo corte atômico da configuração |
| Instalação e descrição | `README.md`, `docs/INSTALL_CODEX.md`, `docs/INSTALL_CLAUDE.md`, `docs/ARCHITECTURE.md` | Descrevem URL/OAuth antigo e onboarding | Revisar junto do corte; não anunciar sessão antiga como válida no Go |
| Contrato operacional das skills | `plugins/aya-sogi/references/mcp-workflow.md`, `plugins/aya-sogi/skills/aya-start/SKILL.md`, `plugins/aya-sogi/skills/sogi-discovery/SKILL.md` e skills analíticas | `sogi_descobrir_consultas` → `sogi_executar_consulta` | Conferir nomes, schemas e autorização contra `tools/list` real do Go antes de alterar o fluxo |
| Metodologia | `plugins/aya-sogi/skills/sogi-methodology/SKILL.md`, `plugins/aya-sogi/references/methodology.md` | `consultar_metodologia` no broker, apoiada pelo RAG | Definir e validar rota externa com evidência e proveniência; RAG S2S da AyA sozinho não expõe essa tool ao plugin |
| Cadastro | `plugins/aya-sogi/skills/sogi-customer-registration/SKILL.md`, `plugins/aya-sogi/references/customer-registration.md` | Preparação, consentimento de criação, aprovação no navegador e execução por `operation_id` | Preservar esse contrato ou aprovar migração funcional explícita; o Go publica somente `mcp:read` |

`docs/RELEASE.md` ainda exige teste de OAuth, metodologia, leitura e preparação de
cadastro. `docs/USER_GUIDE.md` descreve a aprovação. Esses gates também precisam
ser reconciliados no corte. Este inventário cobre a fonte versionada, não cópias
instaladas, preferências locais, Langflow, xAI ou outros serviços; seus responsáveis
precisam confirmar a configuração efetiva de cada cliente antes de retirar o broker.

## Evidência de autenticação e compatibilidade

- O broker Python anuncia issuer `https://mcp.dev.ceppem.com/`, recurso
  `https://mcp.dev.ceppem.com/mcp`, PKCE S256 e escopos `sogi:read` e
  `sogi:clientes:create`. O Go da instalação Nutrata anuncia outro issuer e
  recurso, DCR, PKCE S256 e apenas `mcp:read`. Ambos responderam `200` aos
  respectivos documentos públicos de discovery na verificação sem credenciais.
- `GET` sem credencial à URL MCP Go respondeu `401` com `WWW-Authenticate`
  apontando ao metadata do recurso. Isso confirma o challenge público, mas não
  prova login, callback, refresh nem acesso a tools para uma conta piloto.
- O [runbook OAuth Go](https://github.com/sogitec-br/ceppem-backend/blob/developer/docs/auth/mcpoauth/runbook.md)
  exige nova autorização por cliente; tokens opacos emitidos pelo Python não são
  aceitos automaticamente pelo Go. JWT SOGI e API key via Basic são caminhos
  separados já usados por integrações autenticadas, não uma forma de reaproveitar
  a sessão OAuth do plugin.
- A [issue de migração #890](https://github.com/sogitec-br/ceppem-backend/issues/890)
  e a [PR de retirada Python #647](https://github.com/sogitec-br/ceppem-ai/pull/647)
  deixam metodologia, cadastro aprovado, workflows e consumidores externos como
  dependências do desligamento. A [issue de auditoria #1006](https://github.com/sogitec-br/ceppem-backend/issues/1006)
  registra 24 tools Go em Dev e separa o consentimento do host (F16) do controle
  de autorização no servidor.

## Critérios para trocar a configuração fonte

1. Definir o endpoint Go por instalação e o destino das contas atuais do plugin.
   Registrar owner e rollback por consumidor. Não apontar indiscriminadamente o
   marketplace inteiro para a instalação Nutrata.
2. Validar no Codex e no Claude com contas piloto autorizadas: discovery → DCR →
   navegador/consentimento → callback → token → `tools/list` → leitura permitida
   → refresh → revogação. Testar ausência de `AcessoAI`, outro tenant e escopo
   comercial sem registrar tokens ou dados pessoais.
3. Comparar os contratos reais do Go com cada skill. Para leitura, decidir como
   substituir a descoberta semântica antiga sem inventar `tool_id` ou pressupor
   schemas. Para metodologia, demonstrar a nova tool/rota e sua proveniência.
4. Entregar e aceitar o fluxo de cadastro: preparação de dados sintéticos,
   consentimento de escrita, prévia, aprovação pela mesma identidade, execução
   única por `operation_id`, idempotência, auditoria e recuperação de estado
   incerto. Até lá, não transformar uma tool Go de leitura em atalho para escrita.
5. No corte, mudar juntos os dois manifestos MCP, os dez metadados das skills,
   o validador e a documentação; exigir nova autorização. Validar instalação
   limpa, catálogo, leitura, metodologia e cadastro em cenários autorizados.
   Manter rollback para uma combinação comprovada de URL, cliente e credencial.

## Dependências operacionais fora deste repositório

- **Langflow:** configurar o MCP HTTP na URL Go da instalação com uma API key
  CEPPEM **do tipo usuário**, ativa e autorizada com `AcessoAI`, guardada como
  credencial/header do próprio Langflow, ou JWT SOGI com renovação definida.
  O Bearer OAuth Python não autentica no Go. Registrar versão do Langflow,
  protocolo negociado, `tools/list`, uma leitura e `structuredContent`, além de
  rotação/revogação da credencial e do diagnóstico de Host/Origin.
- **Consentimento do plugin (F16):** o responsável pela integração deve decidir
  o comportamento do host para `Allow all actions` frente a `Always ask`, em
  especial antes de qualquer escrita. O plugin não altera a preferência do host;
  aprovação visível e autorização no servidor precisam ser verificadas
  separadamente.
- **Serviços Python:** não desligar broker, banco nem endpoints antigos enquanto
  metodologia, cadastro, xAI, workflows ou clientes ainda dependerem deles.
  Retenção da auditoria e rollback pertencem ao plano operacional de #890/#647.

## Limites desta verificação

O validador local passou com a URL atual. Não havia credencial SOGI segura
disponível neste processo nem tool SOGI injetada nesta tarefa; portanto não houve
`tools/list` autenticado, descoberta, leitura comercial, metodologia ou cadastro
ao vivo. Os documentos OAuth e o challenge foram consultados sem autenticação;
isso não é aceite funcional nem prova de paridade para Codex, Claude ou Langflow.
