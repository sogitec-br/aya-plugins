# Instalar AYA SOGI no Codex

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

Também é possível abrir o navegador de plugins no Codex e localizar **AYA SOGI Beta** depois de
adicionar o marketplace.

## Primeiro uso

1. feche a tarefa atual e abra uma nova tarefa;
2. peça ao Codex para usar AYA SOGI;
3. selecione **Authenticate** quando o SOGI solicitar conexão;
4. conclua o OAuth no navegador com sua própria conta;
5. volte ao Codex e repita a pergunta.

Nunca informe sua senha ao agente ou em arquivos do projeto.

## Atualização

```bash
codex plugin marketplace upgrade aya-plugins
codex plugin add aya-sogi@aya-plugins
```

Abra uma nova tarefa após atualizar.

## Diagnóstico

Verifique, nesta ordem:

1. marketplace `aya-plugins` aparece na lista;
2. plugin `aya-sogi` está instalado e habilitado;
3. uma nova tarefa foi aberta após a instalação;
4. OAuth foi concluído;
5. o MCP `sogi` está conectado;
6. a identidade possui autorização para a consulta solicitada.

Não publique logs com tokens ou dados SOGI em issues públicas.
