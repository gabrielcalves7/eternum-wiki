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

Those who successfully accomplish the Cursed Chests challenge are granted great rewards, which include powerful equipment and various upgrade orbs used in the Forge system. The quality and rarity of the rewards scale directly with the tier of the chest you defeat.
