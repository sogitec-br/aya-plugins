# Guia do usuário AyA

## Para que serve

A AYA conecta o agente ao conhecimento metodológico CEPPEM e a consultas SOGI autorizadas para a
identidade atual.

O plugin opera somente leitura. Ele não concede acesso novo, não substitui permissões SOGI e não
deve alterar dados.

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

## Perguntas híbridas

```text
Analise os resultados observados e depois explique como a metodologia oficial os interpreta.
```

A resposta deve separar claramente:

- fatos retornados pelo SOGI;
- cálculos derivados;
- evidências metodológicas;
- limitações e hipóteses.

## Segurança

- use sempre sua própria conta;
- nunca compartilhe senha ou token;
- não envie dados pessoais desnecessários;
- confira período e filtros antes de usar um relatório;
- não reutilize uma resposta antiga como se fosse dado atual;
- não publique respostas do SOGI neste repositório público.

## Mensagens comuns

### Nenhuma consulta encontrada

A intenção pode não estar no catálogo ou não estar autorizada para a identidade atual. Reformule o
pedido com entidade, métrica, período e filtros, sem tentar contornar a autorização.

### Zero registros

A consulta existe e foi executada, mas os filtros não retornaram registros. Isso é diferente de
uma consulta indisponível.

### MCP desconectado

Confirme a instalação do plugin e conclua o OAuth novamente pelo cliente.

### Metodologia sem evidência

O Agentic RAG não encontrou base suficiente. A AYA não deve completar a resposta usando memória ou
suposições.
