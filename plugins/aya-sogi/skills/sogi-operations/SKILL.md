---
name: sogi-operations
description: Responde perguntas operacionais com consultas SOGI somente leitura. Use para pedidos, empresas, unidades, requisitos, avaliacoes ou outras entidades presentes no catalogo autorizado.
---

# Consultas operacionais SOGI

1. Use o workflow de `sogi-discovery` para obter um contrato autorizado.
2. Monte `arguments` apenas com propriedades do `input_schema`, respeitando tipos, enums e campos
   obrigatorios.
3. Pergunte ao usuario somente valores obrigatorios ausentes que nao possam ser inferidos do pedido.
4. Execute `sogi_executar_consulta` com o `tool_id` descoberto e os argumentos validados.
5. Responda primeiro com o resultado operacional objetivo e depois com filtros e limitacoes.
6. Diferencie zero registros de consulta inexistente.

Entidades citadas na descricao desta skill sao intencoes possiveis, nao garantia de acesso. O
catalogo retornado para a identidade atual e a autoridade final.
