# Changelog

Todas as mudanças relevantes da AyA são registradas neste arquivo.

## [0.2.1] - 2026-07-16

### Corrigido

- diagnóstico deixa de confundir MCP configurado ou OAuth reconhecido com tools disponíveis na
  tarefa atual;
- onboarding abre uma nova tarefa depois do primeiro OAuth, reconexão ou atualização, evitando
  snapshots de tools criados antes da autenticação;
- remoção de fallback por processo aninhado do Codex quando a tarefa atual não recebeu as tools;
- manifesto Codex passa a respeitar o limite de três prompts sugeridos.

### Documentado

- `list_mcp_resources` não substitui a verificação das tools operacionais;
- instalação canônica usa o MCP fornecido pelo plugin, sem um segundo registro global `sogi`.

## [0.2.0] - 2026-07-15

### Adicionado

- skills de análise de portfólio, retenção e pipeline de pedidos adaptadas ao contrato vivo do
  MCP, sem dependência do harness interno do `ceppem-agent`;
- skill de cadastro de cliente com preparação, pendências, reautorização, aprovação no navegador
  e execução por `operation_id`;
- metadados de interface e dependência MCP para todas as skills no Codex;
- referências compartilhadas de playbooks analíticos e governança de escrita.

### Alterado

- manifests e documentação passam a representar consultas de leitura e cadastro explicitamente
  aprovado;
- onboarding, diagnóstico, descoberta, operações e relatórios reconhecem as três rotas do MCP;
- versão dos pacotes Codex e Claude atualizada para `0.2.0`.

### Removido

- skill genérica `sogi-analytics`, substituída por playbooks de negócio com gatilhos e limites mais
  precisos.

## [0.1.1] - 2026-07-15

### Adicionado

- avatar oficial da AyA como ícone e logo do plugin no Codex;
- nome público simplificado para `AyA` no Codex e Claude;
- inclusão dos assets visuais nos pacotes Codex e Claude.

## [0.1.0] - 2026-07-15

### Adicionado

- plugin compartilhado para Codex e Claude Code;
- conexão OAuth com o MCP SOGI de desenvolvimento;
- skills de onboarding, diagnóstico, metodologia, descoberta, operações, análise e relatórios;
- marketplaces públicos para instalação sem acesso ao GitHub;
- validação e empacotamento reproduzível das duas distribuições;
- licença proprietária e documentação de segurança, privacidade e uso.
