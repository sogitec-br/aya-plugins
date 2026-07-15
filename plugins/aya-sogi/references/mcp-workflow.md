# Contrato do gateway SOGI

O contrato funcional separa uma tool de conhecimento de duas tools de dados:

- `consultar_metodologia(pergunta)` — Agentic RAG SOGI/CEPPEM
- `sogi_descobrir_consultas(query, limit)`
- `sogi_executar_consulta(tool_id, arguments)`

Use `consultar_metodologia` diretamente para conceitos, funcionamento do SOGI, interpretacao e
recomendacoes CEPPEM. Ela nao usa `tool_id`. Se a tool nao aparecer no servico conectado, informe
que a camada metodologica ainda nao esta disponivel nessa versao.

Para dados operacionais, sempre descubra primeiro. A descoberta devolve `tool_id`, titulo,
descricao, scope e `input_schema`. Use somente um ID dessa resposta e envie argumentos que validem
exatamente contra o schema. O executor resolve metodo e path no servidor; clientes nunca constroem
URLs internas do servico operacional.

Metadados de selecao explicam qual seletor ranqueou o catalogo, mas nao sao uma autorizacao. Uma
shortlist vazia e uma abstencao segura.
