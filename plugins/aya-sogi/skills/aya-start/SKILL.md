---
name: aya-start
description: Inicializa e orienta o primeiro uso da AyA. Use quando o usuario abrir o projeto, pedir onboarding, conectar o SOGI ou perguntar como comecar.
---

# Iniciar AYA

1. Identifique se o usuario esta no Codex ou no Claude e confirme que o plugin `aya-sogi` esta
   habilitado no cliente.
2. Verifique se o MCP `sogi` e suas tools aparecem na sessao sem imprimir configuracoes sensiveis.
3. Se o MCP exigir OAuth, instrua o usuario a usar a acao **Authenticate** ou **Connect** exibida
   pelo proprio cliente. Nao solicite credenciais na conversa.
4. Depois do primeiro OAuth, da reconexao ou de uma atualizacao do plugin, oriente o usuario a
   abrir uma nova tarefa no mesmo projeto. A tarefa anterior pode manter o snapshot de tools criado
   antes da autenticacao.
5. Na nova tarefa, confirme a presenca de uma tool SOGI diretamente. Nao use
   `list_mcp_resources`, configuracao local ou status textual como prova de disponibilidade.
6. Depois dessa confirmacao, chame `sogi_descobrir_consultas` com uma intencao de teste somente
   leitura fornecida pelo usuario.
7. Nao execute uma consulta de negocio apenas para testar sem informar ao usuario qual intencao
   sera consultada.
8. Ao concluir, explique as tres rotas disponiveis:
   - conhecimento: `consultar_metodologia` diretamente;
   - dados operacionais: `descobrir -> validar schema -> executar`;
   - cadastro de cliente: `preparar -> revisao e aprovacao no navegador -> executar`.
9. Informe que a rota de cadastro e uma escrita separada, pode exigir novo consentimento OAuth
   para o escopo de criacao e nunca deve ser usada como teste de conectividade.

Nunca solicite que o usuario cole senha, token ou cookie na conversa. Nao abra outro processo do
Codex para contornar tools ausentes na tarefa atual.
