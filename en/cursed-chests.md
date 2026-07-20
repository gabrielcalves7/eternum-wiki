# Cursed Chests System

The **Cursed Chests** system is a custom event where special chests spawn randomly in the world around major towns. Players can open these chests to trigger a multi-wave combat event, which upon successful completion, yields powerful rewards including items with rarity attributes and various upgrade orbs.

## 1. Tiers and Requirements

Cursed Chests come in four distinct tiers, which determine the minimum level required to open them, the difficulty of the monsters spawned, and the quality of the loot.

| Tier | Chest Type | Min Level | Spawn Chance | Monsters per Wave |
| :--- | :--- | :--- | :--- | :--- |
| 1 | Common | 20 | 70% | 3 |
| 2 | Rare | 40 | 50% | 3 |
| 3 | Epic | 60 | 30% | 4 |
| 4 | Legendary | 90 | 10% | 4 |

## 2. Spawn Mechanics

- **Interval:** New chests attempt to spawn every hour (60 minutes).
- **Locations:** Chests spawn within a 500-tile radius around the temple positions of major towns (Ankrahmun, Darashia, Thais, Carlin, Edron, Venore, Ab'Dendriel, Yalahar, Svargrond). 
- **Distance Constraints:** Chests will not spawn closer than 100 tiles from a town temple, and they are spaced out at least 15 tiles from other active chests.
- **Capacity:** The server spawns up to 6 chests globally per cycle.
- **Visuals:** When idle, chests emit an animated "bats" magic effect and display floating text indicating their tier (e.g., "Legendary Cursed Chest").

## 3. The Event (Waves & Combat)

Opening a chest triggers the event. The player (and anyone nearby) must defeat **5 waves** of monsters.

- **Monsters Selection:** The monsters for the waves are pulled dynamically from the daily tasks monster pool, based on the chest's tier. The monsters scale progressively in power from Wave 1 to Wave 5.
- **Skulls and Difficulty:** Monsters have an increasing chance to spawn with higher-tier skulls (White, Green, Yellow, Red, Black). Skulls act as modifiers that boost the monsters' power. By Wave 5, the chances of encountering Red and Black skull monsters are significantly higher.
- **Blink Warnings:** Before a monster spawns, the tile where it will appear blinks with a countdown (in seconds) and a skull effect, giving players time to prepare or reposition.
- **Time Limits:** There is a 5-minute timeout forcing the next wave if monsters are not cleared promptly, and a 1-hour overall timeout before the chest despawns entirely.

## 4. Rewards

If players successfully clear all 5 waves, the chest unlocks (indicated by a "gift wraps" effect and a "Chest Unlocked!" message). Players then have **60 seconds** to claim their rewards from inside the chest before it vanishes.

### Upgrade Orbs
Rewards always include a combination of upgrade orbs used in the Forge system. The amount dropped scales with the tier:
- **Special Orb, Ascension Orb, Fortification Orb, Highroller Orb:** Guaranteed drops.
- **Truesight Orb:** 10% chance to drop.

### Equipment, Power, and Rarity
- **Loot Pools:** Each tier has a specific loot pool including weapons, armors, gems, rings, and platinum coins. Legendary chests can drop top-tier items like Mastermind Shields, Golden Helmets, and Necrotic/Skullcrusher gear.
- **Rarity Rolls:** Equipment dropped from the chest automatically rolls for rarity. Higher tier chests have substantially better chances to roll Epic and Legendary rarities. For example, a Legendary chest has a 20% chance to drop a Legendary rarity item, whereas a Common chest only has a 1% chance.
- **Item Power & Base Tiers:** Dropped items gain a base **Power** score calculated from the average power of the monsters defeated in the event (including bonuses from monster skulls). The item's base **Tier** is also intrinsically linked to the chest's tier, with a small random chance for the item to upgrade itself even further upon dropping (up to Tier 4).

This system integrates tightly with Eternum's Forge and Rarity systems, making Cursed Chests a highly contested and rewarding activity for farming powerful base items.
