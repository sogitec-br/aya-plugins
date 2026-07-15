# Contrato do gateway SOGI

O MCP separa conhecimento, consultas operacionais e cadastro em rotas diferentes.

## Conhecimento metodologico

Use `consultar_metodologia(pergunta)` diretamente para conceitos, funcionamento do SOGI,
interpretacao e recomendacoes CEPPEM. Essa tool nao usa descoberta nem `tool_id` e nao devolve
fatos operacionais atuais.

## Consultas operacionais

Use duas tools para leitura:

1. `sogi_descobrir_consultas(query, limit)` devolve os contratos autorizados mais aderentes;
2. `sogi_executar_consulta(tool_id, arguments)` executa um contrato descoberto.

Sempre descubra primeiro. Compare titulo, descricao, escopo e `input_schema`; preserve o `tool_id`
exatamente e envie apenas argumentos validos para aquele schema. Nao reutilize contrato de outra
sessao, invente IDs ou construa URLs internas. Uma shortlist vazia e abstencao segura, nao
autorizacao para tentar outro endpoint.

## Cadastro de cliente

Use duas tools diretas, sem descoberta semantica:

1. `sogi_preparar_cadastro_cliente(dados)` consulta o contrato vivo, valida e enriquece os dados;
2. `sogi_cadastrar_cliente(operation_id)` executa somente uma operacao preparada e aprovada.

A preparacao pode devolver pendencias, valores de lookup, reautorizacao, escrita desabilitada ou
um `approval_url`. O usuario autenticado revisa e confirma na pagina segura; somente depois a tool
de execucao recebe o `operation_id`. Dados do cliente, tenant, representante e token da aprovacao
nunca entram na chamada de execucao.

Leia `customer-registration.md` para os estados e as regras de falha segura.
