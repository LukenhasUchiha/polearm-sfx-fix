# Polearm SFX fix

[English](README.md) | Português (Brasil)

Preparei este mod para restaurar os efeitos sonoros de armas nas animações do corpo masculino forte (BT4) de Baldur's Gate 3.

**Não sou modder e não sei programação. Este projeto foi feito com uma IA.** Ele resolveu o problema no meu jogo. **Não vou manter o projeto nem lançar atualizações.** Disponibilizo o código-fonte para quem quiser estudá-lo, melhorá-lo ou dar continuidade ao trabalho.

## O bug e a correção

Meu humano BT4 atacava com armas de haste sem reproduzir os sons da arma. A mesma arma funcionava na Shadowheart, e outros tipos de arma tinham som no meu personagem. Isso apontou para as animações usadas pelo BT4.

Com a ajuda da IA, comparei essas animações com versões equivalentes que tinham áudio funcionando. A correção:

- Repõe `Whoosh_Combat`, ausente em nove animações de ataque básico.
- Corrige `SoundObjectIndex` de `2` para `1` em um ataque de alcance, direcionando o som para a mão principal.
- Inclui `CastPierce` em três animações perfurantes e organiza os eventos em ordem cronológica.

Testei em jogo e confirmei o retorno do som das armas de haste. **O mod não precisa de Script Extender, Mod Fixer nem do BG3 Toolkit.**

## Instalação pelo Vortex

1. Baixe **`PolearmSFXFix-1.1.0.zip`** na seção Releases.
2. Com o BG3 fechado, importe o ZIP em **Mods → Install From File**, habilite o mod e faça **Deploy Mods**.
3. Confira **Load Order** e exporte a ordem para o jogo se a exportação automática estiver desligada.
4. No BG3, mantenha **Polearm SFX fix** ativo em **Mod Manager → Installed** e ao carregar o save.

Para instalação manual, extraia o PAK para `%LocalAppData%\Larian Studios\Baldur's Gate 3\Mods` e ative-o no jogo. Use apenas um método de instalação e substitua versões anteriores.

## Escopo e compatibilidade

O pacote altera dez recursos `HUM_MS`, usados por armas de haste, bordões e algumas combinações com escudo ou duas armas. Preserva as propriedades das animações e os tempos originais de `Cast`/`React` relacionados ao dano, utilizando os sons do próprio jogo.

Não testei individualmente todas as armas, raças ou multiplayer. Mods que alterem os mesmos recursos podem conflitar; os IDs estão em [docs/audit.json](docs/audit.json).

Para remover pelo Vortex, desative ou remova o mod e faça Deploy. Na instalação manual, desative-o e remova o PAK com o jogo fechado. O save pode avisar sobre a remoção.

## Continuidade

Deixo o projeto disponível para quem quiser fazer um fork e continuar o desenvolvimento. As [instruções de construção](docs/BUILD.pt-BR.md) acompanham o código-fonte e as verificações.

Este é um projeto não oficial, sem afiliação com a Larian Studios. Os recursos originais de animação e áudio pertencem à Larian.
