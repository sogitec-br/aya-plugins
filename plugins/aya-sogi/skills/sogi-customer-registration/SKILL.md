---
name: sogi-customer-registration
description: Prepara, valida, revisa e executa cadastro de cliente no SOGI com aprovacao explicita. Use quando o usuario pedir para cadastrar ou criar um cliente; nao use para apenas consultar, analisar ou explicar dados de clientes existentes.
---

# Cadastrar cliente no SOGI

Leia `../../references/customer-registration.md` antes de iniciar qualquer escrita.

1. Confirme que o pedido e realmente criar um cliente e que os dados sao destinados ao ambiente
   conectado. Como o endpoint atual e de desenvolvimento, use somente cadastros de teste
   autorizados pela equipe SOGI.
2. Chame `sogi_preparar_cadastro_cliente` diretamente com `dados`. Nao passe cadastro pela
   descoberta nem tente construir URLs internas.
3. Trate a resposta como o contrato atual:
   - em `needs_input` ou `invalid`, mostre pendencias e solicite somente os valores necessarios;
   - para lookups, use exatamente o `value` de uma opcao devolvida; nunca invente IDs;
   - preserve os dados informados pelo usuario quando houver conflito de enriquecimento;
   - reenvie os dados corrigidos e acumulados para uma nova preparacao.
4. Em `reauthorization_required`, oriente o usuario a reconectar o MCP pelo proprio cliente para
   consentir com o escopo indicado. Nao solicite senha, token, cookie ou header na conversa.
5. Em `ready_write_disabled`, entregue a previa e informe que a escrita nao esta habilitada para
   aquela identidade ou ambiente. Nao procure outro caminho de POST.
6. Em `requires_confirmation`, apresente a previa mascarada e os avisos, entregue o
   `approval_url` exato e informe o prazo. Aguarde a mesma pessoa revisar e aprovar no navegador;
   essa pagina reutiliza a sessao OAuth e nao exige um segundo login normal.
7. Chame `sogi_cadastrar_cliente` somente depois da aprovacao explicita, enviando exclusivamente o
   `operation_id`. Nunca envie novamente dados do cliente, token de aprovacao, tenant ou
   representante para a tool de execucao.
8. Retorne o estado e os identificadores seguros. Se o resultado for `unknown`, nao tente de novo,
   nao prepare duplicata automaticamente e oriente a verificacao no ambiente de desenvolvimento.
9. Se a operacao expirar, for cancelada, falhar por validacao ou apontar mudanca de contrato,
   explique o motivo e prepare uma nova somente com autorizacao do usuario.

Preparar nao cadastra. Abrir a pagina nao aprova. Aprovar nao executa. Mantenha essas tres
fronteiras explicitas durante toda a conversa.
