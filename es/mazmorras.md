# 🏰 Sistema de Mazmorras

¡Desafía a poderosos jefes y gana recompensas exclusivas!

![](../assets/wiki/dungeon.png)

## 🚪 Cómo Entrar

Accede a la **Interfaz de Mazmorras** haciendo clic en el botón dentro del **Menú del Cliente**.

- **Entradas Diarias:** Recibes **2 Entradas Gratuitas** en cada guardado del servidor (server save).
- **Tamaño del Equipo:** Se puede realizar en solitario o en un equipo de hasta 4 jugadores.

## 🎁 Recompensas

Las mazmorras son una fuente de:
- **Monedas de Cristal (Crystal Coins)** y botín valioso.
- **Objetos Exclusivos** soltados por los Jefes de Mazmorra.

---

## Sistema de Recompensas de Jefes Diarios
Las recompensas de bonificación para los jefes diarios (que probablemente sean monedas o fichas adicionales) se otorgan dinámicamente en función del número de jugadores dentro de la sala del jefe y el nivel de dificultad elegido (calavera).

### Recompensas Base (Por Número de Jugadores)
- **1 Jugador (Solo):** 0 monedas de bonificación
- **2 Jugadores (Dúo):** 1 moneda de bonificación
- **3 Jugadores (Trío):** 2 monedas de bonificación
- **4 Jugadores (Grupo Completo):** 3 monedas de bonificación

### Bonificación de Dificultad
Si el nivel de dificultad seleccionado es **3 o superior** (Calavera Amarilla, Calavera Roja o Calavera Negra), se otorga **+1 moneda de bonificación** adicional a todos en el grupo.

*Nota: Estas monedas de bonificación se entregan directamente en la mochila de cada jugador inmediatamente después de que muere el jefe, justo antes de ser teletransportados a la sala de cofres de recompensa.*

---

## Escalado de Dificultad de Mazmorras
Las mazmorras cuentan con un sistema de escalado basado en la dificultad elegida por el jugador (Normal, Hard, Expert, Master, Torment, Hell). La dificultad cambia varios aspectos de la mazmorra, desde la fuerza de los monstruos hasta la calidad de las recompensas.

Aquí están los multiplicadores exactos que cambian según la dificultad elegida:

| Dificultad | Nombre  | HP del Monstruo | Daño del Monstruo | Bonificación de XP | Bonificación de Oro | Probabilidad de Botín | Poder del Objeto |
| :---       | :---    | :---            | :---              | :---               | :---                | :---                  | :---             |
| 1          | Normal  | 1.0x            | 1.0x              | 1.0x               | 1.0x                | 1.0x                  | 1.0x             |
| 2          | Hard    | 2.0x            | 1.3x              | 1.75x              | 1.75x               | 1.0x                  | 1.10x            |
| 3          | Expert  | 3.2x            | 1.9x              | 2.0x               | 2.0x                | 1.15x                 | 1.15x            |
| 4          | Master  | 5.0x            | 2.8x              | 3.0x               | 3.0x                | 1.30x                 | 1.20x            |
| 5          | Torment | 8.0x            | 4.0x              | 4.0x               | 4.0x                | 1.45x                 | 1.30x            |
| 6          | Hell    | 13.0x           | 6.0x              | 5.0x               | 5.0x                | 1.60x                 | 1.40x            |

### Detalles de las Recompensas
Al completar una mazmorra, se generan objetos de bonificación adicionales. La dificultad afecta estos objetos de recompensa de las siguientes maneras:

1. **Probabilidad de Botín**: Las dificultades más altas mejoran la probabilidad base de recibir objetos de recompensa de bonificación.
2. **Poder del Objeto**: Las dificultades más altas aumentan el poder de los objetos de las recompensas.
3. **Rareza del Objeto**: La probabilidad de que un objeto obtenga niveles de rareza más altos (hasta el nivel 4) mejora drásticamente con dificultades más altas.
