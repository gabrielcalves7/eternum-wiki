# ✨ Custom & Non-7.4 Spells Guide

Eternum uses the 7.72 protocol but deeply expands the combat system by incorporating mechanics from modern Tibia and entirely custom spells. Below is a guide to the custom spell behaviors and non-7.4 spells you will encounter on the server.

## 🛡️ Challenge Mechanics (Exeta Res)

In standard 7.4, `exeta res` simply caused a monster to retarget to the Knight for a brief moment. In Eternum, it works completely differently as a true **taunt mechanic**:

{% hint style="info" %}
**Challenge Mechanics:**
- **Aggro Lock:** When cast (`exeta res`), it affects a 3x3 area around the Knight. Any challengeable monster hit is **locked onto the Knight for 5 seconds**.
- **No Retargeting:** During these 5 seconds, the monster's natural tendency to change targets is completely ignored. They cannot switch targets under any circumstance.
- **No Fleeing:** Even if a monster reaches critical red health (or is a fleeing Elite), the 5-second challenge lock forces them to stand and fight.
{% endhint %}

## 🧪 Condition Cleansing Spells

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

## ⚔️ Modern Spells in a Retro Client

To provide a more dynamic combat experience, Eternum includes many spells normally found in versions 8.0+:

### Knight Spells
| Spell | Words | Description |
| --- | --- | --- |
| **Fierce Berserk** | `exori gran` | A significantly stronger version of Berserk that deals massive physical damage in a 3x3 area. |
| **Groundshaker** | `exori mas` | An even larger AoE physical attack that hits a large circular area (radius 3) around the Knight. |
| **Whirlwind Throw** | `exori hur` | Allows Knights to attack from a distance by throwing their weapon (3-tile range). |

### Paladin Spells
| Spell | Words | Description |
| --- | --- | --- |
| **Ethereal Spear** | `exori con` | A single-target ranged physical attack spell that scales with Distance skill and Level. |
| **Divine Healing** | `exura san` | A fast, highly efficient heal specifically tailored for Paladins. |
| **Holy Strike** | `exori san` | A single-target holy damage attack. |
| **Divine Caldera** | `exevo mas san` | An AoE holy damage explosion in a large circular area (radius 3) around the Paladin. |

### Mage Elemental Strikes
Mages have access to the full suite of modern single-target strikes with very low cooldowns, allowing them to weave spells between rune attacks:

| Category | Words | Description |
| --- | --- | --- |
| **Normal Strikes** | `exori flam`, `exori vis`, `exori frigo`, `exori tera`, `exori mort` | Single-target elemental strikes with low cooldowns. |
| **Great Strikes** | `exori gran flam`, `exori gran vis`, `exori gran frigo` | Expand into a 3x3 AoE area around target with higher mana cost, dealing same damage as normal strikes. |
| **Strong Ice Wave** | `exevo gran frigo hur` | A powerful directional ice wave specifically for Druids. |

## 🔄 Altered Retro Spells & Runes

Several classic spells and runes have had their damage types adjusted to better fit custom mechanics:

| Spell / Rune | Words | Damage Type / Behavior Change |
| --- | --- | --- |
| **Sudden Death Rune (SD)** | `adori vita vis` | Deals **Death** damage (instead of Physical damage in standard 7.4). |
| **Ultimate Explosion** | `exevo gran mas vis` | Deals **Physical** damage. |
| **Poison Storm** | `exevo gran mas pox` | Deals **Physical** damage. |
