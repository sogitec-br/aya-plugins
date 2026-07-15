# Instalar AyA no Claude Code

## Requisitos

- Claude Code atualizado com suporte a plugins;
- sessão local ou SSH no Claude Code Desktop;
- navegador disponível para concluir OAuth;
- conta SOGI individual autorizada;
- acesso HTTPS a `github.com` e `mcp.dev.ceppem.com`.

## Instalação

Dentro do Claude Code:

```text
/plugin marketplace add sogitec-br/aya-plugins
/plugin install aya-sogi@aya-plugins
/reload-plugins
```

No Claude Code Desktop, use **+ > Plugins > Add plugin** para navegar pelos marketplaces
configurados. Plugins não estão disponíveis em sessões cloud ou WSL do Desktop no momento desta
documentação.

## Primeiro uso

1. inicie uma nova sessão após a instalação;
2. invoque `/aya-sogi:aya-start` ou descreva sua pergunta diretamente;
3. conclua o OAuth com sua própria conta quando solicitado;
4. volte ao Claude e continue a conversa.

Nunca cole senha, token, cookie ou header na conversa.

## Atualização

```text
/plugin marketplace update aya-plugins
/plugin update aya-sogi@aya-plugins
/reload-plugins
```

Se o plugin continuar antigo, confirme a versão instalada, remova e instale novamente.

## Diagnóstico

Use `/plugin` para verificar marketplace, instalação, versão e erros. Depois confirme OAuth, MCP e
autorização da identidade SOGI.

Não publique logs com tokens ou dados SOGI em issues públicas.
