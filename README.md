# Polearm SFX fix

English | [PortuguÃªs (Brasil)](README.pt-BR.md)

I put this mod together to restore weapon sound effects in Baldur's Gate 3's strong masculine body type (BT4) attack animations.

**I am not a modder and I do not know programming. This project was made with an AI.** It solved the problem in my game. **I will not maintain the project or release updates.** I am sharing the source for anyone interested in studying it, improving it, or continuing the work.

## Version 1.2.0

I restored missing BT4 attack vocalizations and expanded the animation coverage:

- Polearm, staff and spear melee attacks, including selected shield and dual-wield attacks.
- Spear throws, with and without a shield.
- Shove and object throws in the game's Tiny and Medium size categories.

## The bug and the fix

My human BT4 character would attack with polearms without playing the weapon sounds. The same weapon worked on Shadowheart, and other weapon types had sound on my character. This pointed toward the animations used by BT4.

With the AI's help, I compared those animations with equivalent versions that had working audio. The fix:

- Restores `Whoosh_Combat`, missing from nine basic attack animations.
- Changes `SoundObjectIndex` from `2` to `1` in a reach attack, directing the sound to the main hand.
- Includes `CastPierce` in three piercing animations and puts events in chronological order.

I tested it in game and confirmed that polearm sounds returned. **The mod does not require Script Extender, Mod Fixer, or the BG3 Toolkit.**

## Install with Vortex

1. Download **`PolearmSFXFix-1.2.0.zip`** from Releases.
2. With BG3 closed, import the ZIP through **Mods â†’ Install From File**, enable the mod, and select **Deploy Mods**.
3. Check **Load Order** and export it to the game if automatic export is disabled.
4. In BG3, keep **Polearm SFX fix** enabled under **Mod Manager â†’ Installed** and when loading your save.

For manual installation, extract the PAK into `%LocalAppData%\Larian Studios\Baldur's Gate 3\Mods` and enable it in game. Use one installation method and replace older versions.

## Scope and compatibility

The package overrides fifteen `HUM_MS` resources covering polearm, staff and spear melee attacks, selected shield or dual-wield attacks, spear throws with and without a shield, shove, and Tiny/Medium object throws. It preserves animation properties and the original damage-related `Cast`/`React` timings, using the game's own sounds.

I have not individually tested every weapon, race, or multiplayer. Mods overriding the same resources can conflict; their IDs are listed in [docs/audit.json](docs/audit.json).

To uninstall through Vortex, disable or remove the mod and deploy again. For a manual installation, disable it and remove the PAK with BG3 closed. Your save may show a missing-mod notice.

## Continuing the work

I am leaving the project available for anyone who wants to fork it and continue development. The source and checks include [build instructions](docs/BUILD.md).

This is an unofficial project with no affiliation with Larian Studios. The original animation and audio resources belong to Larian.
