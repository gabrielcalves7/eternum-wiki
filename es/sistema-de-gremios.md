# 🏛️ Sistema de Gremios

Los gremios suben de nivel con oro. Los miembros donan a un **tesoro** común, y el liderazgo lo gasta en niveles de gremio — que otorgan plazas de miembro — y en cinco **bonificaciones** de gremio que se aplican a todos los miembros conectados mientras estén activas.

{% hint style="info" %}
Fundar un gremio no cuesta oro, pero tu personaje debe ser al menos de **nivel 50**. Puedes crearlo directamente desde la ventana de Gremio en el cliente.
{% endhint %}

## 💰 El Tesoro

- **Cualquier miembro puede donar.** La donación mínima es de **1,000 de oro**, tomada de tu inventario y de tu banco en conjunto.
- **Solo el líder y los vicelíderes pueden gastarlo** — en niveles de gremio y en bonificaciones.
- Cada donación se registra por personaje, así el gremio ve quién lo ha financiado.
- **Las donaciones no se devuelven nunca.** El oro que entra al tesoro se queda allí.

## 📈 Niveles de Gremio y Plazas de Miembro

Un gremio va del nivel 1 al **nivel 100**. Los niveles se cuentan en tramos de diez, y cada tramo otorga **5 plazas más** y un escalón más de cada bonificación desbloqueada.

| Nivel de gremio | 1 | 10 | 20 | 30 | 40 | 50 | 60 | 70 | 80 | 90 | 100 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Plazas de miembro | 10 | 15 | 20 | 25 | 30 | 35 | 40 | 45 | 50 | 55 | 60 |

## ✨ Las Cinco Bonificaciones

Cada bonificación se desbloquea con un nivel de gremio y crece con él. Una bonificación siempre corre al **máximo que permite tu nivel de gremio** — el oro compra tiempo, no potencia.

| Bonificación | Efecto | Se desbloquea en | Valor al desbloquear | Máximo (nivel 100) |
|---|---|---|---|---|
| **Magic Level** | El magic level sube más rápido | 5 | +2% | +15% |
| **Skills** | Las skills de arma y shielding suben más rápido | 10 | +2% | +15% |
| **Experience** | Más experiencia por muerte | 15 | +2% | +15% |
| **Elite Monster Chance** | Más probabilidad de que los monstruos aparezcan como Elite | 20 | +2% | +7.5% |
| **Loot** | Más loot de los monstruos | 25 | +4% | +15% |

## 📊 Bonificación por Nivel de Gremio

Hasta el nivel 50 cada tramo suma **+2%** (**+1%** para Probabilidad de Monstruo Elite). A partir de 50 la curva sigue a la mitad, **+1%** por tramo (**+0.5%** para Elite), hasta el máximo en el nivel 100.

| Nivel de gremio | Magic Level | Skills | Experience | Elite Monster Chance | Loot |
|---|---|---|---|---|---|
| **5** | +2% | — | — | — | — |
| **10** | +2% | +2% | — | — | — |
| **15** | +2% | +2% | +2% | — | — |
| **20** | +4% | +4% | +4% | +2% | — |
| **25** | +4% | +4% | +4% | +2% | +4% |
| **30** | +6% | +6% | +6% | +3% | +6% |
| **35** | +6% | +6% | +6% | +3% | +6% |
| **40** | +8% | +8% | +8% | +4% | +8% |
| **45** | +8% | +8% | +8% | +4% | +8% |
| **50** | +10% | +10% | +10% | +5% | +10% |
| **55** | +10% | +10% | +10% | +5% | +10% |
| **60** | +11% | +11% | +11% | +5.5% | +11% |
| **65** | +11% | +11% | +11% | +5.5% | +11% |
| **70** | +12% | +12% | +12% | +6% | +12% |
| **75** | +12% | +12% | +12% | +6% | +12% |
| **80** | +13% | +13% | +13% | +6.5% | +13% |
| **85** | +13% | +13% | +13% | +6.5% | +13% |
| **90** | +14% | +14% | +14% | +7% | +14% |
| **95** | +14% | +14% | +14% | +7% | +14% |
| **100** | +15% | +15% | +15% | +7.5% | +15% |

## 🪙 Precio de las Bonificaciones

- Se venden en **bloques de 15 minutos**. Un gremio puede acumular hasta **120 minutos** de una misma bonificación.
- El precio depende del **nivel del gremio y del número de miembros**: un gremio más grande y más alto paga más por el mismo bloque.
- **Cada compra de esa bonificación en el día cuesta ×1.5 la anterior.** El contador se reinicia a las **6:00 hora del servidor**.

**La fórmula** — `bloque = coste base × miembros × (1 + nivel de gremio / 20) / 4`, multiplicado por `1.5` por cada bloque de esa bonificación ya comprado hoy.

### Coste **por miembro**: primer bloque de 15 min / primera hora completa

Una hora son cuatro bloques, y el aumento ya se aplica dentro de ella, así que la hora cuesta **8.125×** un bloque, no cuatro veces. Multiplica por tu número de miembros.

