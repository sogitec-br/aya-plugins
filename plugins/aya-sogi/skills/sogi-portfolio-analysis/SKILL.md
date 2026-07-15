---
name: sogi-portfolio-analysis
description: Analisa saude e composicao da carteira SOGI, incluindo clientes positivos, inativos, bloqueados ou congelados, receita, concentracao, geografia, rankings e comparacoes. Use quando o usuario pedir uma visao de portfolio ou desempenho da carteira.
---

# Analisar portfolio SOGI

Leia `../../references/analysis-playbooks.md` antes de interpretar os resultados.

1. Defina a pergunta com metrica, periodo, dimensao, filtros e unidade de comparacao. Pergunte
   apenas o que mudar materialmente a consulta.
2. Descubra um contrato de leitura atual com `sogi_descobrir_consultas`; nunca reutilize
   `tool_id`, campos ou enums de outra sessao.
3. Valide os argumentos contra o `input_schema` e execute `sogi_executar_consulta`.
4. Confirme se o retorno representa o universo completo, uma pagina ou apenas um top N antes de
   calcular participacoes e concentracao.
5. Trate situacoes de carteira como dimensoes do contrato. Nao presuma que positivo, inativo,
   bloqueado e congelado formem grupos exclusivos ou somem o total.
6. Compare apenas periodos, metricas, filtros e granularidades equivalentes. Identifique mudanca
   absoluta e percentual sem misturar as duas.
7. Em receita, informe moeda, periodo, denominador e se o resultado e total, media ou ranking. Em
   geografia, descreva distribuicao e concentracao sem atribuir causalidade.
8. Separe fatos retornados, calculos derivados e hipoteses. Para interpretar ou recomendar acoes,
   consulte `consultar_metodologia` uma vez com uma pergunta autocontida e identifique essa fonte.
9. Se o pedido exigir um arquivo, entregue os dados e a proveniencia para `sogi-reporting`.

Apresente primeiro o achado principal, depois evidencias, recorte utilizado e limitacoes. Nao
amplie filtros quando uma consulta retornar zero registros.
