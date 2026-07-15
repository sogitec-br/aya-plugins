# Cadastro de cliente pelo MCP

Cadastro e uma capacidade separada das consultas de leitura. Ela usa tools estaveis e nao passa
por descoberta semantica.

## Fluxo publico

```text
dados parciais
    -> sogi_preparar_cadastro_cliente
    -> corrigir pendencias e escolher lookups devolvidos
    -> previa + approval_url temporario
    -> revisao e aprovacao pela mesma sessao OAuth no navegador
    -> sogi_cadastrar_cliente(operation_id)
    -> resultado seguro
```

`sogi_preparar_cadastro_cliente(dados)` e somente leitura. Ela consulta o contrato vivo do tenant,
valida CNPJ e CEP, aplica apenas enriquecimentos permitidos e resolve lookups. Reenvie os dados
corrigidos usando os caminhos e `value` devolvidos pela tool ate um estado terminal da preparacao.

`sogi_cadastrar_cliente(operation_id)` e escrita. Ela aparece somente para identidades liberadas
com o escopo de criacao. Recebe apenas o identificador de uma operacao preparada e aprovada pela
mesma pessoa.

## Estados da preparacao

- `invalid`: corrija os campos invalidos e prepare novamente.
- `needs_input`: complete campos obrigatorios ou lookups pendentes e prepare novamente.
- `reauthorization_required`: reconecte o MCP pelo cliente para consentir com o escopo indicado.
- `ready_write_disabled`: a previa e valida, mas a escrita nao esta disponivel.
- `requires_confirmation`: mostre a previa e abra o `approval_url` antes de executar.

O link de aprovacao e temporario e vinculado ao usuario, tenant e cliente OAuth que prepararam a
operacao. A pagina reutiliza a sessao criada no login do MCP; ela nao pede um segundo login normal.
Abrir o link nao equivale a aprovar.

## Execucao e falhas

- Execute somente depois de o usuario confirmar que aprovou a previa.
- Envie exclusivamente `operation_id`; nao envie payload, tenant, representante ou token.
- Uma operacao concluida devolve o mesmo resultado seguro em chamadas seguintes, sem novo POST.
- Operacao expirada, cancelada, com contrato alterado ou validacao obsoleta precisa ser preparada
  novamente.
- Timeout, falha de rede ou erro incerto depois do POST produz `unknown`. Nao repita, nao crie outra
  operacao automaticamente e confirme o estado no ambiente antes de qualquer nova tentativa.

## Ambiente atual

O endpoint do plugin e de desenvolvimento. Use apenas tenant e dados de teste autorizados. O MCP
mantem aprovacao, payload protegido, auditoria e protecao contra repeticao. Um resultado `unknown`
exige verificacao operacional antes de qualquer novo cadastro.
