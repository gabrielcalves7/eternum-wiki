# Guia de Atributos

> Fonte: `rarityAttributes.lua` — Poder Base 300; Teto Suave 1.40.

## Como as rolagens de atributos escalam

`máximo = limitar(Poder do Item × fator, 1, máximo base × 1.40)`

## Multiplicadores de tier

| Tier | Multiplicador |
| --- | ---: |
| Tier 1 | x0.4 |
| Tier 2 | x0.5 |
| Tier 3 | x0.6 |
| Tier 4 | x0.75 |
| Tier 5 | x0.9 |
| Tier 6 | x1.2 |

## Rolagens de atributos

| Atributo do servidor | Atributo | Máximo base | Teto suave | Chance de rolagem | Categorias elegíveis |
| --- | --- | --- | --- | ---: | --- |
| `ITEM_RND_DAMAGE_DEATH` | Dano de morte | 4 | 5.6 | 5% | Joias, Botas, Aljavas, Armas, Escudos, Mochilas |
| `ITEM_RND_DAMAGE_EARTH` | Dano de terra | 4 | 5.6 | 5% | Joias, Botas, Aljavas, Armas, Escudos, Mochilas |
| `ITEM_RND_DAMAGE_ENERGY` | Dano de energia | 4 | 5.6 | 5% | Joias, Botas, Aljavas, Armas, Escudos, Mochilas |
| `ITEM_RND_DAMAGE_FIRE` | Dano de fogo | 4 | 5.6 | 5% | Joias, Botas, Aljavas, Armas, Escudos, Mochilas |
| `ITEM_RND_DAMAGE_HOLY` | Dano sagrado | 4 | 5.6 | 5% | Joias, Botas, Aljavas, Armas, Escudos, Mochilas |
| `ITEM_RND_DAMAGE_ICE` | Dano de gelo | 4 | 5.6 | 5% | Joias, Botas, Aljavas, Armas, Escudos, Mochilas |
| `ITEM_RND_DAMAGE_PHYSICAL` | Dano físico | 4 | 5.6 | 5% | Joias, Botas, Aljavas, Armas, Escudos, Mochilas |
| `ITEM_RND_ARMOR` | Armadura | 5 | 7 | 5% | Armaduras, Amuletos |
| `ITEM_RND_ATTACK` | Ataque | 9 | 12.6 | 10% | Armas corpo a corpo, Armas à distância |
| `ITEM_RND_DEF` | Defesa | 9 | 12.6 | 5% | Escudos |
| `ITEM_RND_EXP_BONUS` | Bônus de experiência | 6.6 | 9.24 | 5% | Armaduras, Joias, Mochilas |
| `ITEM_RND_WEIGHT_REDUCTION` | Redução de peso | 150 | 210 | 0% | Todos os equipamentos |
| `ITEM_RND_LIFELEECH_AMOUNT` | Quantidade de roubo de vida | 4 | 5.6 | 0% | Armas, Botas, Joias, Elmo |
| `ITEM_RND_LIFELEECH_CHANCE` | Chance de roubo de vida | 4 | 5.6 | 5% | Armas, Botas, Joias, Elmo |
| `ITEM_RND_MANALEECH_AMOUNT` | Quantidade de roubo de mana | 4 | 5.6 | 0% | Armas, Botas, Joias, Elmo |
| `ITEM_RND_MANALEECH_CHANCE` | Chance de roubo de mana | 4 | 5.6 | 5% | Armas, Botas, Joias, Elmo |
| `ITEM_RND_RESISTANCE` | Resistência | 2.5 | 3.5 | 5% | Armaduras, Escudos, Joias, Mochilas |
| `ITEM_RND_RESIST_DEATH` | Resistência a morte | 3 | 4.2 | 5% | Armaduras, Escudos, Joias, Mochilas |
| `ITEM_RND_RESIST_ENERGY` | Resistência a energia | 3 | 4.2 | 5% | Armaduras, Escudos, Joias, Mochilas |
| `ITEM_RND_RESIST_FIRE` | Resistência a fogo | 3 | 4.2 | 5% | Armaduras, Escudos, Joias, Mochilas |
| `ITEM_RND_RESIST_HOLY` | Resistência sagrada | 3 | 4.2 | 5% | Armaduras, Escudos, Joias, Mochilas |
| `ITEM_RND_RESIST_ICE` | Resistência a gelo | 3 | 4.2 | 5% | Armaduras, Escudos, Joias, Mochilas |
| `ITEM_RND_RESIST_PHYSICAL` | Resistência física | 3 | 4.2 | 5% | Armaduras, Escudos, Joias, Mochilas |
| `ITEM_RND_RESIST_POISON` | Resistência a veneno | 3 | 4.2 | 5% | Armaduras, Escudos, Joias, Mochilas |
| `ITEM_RND_ATTACK_SPEED` | Velocidade de ataque | 3.2 | 4.48 | 10% | Joias, Armadura de peito, Botas, Armas, Mochilas |
| `ITEM_RND_CRITICAL` | Chance de crítico | 3 | 4.2 | 10% | Joias, Botas, Armas, Aljavas, Escudos, Mochilas |
| `ITEM_RND_LOOT_CHANCE` | Chance de saque | 15 | 21 | 5% | Joias, Botas, Mochilas |
| `ITEM_RND_MAGICLEVEL_PERCENT` | Porcentagem de nível mágico | 3.2 | 4.48 | 10% | Varinhas, Armaduras, Joias, Escudos, Mochilas |
| `ITEM_RND_PARRY` | Aparo | 4 | 5.6 | 5% | Escudos, Armadura de peito, Bugigangas |
| `ITEM_RND_SHARPSHOOTER` | Atirador de elite | 4 | 5.6 | 5% | Armadura de peito, Pernas, Elmo, Aljavas, Bugigangas |
| `ITEM_RND_SKILL` | Bônus de habilidade | 4.7 | 6.58 | 10% | Armas, Escudos, Armaduras, Joias, Aljavas, Mochilas |
| `ITEM_RND_SPEED` | Velocidade de movimento | 52.5 | 73.5 | 5% | Botas, Amuletos |
| `ITEM_RND_BERSERK` | Berserker | 4.5 | 6.3 | 5% | Armadura de peito, Pernas, Elmo, Bugigangas |
| `ITEM_RND_CRUSHING_BLOW` | Golpe esmagador | 8.5 | 11.9 | 0% | Armas à distância, Aljavas |
| `ITEM_RND_FAST_HAND` | Mão rápida | 3.5 | 4.9 | 5% | Armas, Joias, Botas, Elmo, Mochilas |
| `ITEM_RND_MULTISHOT` | Disparo múltiplo | 7.5 | 10.5 | 5% | Armas à distância |
| `ITEM_RND_PARALYZE` | Paralisia | 4.5 | 6.3 | 1% | Armas |
| `ITEM_RND_PERSEVERANCE` | Perseverança | 4.5 | 6.3 | 0% | Armadura de peito, Pernas, Elmo, Bugigangas |
| `ITEM_RND_BLEEDING` | Sangramento | 3.5 | 4.9 | 5% | Joias, Botas, Armas, Mochilas |
| `ITEM_RND_BURNING` | Queimadura | 3.5 | 4.9 | 5% | Joias, Botas, Armas, Mochilas |
| `ITEM_RND_ELETRICFYING` | Eletrificação | 3.5 | 4.9 | 5% | Joias, Botas, Armas, Mochilas |
| `ITEM_RND_POISONING` | Envenenamento | 3.5 | 4.9 | 5% | Joias, Botas, Armas, Mochilas |
| `ITEM_RND_DEATH_STRIKE_CHANCE` | Chance de golpe de morte | 21 | 29.4 | 5% | Armas |
| `ITEM_RND_EARTH_STRIKE_CHANCE` | Chance de golpe de terra | 21 | 29.4 | 5% | Armas |
| `ITEM_RND_ENERGY_STRIKE_CHANCE` | Chance de golpe de energia | 21 | 29.4 | 5% | Armas |
| `ITEM_RND_FIRE_STRIKE_CHANCE` | Chance de golpe de fogo | 21 | 29.4 | 5% | Armas |
| `ITEM_RND_HOLY_STRIKE_CHANCE` | Chance de golpe sagrado | 21 | 29.4 | 5% | Armas |
| `ITEM_RND_ICE_STRIKE_CHANCE` | Chance de golpe de gelo | 21 | 29.4 | 5% | Armas |
| `ITEM_RND_HEALTH_REGEN` | Regeneração de vida | 6 | 8.4 | 0% | Todos os equipamentos |
| `ITEM_RND_MANA_REGEN` | Regeneração de mana | 6 | 8.4 | 0% | Todos os equipamentos |
| `ITEM_RND_MAX_HEALTH` | Vida máxima | 240 | 336 | 5% | Joias |
| `ITEM_RND_MAX_MANA` | Mana máxima | 240 | 336 | 5% | Joias |

Gerado de rarityAttributes.lua; não edite manualmente as linhas de atributos.
