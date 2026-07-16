# Instalar AyA no Codex

## Requisitos

- Codex atualizado com suporte a plugins;
- navegador disponível para concluir OAuth;
- conta SOGI individual autorizada;
- acesso HTTPS a `github.com` e `mcp.dev.ceppem.com`.

## Instalação pelo marketplace público

No terminal:

```bash
codex plugin marketplace add sogitec-br/aya-plugins
codex plugin add aya-sogi@aya-plugins
```

Também é possível abrir o navegador de plugins no Codex e localizar **AyA** depois de
adicionar o marketplace.

Se uma instalação antiga registrou o mesmo MCP manualmente, remova apenas esse registro global
depois de confirmar que o plugin está instalado:

```bash
codex mcp remove sogi
```

O plugin já fornece `https://mcp.dev.ceppem.com/mcp`; manter as duas declarações cria conexões e
diagnósticos duplicados.

## Primeiro uso

1. feche a tarefa atual e abra uma nova tarefa;
2. peça ao Codex para usar a AyA;
3. selecione **Authenticate** quando o SOGI solicitar conexão;
4. conclua o OAuth no navegador com sua própria conta;
5. feche essa tarefa e abra outra no mesmo projeto;
6. repita a pergunta na tarefa nova, que receberá o snapshot autenticado das tools.

Nunca informe sua senha ao agente ou em arquivos do projeto.

## Atualização

```bash
codex plugin marketplace upgrade aya-plugins
codex plugin add aya-sogi@aya-plugins
```

Abra uma nova tarefa após atualizar.

Ao migrar de `0.1.x` para `0.2.x`, a consulta continua funcionando com a sessão anterior, mas o
cadastro pode pedir **Authenticate** uma vez para consentir com o novo escopo de criação. Faça essa
reconexão pela interface do Codex; nunca cole a senha na conversa.

## Diagnóstico

Verifique, nesta ordem:

1. marketplace `aya-plugins` aparece na lista;
2. plugin `aya-sogi` está instalado e habilitado;
3. uma nova tarefa foi aberta após a instalação;
4. OAuth foi concluído;
5. uma nova tarefa foi aberta depois do OAuth;
6. uma tool SOGI aparece diretamente na tarefa;
7. a identidade possui autorização para a consulta solicitada.

Não publique logs com tokens ou dados SOGI em issues públicas.
