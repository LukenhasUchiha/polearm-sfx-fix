# Polearm SFX fix

[English](README.md) | PortuguÃªs (Brasil)

Preparei este mod para restaurar os efeitos sonoros de armas nas animaÃ§Ãµes do corpo masculino forte (BT4) de Baldur's Gate 3.

**NÃ£o sou modder e nÃ£o sei programaÃ§Ã£o. Este projeto foi feito com uma IA.** Ele resolveu o problema no meu jogo. **NÃ£o vou manter o projeto nem lanÃ§ar atualizaÃ§Ãµes.** Disponibilizo o cÃ³digo-fonte para quem quiser estudÃ¡-lo, melhorÃ¡-lo ou dar continuidade ao trabalho.

## O bug e a correÃ§Ã£o

Meu humano BT4 atacava com armas de haste sem reproduzir os sons da arma. A mesma arma funcionava na Shadowheart, e outros tipos de arma tinham som no meu personagem. Isso apontou para as animaÃ§Ãµes usadas pelo BT4.

Com a ajuda da IA, comparei essas animaÃ§Ãµes com versÃµes equivalentes que tinham Ã¡udio funcionando. A correÃ§Ã£o:

- RepÃµe `Whoosh_Combat`, ausente em nove animaÃ§Ãµes de ataque bÃ¡sico.
- Corrige `SoundObjectIndex` de `2` para `1` em um ataque de alcance, direcionando o som para a mÃ£o principal.
- Inclui `CastPierce` em trÃªs animaÃ§Ãµes perfurantes e organiza os eventos em ordem cronolÃ³gica.

Testei em jogo e confirmei o retorno do som das armas de haste. **O mod nÃ£o precisa de Script Extender, Mod Fixer nem do BG3 Toolkit.**

## InstalaÃ§Ã£o pelo Vortex

1. Baixe **`PolearmSFXFix-1.2.0.zip`** na seÃ§Ã£o Releases.
2. Com o BG3 fechado, importe o ZIP em **Mods â†’ Install From File**, habilite o mod e faÃ§a **Deploy Mods**.
3. Confira **Load Order** e exporte a ordem para o jogo se a exportaÃ§Ã£o automÃ¡tica estiver desligada.
4. No BG3, mantenha **Polearm SFX fix** ativo em **Mod Manager â†’ Installed** e ao carregar o save.

Para instalaÃ§Ã£o manual, extraia o PAK para `%LocalAppData%\Larian Studios\Baldur's Gate 3\Mods` e ative-o no jogo. Use apenas um mÃ©todo de instalaÃ§Ã£o e substitua versÃµes anteriores.

## Escopo e compatibilidade

O pacote altera dez recursos `HUM_MS`, usados por armas de haste, bordÃµes e algumas combinaÃ§Ãµes com escudo ou duas armas. Preserva as propriedades das animaÃ§Ãµes e os tempos originais de `Cast`/`React` relacionados ao dano, utilizando os sons do prÃ³prio jogo.

NÃ£o testei individualmente todas as armas, raÃ§as ou multiplayer. Mods que alterem os mesmos recursos podem conflitar; os IDs estÃ£o em [docs/audit.json](docs/audit.json).

Para remover pelo Vortex, desative ou remova o mod e faÃ§a Deploy. Na instalaÃ§Ã£o manual, desative-o e remova o PAK com o jogo fechado. O save pode avisar sobre a remoÃ§Ã£o.

## Continuidade

Deixo o projeto disponÃ­vel para quem quiser fazer um fork e continuar o desenvolvimento. As [instruÃ§Ãµes de construÃ§Ã£o](docs/BUILD.pt-BR.md) acompanham o cÃ³digo-fonte e as verificaÃ§Ãµes.

Este Ã© um projeto nÃ£o oficial, sem afiliaÃ§Ã£o com a Larian Studios. Os recursos originais de animaÃ§Ã£o e Ã¡udio pertencem Ã  Larian.
