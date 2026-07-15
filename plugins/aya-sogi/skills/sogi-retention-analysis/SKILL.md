---
name: sogi-retention-analysis
description: Analisa inatividade, churn, pre-inatividade, risco de perda, retencao e reativacao no SOGI. Use para diagnosticar deterioracao da carteira, distinguir estoque de inativos de novas perdas e priorizar oportunidades de recuperacao.
---

# Analisar retencao SOGI

Leia `../../references/analysis-playbooks.md` antes de interpretar os resultados.

1. Determine se o pedido trata de panorama atual, evento no periodo, risco futuro ou recuperacao.
   Nao use esses conceitos como sinonimos.
2. Para panorama de inatividade, consulte o estoque no recorte solicitado. Para churn, procure uma
   consulta que represente novas inativacoes ou perdas no periodo.
3. Nunca calcule churn a partir de uma lista generica de clientes inativos. Se o catalogo nao
   expuser o evento ou denominador necessario, declare que a taxa nao pode ser sustentada.
4. Chame `sogi_descobrir_consultas` para cada medida necessaria, valide o `input_schema` e use
   `sogi_executar_consulta` apenas com contratos autorizados da sessao atual.
5. Mantenha periodos e denominadores comparaveis. Diferencie quantidade, taxa, valor em risco e
   participacao na carteira.
6. Nao presuma que pre-inativo, inativo, bloqueado ou outra situacao tenham significado, limiar ou
   exclusividade fixa; use os rotulos e a semantica do contrato e da metodologia atuais.
7. Separe observacao, diagnostico e recomendacao. Para interpretar sinais ou propor abordagem de
   retencao, consulte `consultar_metodologia` uma vez e vincule cada acao a uma evidencia atual.
8. Priorize por impacto, urgencia e recuperabilidade somente quando os dados fornecerem base para
   esses criterios. Identifique hipoteses e informacoes ausentes.

Entregue o panorama, a movimentacao no periodo, os segmentos prioritarios e as limitacoes em
blocos separados. Uma resposta vazia nao autoriza ampliar silenciosamente o recorte.
