---
name: sogi-discovery
description: Descobre consultas SOGI autorizadas e seleciona o contrato correto antes da execucao. Use para qualquer pergunta que dependa de dados do SOGI/AyA.
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