| Nivel de gremio | Magic Level | Skills | Experience | Elite Monster Chance | Loot |
|---|---|---|---|---|---|
| **5** | 1,562 / 12,693 | — | — | — | — |
| **10** | 1,875 / 15,233 | 1,875 / 15,233 | — | — | — |
| **15** | 2,187 / 17,771 | 2,187 / 17,771 | 3,281 / 26,658 | — | — |
| **20** | 2,500 / 20,312 | 2,500 / 20,312 | 3,750 / 30,468 | 5,000 / 40,625 | — |
| **25** | 2,812 / 22,850 | 2,812 / 22,850 | 4,218 / 34,276 | 5,625 / 45,702 | 4,218 / 34,276 |
| **30** | 3,125 / 25,389 | 3,125 / 25,389 | 4,687 / 38,084 | 6,250 / 50,780 | 4,687 / 38,084 |
| **40** | 3,750 / 30,468 | 3,750 / 30,468 | 5,625 / 45,702 | 7,500 / 60,937 | 5,625 / 45,702 |
| **50** | 4,375 / 35,545 | 4,375 / 35,545 | 6,562 / 53,318 | 8,750 / 71,093 | 6,562 / 53,318 |
| **60** | 5,000 / 40,625 | 5,000 / 40,625 | 7,500 / 60,937 | 10,000 / 81,250 | 7,500 / 60,937 |
| **70** | 5,625 / 45,702 | 5,625 / 45,702 | 8,437 / 68,553 | 11,250 / 91,405 | 8,437 / 68,553 |
| **80** | 6,250 / 50,780 | 6,250 / 50,780 | 9,375 / 76,170 | 12,500 / 101,562 | 9,375 / 76,170 |
| **90** | 6,875 / 55,858 | 6,875 / 55,858 | 10,312 / 83,787 | 13,750 / 111,718 | 10,312 / 83,787 |
| **100** | 7,500 / 60,937 | 7,500 / 60,937 | 11,250 / 91,405 | 15,000 / 121,875 | 11,250 / 91,405 |

### Ejemplo: gremio de 20 miembros

El precio real que paga un gremio de 20 miembros, en su primera compra del día.

| Nivel de gremio | Magic Level | Skills | Experience | Elite Monster Chance | Loot |
|---|---|---|---|---|---|
| **25** | 56,250 / 457,030 | 56,250 / 457,030 | 84,375 / 685,545 | 112,500 / 914,062 | 84,375 / 685,545 |
| **50** | 87,500 / 710,937 | 87,500 / 710,937 | 131,250 / 1,066,405 | 175,000 / 1,421,875 | 131,250 / 1,066,405 |
| **75** | 118,750 / 964,843 | 118,750 / 964,843 | 178,125 / 1,447,264 | 237,500 / 1,929,687 | 178,125 / 1,447,264 |
| **100** | 150,000 / 1,218,750 | 150,000 / 1,218,750 | 225,000 / 1,828,125 | 300,000 / 2,437,500 | 225,000 / 1,828,125 |

| Bloques comprados hoy | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|---|---|---|---|---|---|---|---|---|
| Multiplicador de precio | ×1 | ×1.5 | ×2.25 | ×3.38 | ×5.06 | ×7.59 | ×11.39 | ×17.09 |

{% hint style="warning" %}
Llenar los 120 minutos en un solo día cuesta por tanto **49.26×** un bloque — a propósito, mucho más que 8 veces.
{% endhint %}

## 🏦 Oro Necesario para Cada Nivel de Gremio

Coste del siguiente nivel y el total acumulado desde el nivel 1.

| Nivel | Coste del siguiente nivel | Total desde el nivel 1 |
|---|---|---|
| 1 → 2 | 10,000 | 10,000 |
| 2 → 3 | 22,973 | 32,973 |
| 3 → 4 | 37,371 | 70,344 |
| 4 → 5 | 52,780 | 123,124 |
| 5 → 6 | 68,986 | 192,110 |
| 6 → 7 | 85,858 | 277,968 |
| 7 → 8 | 103,304 | 381,272 |
| 8 → 9 | 121,257 | 502,529 |
| 9 → 10 | 139,666 | 642,195 |
| 10 → 11 | 158,489 | 800,684 |
| 11 → 12 | 177,693 | 978,377 |
| 12 → 13 | 197,250 | 1,175,627 |
| 13 → 14 | 217,136 | 1,392,763 |
| 14 → 15 | 237,330 | 1,630,093 |
| 15 → 16 | 257,815 | 1,887,908 |
| 16 → 17 | 278,576 | 2,166,484 |
| 17 → 18 | 299,597 | 2,466,081 |
| 18 → 19 | 320,868 | 2,786,949 |
| 19 → 20 | 342,376 | 3,129,325 |
| 20 → 21 | 364,112 | 3,493,437 |
| 21 → 22 | 386,067 | 3,879,504 |
| 22 → 23 | 408,232 | 4,287,736 |
| 23 → 24 | 430,599 | 4,718,335 |
| 24 → 25 | 453,162 | 5,171,497 |
| 25 → 26 | 475,913 | 5,647,410 |

