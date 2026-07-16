---
name: aya-doctor
description: Diagnostica o workspace AYA, o plugin e a conexao MCP SOGI sem alterar dados. Use para falhas de instalacao, autenticacao, catalogo, tools ou conectividade.
---

# Diagnosticar AYA

1. Identifique o cliente e confirme se o plugin `aya-sogi` esta instalado, habilitado e carregado
   nesta sessao.
2. Separe o diagnostico em: plugin, MCP, rede, OAuth, tools e catalogo.
3. Confirme se as tools do MCP aparecem antes de tentar uma consulta.
   - `enabled=true`, `Auth=OAuth` ou a presenca do endpoint provam apenas configuracao;
   - `list_mcp_resources` lista resources, nao as tools operacionais do SOGI;
   - considere a conexao pronta somente quando uma tool SOGI estiver disponivel para chamada.
   Verifique separadamente as tools consultivas, `consultar_metodologia` e as tools de cadastro,
   pois elas podem variar por tenant, perfil e escopo OAuth.
4. Se o servico estiver inacessivel, reporte conectividade antes de investigar catalogo.
5. Se o MCP estiver pendente de autenticacao, oriente **Authenticate** ou **Connect** pelo proprio
   cliente; nao manipule tokens nem solicite credenciais.
6. Se o OAuth acabou de ser concluido, mas as tools nao aparecem na tarefa atual, informe que a
   tarefa foi criada com um snapshot anterior das tools. Oriente abrir uma nova tarefa no mesmo
   projeto e repetir a pergunta. Nao use outro `codex exec`, terminal ou processo aninhado como
   substituto.
7. Se uma tool SOGI estiver disponivel, mas a descoberta estiver vazia, trate como catalogo,
   autorizacao ou
   intencao fora do contrato, nao como falha automatica de rede.
8. Se a preparacao de cadastro aparecer mas a execucao nao, trate primeiro como escopo de escrita,
   perfil ou flag do ambiente; nao conclua que o MCP inteiro falhou.
9. Somente amplie para uma consulta real quando o usuario fornecer a intencao exata. Nao crie um
   cadastro para diagnosticar conexao.

Nunca afirme que a AyA esta autenticada com base apenas em arquivo de configuracao, manifesto,
status textual ou tentativa de refresh. Diferencie explicitamente configurado, autenticado e
disponivel nesta tarefa.

O diagnostico e somente leitura. Nao reinstale, remova, revogue sessoes ou altere configuracoes sem
pedido explicito.
