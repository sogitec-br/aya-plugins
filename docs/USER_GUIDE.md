# Guia do usuário AyA

## Para que serve

A AYA conecta o agente ao conhecimento metodológico CEPPEM e a consultas SOGI autorizadas para a
identidade atual.

O plugin não concede acesso novo nem substitui permissões SOGI. Consultas são somente leitura; o
cadastro de cliente é uma escrita separada, disponível apenas para identidades autorizadas e depois
de revisão e aprovação explícitas.

## Perguntas metodológicas

Use para conceitos, funcionalidades, interpretação de indicadores e orientação metodológica:

```text
O que este indicador significa segundo a metodologia CEPPEM?
```

```text
Qual procedimento a metodologia recomenda para este cenário?
```

## Perguntas operacionais

Informe entidade, métrica, período e filtros quando souber:

```text
Quantos pedidos existem por status neste mês?
```

```text
Compare as avaliações autorizadas entre as unidades no período informado.
```

O agente primeiro descobre uma consulta autorizada, valida seu contrato e somente depois executa.
Se a consulta não estiver no catálogo da identidade, a AYA deve informar a limitação.

## Análises orientadas

A AyA possui playbooks próprios para portfólio, retenção e pedidos. Eles usam o contrato atual do
MCP e evitam assumir campos, códigos de status ou limiares fixos:

```text
Analise a saúde da carteira, a concentração de receita e os riscos de retenção neste trimestre.
```

```text
Mostre o pipeline de pedidos e os gargalos sustentados pelos dados deste mês.
```

## Perguntas híbridas

```text
Analise os resultados observados e depois explique como a metodologia oficial os interpreta.
```

A resposta deve separar claramente:

- fatos retornados pelo SOGI;
- cálculos derivados;
- evidências metodológicas;
- limitações e hipóteses.

## Cadastro de cliente

```text
Prepare o cadastro deste cliente com estes dados e me mostre o que falta antes de executar.
```

O fluxo acontece em três fronteiras:

1. a AyA valida e completa os dados, sem cadastrar;
2. o usuário abre a URL temporária, revisa a prévia e aprova com a mesma sessão OAuth;
3. depois da confirmação, a AyA executa somente o `operation_id` aprovado.

Se o escopo de escrita ainda não tiver sido consentido, o cliente solicitará reconexão uma vez.
Não informe credenciais ao agente. Como o endpoint atual é de desenvolvimento, use somente dados
de teste autorizados. Se o resultado ficar incerto (`unknown`), não tente novamente antes de
confirmar o estado no ambiente.

## Segurança

- use sempre sua própria conta;
- nunca compartilhe senha ou token;
- não envie dados pessoais desnecessários;
- confira período e filtros antes de usar um relatório;
- não reutilize uma resposta antiga como se fosse dado atual;
- revise todos os campos antes de aprovar um cadastro;
- não publique respostas do SOGI neste repositório público.

## Mensagens comuns

### Nenhuma consulta encontrada

A intenção pode não estar no catálogo ou não estar autorizada para a identidade atual. Reformule o
pedido com entidade, métrica, período e filtros, sem tentar contornar a autorização.

### Zero registros

A consulta existe e foi executada, mas os filtros não retornaram registros. Isso é diferente de
uma consulta indisponível.

### MCP desconectado

Confirme a instalação do plugin e conclua o OAuth novamente pelo cliente. Se a autenticação foi
feita depois de a tarefa atual ser aberta, crie uma nova tarefa no mesmo projeto antes de testar.
Um endpoint configurado ou `list_mcp_resources` bem-sucedido não prova que as tools SOGI estão
disponíveis naquela tarefa.

### Metodologia sem evidência

O Agentic RAG não encontrou base suficiente. A AYA não deve completar a resposta usando memória ou
suposições.
