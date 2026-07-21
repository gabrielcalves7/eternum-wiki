# ✨ Guía de Hechizos Personalizados y No 7.4

Eternum utiliza el protocolo 7.72 pero amplía profundamente el sistema de combate incorporando mecánicas de Tibia moderno y hechizos completamente personalizados. A continuación se muestra una guía de los comportamientos de hechizos personalizados y hechizos no pertenecientes a la versión 7.4 que encontrarás en el servidor.

## 🛡️ Mecánicas de Provocación (Exeta Res)

En la versión 7.4 estándar, `exeta res` simplemente hacía que un monstruo cambiara de objetivo al Knight durante un breve momento. En Eternum, funciona de manera completamente diferente como una verdadera **mecánica de provocación (taunt)**:

{% hint style="info" %}
**Mecánicas de Provocación:**
- **Bloqueo de Agronomía (Aggro Lock):** Al lanzarlo (`exeta res`), afecta a un área de 3x3 alrededor del Knight. Cualquier monstruo provocable alcanzado queda **fijado al Knight durante 5 segundos**.
- **Sin Cambio de Objetivo:** Durante estos 5 segundos, la tendencia natural del monstruo a cambiar de objetivo se ignora por completo. No pueden cambiar de objetivo bajo ninguna circunstancia.
- **Sin Huidas:** Incluso si un monstruo alcanza la salud roja crítica (o es un Élite en huida), el bloqueo de 5 segundos lo obliga a quedarse y luchar.
{% endhint %}

## 🧪 Hechizos de Limpieza de Estados (Cleansing)

Eternum presenta muchos nuevos estados perjudiciales (como Bleeding, Freezing, Dazzled, Cursed y Drown). Para combatir esto, existen varios hechizos de limpieza personalizados:

### Purify (`exana omni`)
- **Vocación:** Todas las vocaciones (debe aprenderse explícitamente).
- **Efecto:** Un hechizo autolanzado que cura instantáneamente **todos** los estados perjudiciales de daño en el tiempo (DoT) a la vez (Poison, Fire, Energy, Bleeding, Freezing, Dazzled, Cursed, Drown).

### Mass Cleanse (`exana mas res`)
- **Vocación:** Druids.
- **Efecto:** Un hechizo de soporte en área (AoE) que afecta un área circular grande (radio 3) alrededor del lanzador. Cura simultáneamente a los aliados y aplica el efecto `Purify`, limpiando todos los estados negativos de DoT de cada jugador alcanzado.

### Curas Específicas
- **Discharge (`exana vis`):** Cura instantáneamente el estado de Energía (electrificado).
- **Extinguish (`exana flam`):** Cura instantáneamente el estado de Fuego (quemadura).

## ⚔️ Hechizos Modernos en un Cliente Retro

Para proporcionar una experiencia de combate más dinámica, Eternum incluye muchos hechizos que normalmente se encuentran en las versiones 8.0+:

### Hechizos de Knight
| Hechizo | Palabras | Descripción |
| --- | --- | --- |
| **Fierce Berserk** | `exori gran` | Una versión significativamente más fuerte de Berserk que inflige un gran daño físico en un área de 3x3. |
| **Groundshaker** | `exori mas` | Un ataque físico en área aún mayor que alcanza un área circular grande (radio 3) alrededor del Knight. |
| **Whirlwind Throw** | `exori hur` | Permite a los Knights atacar a distancia lanzando su arma (alcance de 3 casillas). |

### Hechizos de Paladin
| Hechizo | Palabras | Descripción |
| --- | --- | --- |
| **Ethereal Spear** | `exori con` | Un hechizo de ataque físico a distancia a un solo objetivo que escala con la habilidad Distance y el Nivel. |
| **Divine Healing** | `exura san` | Una curación rápida y altamente eficiente diseñada específicamente para Paladins. |
| **Holy Strike** | `exori san` | Un ataque de daño sagrado a un solo objetivo. |
| **Divine Caldera** | `exevo mas san` | Una explosión en área de daño sagrado en una zona circular grande (radio 3) alrededor del Paladin. |

### Impactos Elementales de Magos (Elemental Strikes)
Los magos tienen acceso a toda la suite de impactos modernos a un solo objetivo con tiempos de reutilización (cooldowns) muy bajos, lo que les permite intercalar hechizos entre ataques de runas:

| Categoría | Palabras | Descripción |
| --- | --- | --- |
| **Impactos Normales** | `exori flam`, `exori vis`, `exori frigo`, `exori tera`, `exori mort` | Impactos elementales a un solo objetivo con cooldowns bajos. |
| **Grandes Impactos** | `exori gran flam`, `exori gran vis`, `exori gran frigo` | Se expanden a un área de 3x3 alrededor del objetivo con un costo de mana mayor, infligiendo el mismo daño que los impactos normales. |
| **Strong Ice Wave** | `exevo gran frigo hur` | Una potente ola de hielo direccional específica para Druids. |

## 🔄 Hechizos y Runas Retro Modificados

Varias runas y hechizos clásicos han visto ajustados sus tipos de daño para adaptarse mejor a las mecánicas personalizadas:

| Hechizo / Runa | Palabras | Tipo de Daño / Cambio de Comportamiento |
| --- | --- | --- |
| **Sudden Death Rune (SD)** | `adori vita vis` | Inflige daño de **Muerte (Death)** (en lugar de daño físico en 7.4 estándar). |
| **Ultimate Explosion** | `exevo gran mas vis` | Inflige daño **Físico (Physical)**. |
| **Poison Storm** | `exevo gran mas pox` | Inflige daño **Físico (Physical)**. |
