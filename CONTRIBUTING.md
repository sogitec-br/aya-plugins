# Contribuição

Este é um repositório público proprietário, não um projeto open source. Pull requests externos não
são aceitos sem autorização escrita prévia.

É permitido abrir issues para relatar problemas de instalação ou documentação, desde que nenhum
segredo, dado pessoal ou conteúdo SOGI seja publicado.

Vulnerabilidades devem seguir [SECURITY.md](SECURITY.md), nunca uma issue pública.

Mantenedores autorizados devem:

1. trabalhar em branch;
2. atualizar `VERSION`, manifestos e `CHANGELOG.md` juntos;
3. executar `python3 scripts/validate_repository.py`;
4. executar `bash scripts/build_releases.sh`;
5. revisar o conteúdo público e a ausência de segredos;
6. abrir pull request para `main`.
