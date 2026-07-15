---
name: sogi-discovery
description: Descobre consultas operacionais de leitura autorizadas no SOGI e seleciona o contrato correto antes da execucao. Use quando uma pergunta depender de fatos atuais do SOGI; nao use para metodologia nem para cadastro de cliente.
---

# Descoberta de consultas

Leia `../../references/mcp-workflow.md` quando precisar revisar o contrato do gateway.

1. Resuma a intencao com entidade, metrica, granularidade, periodo e filtros informados.
2. Chame `sogi_descobrir_consultas` com a intencao em linguagem natural e limite pequeno.
3. Compare titulo, descricao e `input_schema` dos candidatos; nao escolha apenas por palavra-chave.
4. Se nenhum candidato cobrir a intencao, pare e reporte a lacuna.
5. Se houver ambiguidade material entre candidatos, apresente a diferenca ou solicite o dado minimo
   que falta.
6. Preserve o `tool_id` exatamente como retornado e use somente o schema da mesma descoberta.

Nao execute durante uma tarefa que pediu apenas para listar ou avaliar consultas disponiveis.
Nao use este fluxo para `consultar_metodologia`, `sogi_preparar_cadastro_cliente` ou
`sogi_cadastrar_cliente`, que sao tools diretas e estaveis.
