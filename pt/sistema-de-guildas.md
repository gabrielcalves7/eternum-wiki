# 🏛️ Sistema de Guildas

Guildas sobem de nível com ouro. Os membros doam para um **tesouro** compartilhado, e a liderança o gasta em níveis de guilda, em **vagas de membro** e em cinco **bônus** de guilda que valem para todos os membros online enquanto estiverem ativos.

{% hint style="info" %}
Fundar uma guilda não custa ouro, mas seu personagem precisa ter no mínimo **nível 50**. Você pode criá-la direto pela janela de Guilda no cliente.
{% endhint %}

## 💰 O Tesouro

- **Qualquer membro pode doar.** A doação mínima é de **1,000 de ouro**, retirada do seu inventário e do seu banco somados.
- **Somente o líder e os vice-líderes podem gastar** — em níveis de guilda e em bônus.
- Cada doação é registrada por personagem, então a guilda vê quem a financiou.
- **Doações nunca são devolvidas.** Ouro que entra no tesouro fica lá.

## 📈 Níveis de Guilda

Uma guilda vai do nível 1 ao **nível 100**. Os níveis são contados em faixas de dez, e cada faixa adiciona mais um degrau a cada bônus desbloqueado e eleva o teto de quantas vagas de membro a guilda pode comprar.

| Nível da guilda | 1 | 10 | 20 | 30 | 40 | 50 | 60 | 70 | 80 | 90 | 100 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Teto de vagas | 5 | 10 | 15 | 20 | 25 | 30 | 35 | 40 | 45 | 50 | 55 |

## 👥 Vagas de Membro

Uma guilda é fundada com **5 membros** e compra cada vaga adicional do tesouro. O nível da guilda não dá vagas; ele apenas define o teto, então é preciso ter o nível e o ouro. Cada vaga custa mais que a anterior, e o preço nunca zera.

| Vaga | Custa | Total gasto em vagas | Exige nível de guilda |
|---|---|---|---|
| **6** | 50,000 | 50,000 | 10 |
| **10** | 73,205 | 305,255 | 10 |
| **15** | 117,897 | 796,869 | 20 |
| **20** | 189,874 | 1,588,619 | 30 |
| **25** | 305,795 | 2,863,742 | 40 |
| **30** | 492,486 | 4,917,342 | 50 |
| **35** | 793,154 | 8,224,687 | 60 |
| **40** | 1,277,383 | 13,551,202 | 70 |
| **45** | 2,057,238 | 22,129,609 | 80 |
| **50** | 3,313,203 | 35,945,220 | 90 |
| **55** | 5,335,947 | 58,195,402 | 100 |

## ✨ Os Cinco Bônus

Cada bônus é desbloqueado por um nível de guilda e cresce junto com ele. Um bônus sempre roda no **valor máximo que o nível da sua guilda permite** — o ouro compra tempo, não força.

| Bônus | Efeito | Desbloqueia no | Valor ao desbloquear | Máximo (nível 100) |
|---|---|---|---|---|
| **Magic Level** | Magic level sobe mais rápido | 5 | +2% | +15% |
| **Skills** | Skills de arma e shielding sobem mais rápido | 10 | +2% | +15% |
| **Experience** | Mais experiência por abate | 15 | +2% | +15% |
| **Elite Monster Chance** | Mais chance de monstros nascerem Elite | 20 | +2% | +7.5% |
| **Loot** | Mais loot dos monstros | 25 | +4% | +15% |

## 📊 Bônus por Nível de Guilda

Até o nível 50 cada faixa soma **+2%** (**+1%** para Chance de Monstro Elite). Depois do 50 a curva continua pela metade, **+1%** por faixa (**+0.5%** para Elite), até o máximo no nível 100.

| Nível da guilda | Magic Level | Skills | Experience | Elite Monster Chance | Loot |
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

## 🪙 Preço dos Bônus

- Os bônus são vendidos em **blocos de 15 minutos**. Uma guilda pode acumular até **120 minutos** de um mesmo bônus.
- O preço depende do **nível da guilda e da quantidade de membros**: uma guilda maior e mais alta paga mais pelo mesmo bloco.
- **Cada compra daquele bônus no dia custa ×1.5 a anterior.** O contador zera às **6:00 do horário do servidor**.

### Custo **por membro**: primeiro bloco de 15 min / primeira hora cheia

Uma hora são quatro blocos, e o aumento já vale dentro dela, então a hora custa **8.125×** um bloco, e não quatro vezes. Multiplique pelo número de membros.

| Nível da guilda | Magic Level | Skills | Experience | Elite Monster Chance | Loot |
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

### Exemplo: guilda com 20 membros

O preço real que uma guilda de 20 membros paga, na primeira compra do dia.

| Nível da guilda | Magic Level | Skills | Experience | Elite Monster Chance | Loot |
|---|---|---|---|---|---|
| **25** | 56,250 / 457,030 | 56,250 / 457,030 | 84,375 / 685,545 | 112,500 / 914,062 | 84,375 / 685,545 |
| **50** | 87,500 / 710,937 | 87,500 / 710,937 | 131,250 / 1,066,405 | 175,000 / 1,421,875 | 131,250 / 1,066,405 |
| **75** | 118,750 / 964,843 | 118,750 / 964,843 | 178,125 / 1,447,264 | 237,500 / 1,929,687 | 178,125 / 1,447,264 |
| **100** | 150,000 / 1,218,750 | 150,000 / 1,218,750 | 225,000 / 1,828,125 | 300,000 / 2,437,500 | 225,000 / 1,828,125 |

| Blocos comprados hoje | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|---|---|---|---|---|---|---|---|---|
| Multiplicador de preço | ×1 | ×1.5 | ×2.25 | ×3.38 | ×5.06 | ×7.59 | ×11.39 | ×17.09 |

{% hint style="warning" %}
Encher os 120 minutos em um único dia custa, portanto, **49.26×** um bloco — de propósito, muito mais do que 8 vezes.
{% endhint %}

## 🏦 Ouro Necessário para Cada Nível de Guilda

Custo do próximo nível e o total acumulado desde o nível 1.

| Nível | Custo do próximo nível | Total desde o nível 1 |
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

| Nível | Custo do próximo nível | Total desde o nível 1 |
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

| Nível | Custo do próximo nível | Total desde o nível 1 |
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

| Nível | Custo do próximo nível | Total desde o nível 1 |
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
Chegar ao nível 50 — onde o primeiro teto acontece — custa **24,304,075 de ouro**, e maximizar a guilda no nível 100 custa **112,922,637 de ouro** no total.
{% endhint %}
