---
name: aya-doctor
description: Diagnostica o workspace AYA, o plugin e a conexao MCP SOGI sem alterar dados. Use para falhas de instalacao, autenticacao, catalogo, tools ou conectividade.
---

# Diagnosticar AYA

1. Identifique o cliente e confirme se o plugin `aya-sogi` esta instalado, habilitado e carregado
   nesta sessao.
2. Separe o diagnostico em: plugin, MCP, rede, OAuth, tools e catalogo.
3. Confirme se as tools do MCP aparecem antes de tentar uma consulta. A ausencia delas pode exigir
   recarregar o cliente depois da instalacao ou atualizacao.
4. Se o servico estiver inacessivel, reporte conectividade antes de investigar catalogo.
5. Se o MCP estiver pendente de autenticacao, oriente **Authenticate** ou **Connect** pelo proprio
   cliente; nao manipule tokens nem solicite credenciais.
6. Se a conexao estiver ativa mas a descoberta estiver vazia, trate como catalogo, autorizacao ou
   intencao fora do contrato, nao como falha automatica de rede.
7. Somente amplie para uma consulta real quando o usuario fornecer a intencao exata.

O diagnostico e somente leitura. Nao reinstale, remova, revogue sessoes ou altere configuracoes sem
pedido explicito.
