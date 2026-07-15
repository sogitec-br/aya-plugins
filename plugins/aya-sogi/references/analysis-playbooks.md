# Playbooks de analise SOGI

Estes playbooks preservam a logica de negocio util do ecossistema CEPPEM e operam diretamente as
tools publicas do MCP, sem depender de um runtime ou uma arquitetura interna de agentes.

## Invariantes

1. Obtenha fatos atuais somente por consultas autorizadas do MCP.
2. Obtenha definicoes, interpretacao e playbooks oficiais somente por
   `consultar_metodologia`.
3. Descubra o contrato vivo; nao fixe `tool_id`, campos, enums, status ou limiares.
4. Separe fatos retornados, calculos derivados, hipoteses e recomendacoes.
5. Informe periodo, filtros, denominador e granularidade de percentuais e comparacoes.
6. Diferencie universo completo, pagina e top N. Um ranking parcial nao sustenta sozinho uma
   participacao sobre o total.
7. Nao amplie filtros ou periodos quando o resultado for vazio.
8. Pergunte apenas valores ausentes que mudem materialmente a selecao do contrato ou o resultado.

## Portfolio

- Analise saude da carteira por composicao, movimento, valor, concentracao e geografia.
- Nao presuma que situacoes como positivo, inativo, bloqueado e congelado sejam mutuamente
  exclusivas ou formem uma particao exaustiva.
- Em receita, diferencie total, media, ranking e concentracao; preserve moeda e periodo.
- Em geografia, compare participacao, cobertura e concentracao sem inferir causa pela localizacao.
- Em comparacoes, alinhe periodo, metrica, dimensao e filtros; distinga variacao absoluta de
  variacao percentual.
- Se o motivo de um bloqueio ou congelamento nao estiver na fonte, nao o invente.

## Retencao

- Inatividade e um panorama de estoque; churn e uma perda ou nova inativacao ocorrida em um
  intervalo. Nao derive um do outro.
- Pre-inatividade ou sinais de risco dependem da definicao vigente do contrato e da metodologia;
  nao fixe dias, scores ou faixas no plugin.
- Diferencie quantidade de clientes, taxa, participacao e valor em risco.
- Priorize recuperacao por impacto, urgencia e recuperabilidade somente quando houver evidencias
  para esses criterios.
- Vincule recomendacoes a fatos atuais e ao playbook metodologico recuperado.

## Pedidos

- Organize o pipeline por etapas ou status atuais e distinga pendencia, bloqueio, perda e
  conclusao apenas quando o contrato sustentar essas categorias.
- Nao trate cancelado, reprovado, em analise, nao liberado e nao confirmado como codigos fixos.
- Separe quantidade, valor e tempo; um gargalo observado nao revela automaticamente sua causa.
- Compare funis somente com periodos e universos equivalentes.
- Nao confunda acumulado atual com entradas ou saidas ocorridas no periodo.

## Entrega

Comece pelo achado principal e mostre as evidencias que o sustentam. Termine com recorte,
limitacoes e proximas acoes. Use as ferramentas de artefato nativas do cliente quando um arquivo ou
visualizacao for solicitado; estas regras nao dependem do pipeline de documentos do runtime de
origem.