| Nivel | Coste del siguiente nivel | Total desde el nivel 1 |
|---|---|---|
| 26 → 27 | 498,847 | 6,146,257 |
| 27 → 28 | 521,959 | 6,668,216 |
| 28 → 29 | 545,242 | 7,213,458 |
| 29 → 30 | 568,692 | 7,782,150 |
| 30 → 31 | 592,305 | 8,374,455 |
| 31 → 32 | 616,075 | 8,990,530 |
| 32 → 33 | 639,999 | 9,630,529 |
| 33 → 34 | 664,074 | 10,294,603 |
| 34 → 35 | 688,295 | 10,982,898 |
| 35 → 36 | 712,658 | 11,695,556 |
| 36 → 37 | 737,162 | 12,432,718 |
| 37 → 38 | 761,801 | 13,194,519 |
| 38 → 39 | 786,575 | 13,981,094 |
| 39 → 40 | 811,479 | 14,792,573 |
| 40 → 41 | 836,511 | 15,629,084 |
| 41 → 42 | 861,669 | 16,490,753 |
| 42 → 43 | 886,950 | 17,377,703 |
| 43 → 44 | 912,351 | 18,290,054 |
| 44 → 45 | 937,871 | 19,227,925 |
| 45 → 46 | 963,507 | 20,191,432 |
| 46 → 47 | 989,257 | 21,180,689 |
| 47 → 48 | 1,015,120 | 22,195,809 |
| 48 → 49 | 1,041,092 | 23,236,901 |
| 49 → 50 | 1,067,174 | 24,304,075 |
| 50 → 51 | 1,093,362 | 25,397,437 |

| Nivel | Coste del siguiente nivel | Total desde el nivel 1 |
|---|---|---|
| 51 → 52 | 1,119,654 | 26,517,091 |
| 52 → 53 | 1,146,051 | 27,663,142 |
| 53 → 54 | 1,172,549 | 28,835,691 |
| 54 → 55 | 1,199,147 | 30,034,838 |
| 55 → 56 | 1,225,844 | 31,260,682 |
| 56 → 57 | 1,252,638 | 32,513,320 |
| 57 → 58 | 1,279,528 | 33,792,848 |
| 58 → 59 | 1,306,512 | 35,099,360 |
| 59 → 60 | 1,333,590 | 36,432,950 |
| 60 → 61 | 1,360,759 | 37,793,709 |
| 61 → 62 | 1,388,020 | 39,181,729 |
| 62 → 63 | 1,415,370 | 40,597,099 |
| 63 → 64 | 1,442,808 | 42,039,907 |
| 64 → 65 | 1,470,333 | 43,510,240 |
| 65 → 66 | 1,497,945 | 45,008,185 |
| 66 → 67 | 1,525,642 | 46,533,827 |
| 67 → 68 | 1,553,423 | 48,087,250 |
| 68 → 69 | 1,581,286 | 49,668,536 |
| 69 → 70 | 1,609,232 | 51,277,768 |
| 70 → 71 | 1,637,259 | 52,915,027 |
| 71 → 72 | 1,665,367 | 54,580,394 |
| 72 → 73 | 1,693,553 | 56,273,947 |
| 73 → 74 | 1,721,818 | 57,995,765 |
| 74 → 75 | 1,750,161 | 59,745,926 |
| 75 → 76 | 1,778,580 | 61,524,506 |

| Nivel | Coste del siguiente nivel | Total desde el nivel 1 |
|---|---|---|
| 76 → 77 | 1,807,075 | 63,331,581 |
| 77 → 78 | 1,835,645 | 65,167,226 |
| 78 → 79 | 1,864,290 | 67,031,516 |
| 79 → 80 | 1,893,008 | 68,924,524 |
| 80 → 81 | 1,921,799 | 70,846,323 |
| 81 → 82 | 1,950,661 | 72,796,984 |
| 82 → 83 | 1,979,596 | 74,776,580 |
| 83 → 84 | 2,008,601 | 76,785,181 |
| 84 → 85 | 2,037,676 | 78,822,857 |
| 85 → 86 | 2,066,820 | 80,889,677 |
| 86 → 87 | 2,096,033 | 82,985,710 |
| 87 → 88 | 2,125,314 | 85,111,024 |
| 88 → 89 | 2,154,662 | 87,265,686 |
| 89 → 90 | 2,184,077 | 89,449,763 |
| 90 → 91 | 2,213,558 | 91,663,321 |
| 91 → 92 | 2,243,105 | 93,906,426 |
| 92 → 93 | 2,272,717 | 96,179,143 |
| 93 → 94 | 2,302,393 | 98,481,536 |
| 94 → 95 | 2,332,133 | 100,813,669 |
| 95 → 96 | 2,361,937 | 103,175,606 |
| 96 → 97 | 2,391,803 | 105,567,409 |
| 97 → 98 | 2,421,732 | 107,989,141 |
| 98 → 99 | 2,451,722 | 110,440,863 |
| 99 → 100 | 2,481,774 | 112,922,637 |

{% hint style="success" %}
Llegar al nivel 50 — donde está el primer tope — cuesta **24,304,075 de oro**, y maximizar el gremio en el nivel 100 cuesta **112,922,637 de oro** en total.
{% endhint %}
