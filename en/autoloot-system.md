# Autoloot System

## Overview
The Autoloot System allows players to automatically loot specific items from monster corpses. It's designed for convenience, letting you manage your loot list seamlessly.

## Features & Mechanics

### Basic Autoloot
- **Base Capacity:** You start with **8 slots** for items in your autoloot list.
- **Mechanic:** When you open a monster's corpse, the system automatically extracts items matching your list and places them into your inventory.

### Loot Without Click
- **Mechanic:** Players can unlock the "Loot Without Click" ability using a specific item.
- Once unlocked, items on your list are looted straight to your inventory the moment the monster dies, eliminating the need to physically interact with the corpse.

### Bank Coins (Midas Permit)
- **Mechanic:** Consuming a Midas Permit permanently grants access to the Bank Coins feature. You can toggle this feature on or off.
- When active, any looted gold, platinum, or crystal coins bypass your inventory entirely and are deposited directly into your bank balance.

### Capacity Expansion
- **Mechanic:** Players can permanently increase their maximum autoloot slots by using a specific expansion item.

## Player Commands
You can manage your autoloot configuration using the `!autoloot` chat command. You can use item names directly.

- `!autoloot add, <name>`: Adds an item to the autoloot list.
- `!autoloot remove, <name>`: Removes an item from the list.
- `!autoloot show`: Displays all items currently in the autoloot list.
- `!autoloot clear`: Empties the autoloot list completely.
- `!autoloot bankcoins`: Toggles the automatic banking of coins (requires the Midas Permit).

*Note: The command supports both comma-separated (`!autoloot add, gold coin`) and space-separated (`!autoloot add gold coin`) syntax.*

## Container Mappings (Categorized Loot)
You can organize your drops by routing specific categories of items into designated containers (like specific backpacks) within your inventory via the client interface.

**Available Categories:**
- Equipment
- Valuables
- Potions
- Runes
- Miscellaneous
- Gold
- Ammo
- Default
