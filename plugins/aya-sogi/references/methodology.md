# Contrato da metodologia

`consultar_metodologia(pergunta)` e a interface do Agentic RAG de conhecimento do ecossistema.
Seu corpus cobre informacoes sobre o SOGI e a metodologia oficial CEPPEM, incluindo conceitos,
glossario, playbooks, interpretacao de indicadores e orientacoes de acao.

Ela nao devolve fatos operacionais atuais. Dados de clientes, unidades, requisitos, avaliacoes,
pedidos, valores e status continuam vindo das consultas operacionais autorizadas do SOGI.

## Escolha da fonte

| Pedido | Fonte |
| --- | --- |
| "O que significa este indicador?" | `consultar_metodologia` |
| "Como o SOGI trata este processo?" | `consultar_metodologia` |
| "Qual acao a metodologia recomenda?" | `consultar_metodologia` |
| "Quantos clientes estao inativos?" | descoberta + execucao SOGI |
| "Analise os inativos segundo a metodologia" | ambas, com evidencias separadas |

O RAG e a fonte para metodo e conhecimento institucional; ele nao e autorizacao para acessar
dados. A descoberta de consultas operacionais e a recuperacao metodologica sao fluxos separados.
