# Arquitetura pública da AYA SOGI

## Componentes

```text
Codex ou Claude
    ↓
Plugin AYA SOGI
    ├── skills e referências operacionais
    └── configuração MCP
            ↓ OAuth individual
MCP SOGI/CEPPEM
    ├── consultar_metodologia
    ├── sogi_descobrir_consultas
    └── sogi_executar_consulta
            ↓
Serviços autorizados e Agentic RAG
```

## Responsabilidades do plugin

- escolher corretamente entre conhecimento metodológico e dados operacionais;
- exigir descoberta antes de executar consultas operacionais;
- usar somente contratos devolvidos pelo MCP;
- separar fatos, cálculos e interpretação;
- orientar minimização de dados;
- permanecer somente leitura.

## Responsabilidades do MCP

- autenticar cada usuário;
- derivar identidade, tenant, perfil e representante;
- aplicar autorização antes da descoberta e da execução;
- validar schemas e parâmetros;
- proteger serviços internos;
- registrar auditoria;
- revogar acesso.

O plugin nunca é uma fronteira de autorização. Como o código é publicamente visível, toda decisão de
segurança deve permanecer no servidor.

## Separação das fontes

`consultar_metodologia` recupera conceitos, procedimentos e evidências metodológicas. Ela não
retorna fatos operacionais atuais.

`sogi_descobrir_consultas` e `sogi_executar_consulta` tratam fatos operacionais autorizados. O
cliente nunca deve inventar identificadores ou construir chamadas para serviços internos.

## Estado beta

A versão `0.1.x` aponta para `https://mcp.dev.ceppem.com/mcp`. Uma release estável deve usar um
endpoint de produção explicitamente aprovado e passar novamente pelos testes de OAuth, catálogo,
metodologia, auditoria e rollback.
