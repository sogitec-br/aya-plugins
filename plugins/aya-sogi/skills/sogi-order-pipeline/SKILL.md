---
name: sogi-order-pipeline
description: Analisa pipeline, funil, status, valores, gargalos e risco operacional de pedidos SOGI. Use para pedidos cancelados, reprovados, em analise, nao liberados, nao confirmados ou para comparar etapas e periodos.
---

# Analisar pipeline de pedidos

Leia `../../references/analysis-playbooks.md` antes de interpretar os resultados.

1. Defina periodo, unidade de analise, filtros e se o usuario quer panorama, comparacao ou lista
   acionavel.
2. Chame `sogi_descobrir_consultas` para localizar leituras adequadas ao funil e aos status
   solicitados. Use exatamente os rotulos, valores e campos devolvidos; nao fixe codigos de status.
3. Valide o `input_schema` e chame `sogi_executar_consulta` somente com contratos autorizados. Nao
   substitua uma consulta ausente por outra de status semelhante.
4. Organize o retorno por etapa ou situacao e diferencie:
   - pendente ou em processamento;
   - bloqueado aguardando acao;
   - perdido, cancelado ou reprovado;
   - confirmado ou concluido.
   Use apenas categorias sustentadas pelos dados, sem reclassificar registros por intuicao.
5. Informe quantidade e valor separadamente. Confirme se totais incluem todo o universo ou apenas
   uma pagina ou ranking antes de calcular conversao, participacao ou valor em risco.
6. Compare periodos equivalentes e nao interprete acumulado como fluxo do periodo.
7. Identifique gargalos como padroes observados; nao invente causa quando a fonte nao trouxer
   motivo, historico ou tempo de permanencia.
8. Para explicar prioridade ou recomendar proxima acao, consulte `consultar_metodologia` uma vez e
   separe o playbook oficial dos fatos operacionais.

Apresente resumo do funil, pontos de atencao, evidencias por status e limitacoes. Nao amplie o
periodo silenciosamente quando nao houver pedidos no recorte.
