# Custom & Non-7.4 Spells Guide

Eternum uses the 7.72 protocol but deeply expands the combat system by incorporating mechanics from modern Tibia and entirely custom spells. Below is a guide to the custom spell behaviors and non-7.4 spells you will encounter on the server.

## 1. Challenge Mechanics (Exeta Res)

In standard 7.4, `exeta res` simply caused a monster to retarget to the Knight for a brief moment. In Eternum, it works completely differently as a true "taunt" mechanic:

- **Aggro Lock:** When cast (`exeta res`), it affects a 3x3 area around the Knight. Any challengeable monster hit is **locked onto the Knight for 5 seconds**.
- **No Retargeting:** During these 5 seconds, the monster's natural tendency to change targets is completely ignored. They cannot switch targets under any circumstance.
- **No Fleeing:** Even if a monster reaches critical red health (or is a fleeing Elite), the 5-second challenge lock forces them to stand and fight.

## 2. Condition Cleansing Spells

Eternum features many new harmful status conditions (like Bleeding, Freezing, Dazzled, Cursed, and Drown). To combat this, several custom cleansing spells exist:

### Purify (`exana omni`)
- **Vocation:** All Vocations (must be explicitly learned).
- **Effect:** A self-cast spell that instantly cures **all** harmful damage-over-time conditions at once (Poison, Fire, Energy, Bleeding, Freezing, Dazzled, Cursed, Drown).

### Mass Cleanse (`exana mas res`)
- **Vocation:** Druids.
- **Effect:** An AoE support spell that affects a large circular area (radius 3) around the caster. It simultaneously heals allies and applies the `Purify` effect, cleansing all negative DoT conditions from every player hit.

### Specific Cures
- **Discharge (`exana vis`):** Instantly cures the Energy (electrified) condition.
- **Extinguish (`exana flam`):** Instantly cures the Burning (fire) condition.

## 3. Modern Spells in a Retro Client

To provide a more dynamic combat experience, Eternum includes many spells normally found in versions 8.0+:

### Knight Spells
- **Fierce Berserk (`exori gran`):** A significantly stronger version of Berserk that deals massive physical damage in a 3x3 area.
- **Groundshaker (`exori mas`):** An even larger AoE physical attack that hits a large circular area (radius 3) around the Knight.
- **Whirlwind Throw (`exori hur`):** Allows Knights to attack from a distance by throwing their weapon (3-tile range).

### Paladin Spells
- **Ethereal Spear (`exori con`):** A single-target ranged physical attack spell that scales with Distance skill and Level.
- **Divine Healing (`exura san`):** A fast, highly efficient heal specifically tailored for Paladins.
- **Holy Strike (`exori san`):** A single-target holy damage attack.
- **Divine Caldera (`exevo mas san`):** An AoE holy damage explosion in a large circular area (radius 3) around the Paladin.

### Mage Elemental Strikes
Mages have access to the full suite of modern single-target strikes with very low cooldowns, allowing them to weave spells between rune attacks:
- **Normal Strikes:** Flame Strike (`exori flam`), Energy Strike (`exori vis`), Ice Strike (`exori frigo`), Terra Strike (`exori tera`), Death Strike (`exori mort`).
  - **Great Strikes:** Higher mana cost, but deal the **same damage** as normal strikes. Instead of single-target, they expand into a 3x3 AoE area around the target/cast position (e.g., `exori gran flam`, `exori gran vis`, `exori gran frigo`).
- **Strong Ice Wave (`exevo gran frigo hur`):** A powerful directional ice wave for Druids.

## 4. Altered Retro Spells & Runes

Several classic spells and runes have had their damage types adjusted to better fit the custom mechanics:
- **Sudden Death Rune (SD):** Deals **Death** damage (not Physical damage like in standard 7.4).
- **Ultimate Explosion (`exevo gran mas vis`):** Deals **Physical** damage.
- **Poison Storm (`exevo gran mas pox`):** Deals **Physical** damage.
