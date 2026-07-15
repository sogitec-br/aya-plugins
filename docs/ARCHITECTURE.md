# Arquitetura pública da AyA

## Componentes

```text
Codex ou Claude
    ↓
Plugin AyA
    ├── skills e referências operacionais
    └── configuração MCP
            ↓ OAuth individual
MCP SOGI/CEPPEM
    ├── consultar_metodologia
    ├── sogi_descobrir_consultas
    ├── sogi_executar_consulta
    ├── sogi_preparar_cadastro_cliente
    └── sogi_cadastrar_cliente
            ↓
Serviços autorizados e Agentic RAG
```

## Responsabilidades do plugin

- escolher corretamente entre conhecimento metodológico e dados operacionais;
- exigir descoberta antes de executar consultas operacionais;
- usar somente contratos devolvidos pelo MCP;
- separar fatos, cálculos e interpretação;
- orientar minimização de dados;
- aplicar playbooks de portfólio, retenção e pedidos sem fixar campos ou status;
- manter cadastro separado das consultas e exigir revisão e aprovação explícitas.

## Responsabilidades do MCP

- autenticar cada usuário;
- derivar identidade, tenant, perfil e representante;
- aplicar autorização antes da descoberta e da execução;
- validar schemas e parâmetros;
- validar e enriquecer CNPJ, CEP e lookups conforme o contrato vivo;
- vincular a aprovação de escrita à mesma identidade OAuth;
- proteger o cadastro contra repetição no MCP e falhar fechado quando o resultado for incerto;
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

`sogi_preparar_cadastro_cliente` e `sogi_cadastrar_cliente` formam um fluxo direto de escrita. A
preparação não cria dados; a execução só aceita o `operation_id` preparado e aprovado pela mesma
pessoa. Esse fluxo não passa pela descoberta semântica.

## Estado beta

A versão `0.2.x` aponta para `https://mcp.dev.ceppem.com/mcp`. O cadastro deve usar somente dados de
teste autorizados. Uma release estável deve usar um endpoint de produção explicitamente aprovado e
passar novamente pelos testes de OAuth, catálogo, metodologia, aprovação, idempotência, auditoria e
rollback.
