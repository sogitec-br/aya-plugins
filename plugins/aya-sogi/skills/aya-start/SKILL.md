---
name: aya-start
description: Inicializa e orienta o primeiro uso do workspace AYA SOGI. Use quando o usuario abrir o projeto, pedir onboarding, conectar o SOGI ou perguntar como comecar.
---

# Iniciar AYA

1. Identifique se o usuario esta no Codex ou no Claude e confirme que o plugin `aya-sogi` esta
   habilitado no cliente.
2. Verifique se o MCP `sogi` e suas tools aparecem na sessao sem imprimir configuracoes sensiveis.
3. Se o MCP exigir OAuth, instrua o usuario a usar a acao **Authenticate** ou **Connect** exibida
   pelo proprio cliente. Nao solicite credenciais na conversa.
4. Se o plugin acabou de ser instalado ou atualizado, oriente o recarregamento do cliente antes de
   concluir que o MCP esta indisponivel.
5. Depois da autenticacao, chame `sogi_descobrir_consultas` com uma intencao de teste somente
   leitura fornecida pelo usuario.
6. Nao execute uma consulta de negocio apenas para testar sem informar ao usuario qual intencao
   sera consultada.
7. Ao concluir, explique que toda operacao de dados segue
   `descobrir -> validar schema -> executar`.

Nunca solicite que o usuario cole senha, token ou cookie na conversa.
