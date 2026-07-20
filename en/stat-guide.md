# Stat Guide

> Source: `rarityAttributes.lua` — Base Power 300; Soft Cap 1.40.

## How attribute rolls scale

`maximum = clamp(Item Power × factor, 1, base maximum × 1.40)`

## Tier multipliers

| Tier | Multiplier |
| --- | ---: |
| Tier 1 | x0.4 |
| Tier 2 | x0.5 |
| Tier 3 | x0.6 |
| Tier 4 | x0.75 |
| Tier 5 | x0.9 |
| Tier 6 | x1.2 |

## Attribute rolls

| Server attribute | Attribute | Base maximum | Soft cap | Roll chance | Eligible categories |
| --- | --- | ---: | ---: | ---: | --- |
| `ITEM_RND_DAMAGE_DEATH` | Death damage | 4 | 5.6 | 5% | Jewelry, Boots, Quivers, Weapons, Shields, Backpacks |
| `ITEM_RND_DAMAGE_EARTH` | Earth damage | 4 | 5.6 | 5% | Jewelry, Boots, Quivers, Weapons, Shields, Backpacks |
| `ITEM_RND_DAMAGE_ENERGY` | Energy damage | 4 | 5.6 | 5% | Jewelry, Boots, Quivers, Weapons, Shields, Backpacks |
| `ITEM_RND_DAMAGE_FIRE` | Fire damage | 4 | 5.6 | 5% | Jewelry, Boots, Quivers, Weapons, Shields, Backpacks |
| `ITEM_RND_DAMAGE_HOLY` | Holy damage | 4 | 5.6 | 5% | Jewelry, Boots, Quivers, Weapons, Shields, Backpacks |
| `ITEM_RND_DAMAGE_ICE` | Ice damage | 4 | 5.6 | 5% | Jewelry, Boots, Quivers, Weapons, Shields, Backpacks |
| `ITEM_RND_DAMAGE_PHYSICAL` | Physical damage | 4 | 5.6 | 5% | Jewelry, Boots, Quivers, Weapons, Shields, Backpacks |
| `ITEM_RND_ARMOR` | Armor | 5 | 7 | 5% | Armor, Amulets |
| `ITEM_RND_ATTACK` | Attack | 9 | 12.6 | 10% | Melee weapons, Distance weapons |
| `ITEM_RND_DEF` | Defense | 9 | 12.6 | 5% | Shields |
| `ITEM_RND_EXP_BONUS` | Experience bonus | 6.6 | 9.24 | 5% | Armor, Jewelry, Backpacks |
| `ITEM_RND_WEIGHT_REDUCTION` | Weight reduction | 150 | 210 | 0% | All equipment |
| `ITEM_RND_LIFELEECH_AMOUNT` | Life leech amount | 4 | 5.6 | 0% | Weapons, Boots, Jewelry, Helmet |
| `ITEM_RND_LIFELEECH_CHANCE` | Life leech chance | 4 | 5.6 | 5% | Weapons, Boots, Jewelry, Helmet |
| `ITEM_RND_MANALEECH_AMOUNT` | Mana leech amount | 4 | 5.6 | 0% | Weapons, Boots, Jewelry, Helmet |
| `ITEM_RND_MANALEECH_CHANCE` | Mana leech chance | 4 | 5.6 | 5% | Weapons, Boots, Jewelry, Helmet |
| `ITEM_RND_RESISTANCE` | Resistance | 2.5 | 3.5 | 5% | Armor, Shields, Jewelry, Backpacks |
| `ITEM_RND_RESIST_DEATH` | Death resistance | 3 | 4.2 | 5% | Armor, Shields, Jewelry, Backpacks |
| `ITEM_RND_RESIST_ENERGY` | Energy resistance | 3 | 4.2 | 5% | Armor, Shields, Jewelry, Backpacks |
| `ITEM_RND_RESIST_FIRE` | Fire resistance | 3 | 4.2 | 5% | Armor, Shields, Jewelry, Backpacks |
| `ITEM_RND_RESIST_HOLY` | Holy resistance | 3 | 4.2 | 5% | Armor, Shields, Jewelry, Backpacks |
| `ITEM_RND_RESIST_ICE` | Ice resistance | 3 | 4.2 | 5% | Armor, Shields, Jewelry, Backpacks |
| `ITEM_RND_RESIST_PHYSICAL` | Physical resistance | 3 | 4.2 | 5% | Armor, Shields, Jewelry, Backpacks |
| `ITEM_RND_RESIST_POISON` | Poison resistance | 3 | 4.2 | 5% | Armor, Shields, Jewelry, Backpacks |
| `ITEM_RND_ATTACK_SPEED` | Attack speed | 3.2 | 4.48 | 10% | Jewelry, Chest armor, Boots, Weapons, Backpacks |
| `ITEM_RND_CRITICAL` | Critical chance | 3 | 4.2 | 10% | Jewelry, Boots, Weapons, Quivers, Shields, Backpacks |
| `ITEM_RND_LOOT_CHANCE` | Loot chance | 15 | 21 | 5% | Jewelry, Boots, Backpacks |
| `ITEM_RND_MAGICLEVEL_PERCENT` | Magic level percentage | 3.2 | 4.48 | 10% | Wands, Armor, Jewelry, Shields, Backpacks |
| `ITEM_RND_PARRY` | Parry | 4 | 5.6 | 5% | Shields, Chest armor, Trinkets |
| `ITEM_RND_SHARPSHOOTER` | Sharpshooter | 4 | 5.6 | 5% | Chest armor, Legs, Helmet, Quivers, Trinkets |
| `ITEM_RND_SKILL` | Skill bonus | 4.7 | 6.58 | 10% | Weapons, Shields, Armor, Jewelry, Quivers, Backpacks |
| `ITEM_RND_SPEED` | Movement speed | 52.5 | 73.5 | 5% | Boots, Amulets |
| `ITEM_RND_BERSERK` | Berserk | 4.5 | 6.3 | 5% | Chest armor, Legs, Helmet, Trinkets |
| `ITEM_RND_CRUSHING_BLOW` | Crushing blow | 8.5 | 11.9 | 0% | Distance weapons, Quivers |
| `ITEM_RND_FAST_HAND` | Fast hand | 3.5 | 4.9 | 5% | Weapons, Jewelry, Boots, Helmet, Backpacks |
| `ITEM_RND_MULTISHOT` | Multishot | 7.5 | 10.5 | 5% | Distance weapons |
| `ITEM_RND_PARALYZE` | Paralyze | 4.5 | 6.3 | 1% | Weapons |
| `ITEM_RND_PERSEVERANCE` | Perseverance | 4.5 | 6.3 | 0% | Chest armor, Legs, Helmet, Trinkets |
| `ITEM_RND_BLEEDING` | Bleeding | 3.5 | 4.9 | 5% | Jewelry, Boots, Weapons, Backpacks |
| `ITEM_RND_BURNING` | Burning | 3.5 | 4.9 | 5% | Jewelry, Boots, Weapons, Backpacks |
| `ITEM_RND_ELETRICFYING` | Electrifying | 3.5 | 4.9 | 5% | Jewelry, Boots, Weapons, Backpacks |
| `ITEM_RND_POISONING` | Poisoning | 3.5 | 4.9 | 5% | Jewelry, Boots, Weapons, Backpacks |
| `ITEM_RND_DEATH_STRIKE_CHANCE` | Death strike chance | 21 | 29.4 | 5% | Weapons |
| `ITEM_RND_EARTH_STRIKE_CHANCE` | Earth strike chance | 21 | 29.4 | 5% | Weapons |
| `ITEM_RND_ENERGY_STRIKE_CHANCE` | Energy strike chance | 21 | 29.4 | 5% | Weapons |
| `ITEM_RND_FIRE_STRIKE_CHANCE` | Fire strike chance | 21 | 29.4 | 5% | Weapons |
| `ITEM_RND_HOLY_STRIKE_CHANCE` | Holy strike chance | 21 | 29.4 | 5% | Weapons |
| `ITEM_RND_ICE_STRIKE_CHANCE` | Ice strike chance | 21 | 29.4 | 5% | Weapons |
| `ITEM_RND_HEALTH_REGEN` | Health regeneration | 6 | 8.4 | 0% | All equipment |
| `ITEM_RND_MANA_REGEN` | Mana regeneration | 6 | 8.4 | 0% | All equipment |
| `ITEM_RND_MAX_HEALTH` | Maximum health | 240 | 336 | 5% | Jewelry |
| `ITEM_RND_MAX_MANA` | Maximum mana | 240 | 336 | 5% | Jewelry |

Generated from rarityAttributes.lua; do not edit attribute rows manually.
