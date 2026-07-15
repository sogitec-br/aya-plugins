---
name: sogi-reporting
description: Produz relatorios e exportacoes rastreaveis a partir de consultas SOGI autorizadas. Use quando o usuario pedir arquivo, resumo executivo, relatorio, tabela ou exportacao.
---

# Relatorios SOGI

1. Confirme formato, audiencia e periodo quando forem materiais para a entrega.
2. Consulte os dados pelo fluxo obrigatorio do MCP.
3. Inclua pergunta original, horario, filtros, `tool_id`, resultado e limitacoes.
4. Identifique calculos derivados e nao apresente campos ausentes como zero.
5. Remova dados pessoais desnecessarios e nunca inclua credenciais ou headers.
6. Confirme o destino com o usuario. Sem destino explicito, use uma pasta apropriada no projeto
   atual e nunca grave dentro do diretorio de instalacao do plugin.
7. Crie diretorios ou sobrescreva arquivos somente quando isso estiver dentro do pedido do usuario.
8. Valide o arquivo gerado antes de entregar.

Use as ferramentas nativas de documento, planilha, apresentacao ou visualizacao do cliente quando
estiverem disponiveis. Esta skill governa conteudo e proveniencia SOGI; ela nao depende de um
pipeline especifico de artefatos.

Leia `../../references/governance.md` para as regras de minimizacao e proveniencia.
