---
name: sogi-methodology
description: Consulta o Agentic RAG oficial para explicar o SOGI e a metodologia CEPPEM com evidencia recuperada. Use quando o usuario perguntar o que um conceito, recurso ou indicador significa, como interpretar um resultado, qual procedimento ou estrategia a metodologia recomenda, ou quando uma analise operacional precisar ser ancorada no metodo oficial.
---

# Metodologia SOGI e CEPPEM

Leia `../../references/methodology.md` antes de combinar metodologia com dados operacionais.

## Fluxo

1. Formule uma unica pergunta autocontida sobre o SOGI ou a metodologia CEPPEM.
2. Chame `consultar_metodologia` diretamente. Nao passe essa pergunta por
   `sogi_descobrir_consultas`, pois o Agentic RAG e uma fonte de conhecimento separada das
   consultas operacionais.
3. Baseie a explicacao nos trechos recuperados. Preserve titulo, fonte, secao e escopo quando o
   retorno trouxer esses metadados.
4. Se nenhum trecho relevante for retornado, diga que a base indexada nao fornece evidencia
   suficiente. Nao complete a resposta com uma metodologia suposta.
5. Chame a tool no maximo uma vez por turno; formule melhor a pergunta antes de chamar.

## Separacao de fontes

- Use `consultar_metodologia` para conhecimento: definicoes, funcionalidades do SOGI, playbooks,
  interpretacao de indicadores e recomendacoes CEPPEM.
- Use descoberta e execucao para fatos operacionais: clientes, unidades, pedidos, avaliacoes,
  valores, status e contagens atuais.
- Em pedidos hibridos, consulte as duas fontes e identifique separadamente o que veio dos dados e
  o que veio da metodologia.

## Disponibilidade

Se `consultar_metodologia` nao aparecer entre as tools do MCP, informe que a camada metodologica
ainda nao esta exposta por esse deployment. Nao tente substitui-la por memoria do modelo nem usar
as consultas operacionais como se fossem uma base de conhecimento.
