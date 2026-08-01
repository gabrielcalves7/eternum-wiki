# 🏰 Sistema de Masmorras (Dungeons)

Desafie chefes poderosos e ganhe recompensas exclusivas!

![](../assets/wiki/dungeon.png)

## 🚪 Como Entrar

Acesse a **Interface da Masmorra** clicando no botão no **Menu do Client**.

- **Entradas Diárias:** Você recebe **2 Entradas Gratuitas** a cada server save.
- **Tamanho da Equipe:** Pode ser feito solo ou em equipe de até 4 jogadores.

## 🎁 Recompensas

Masmorras são fonte de:
- **Crystal Coins** e itens valiosos (loot).
- **Itens Exclusivos** derrubados pelos Chefes da Masmorra.

---

## Sistema de Recompensas de Bosses Diários
As recompensas bônus para os bosses diários (que provavelmente são moedas ou tokens extras) são dadas dinamicamente com base no número de jogadores dentro da sala do boss e no nível de dificuldade escolhido (caveira).

### Recompensas Base (Por Número de Jogadores)
- **1 Jogador (Solo):** 0 moedas bônus
- **2 Jogadores (Duo):** 1 moeda bônus
- **3 Jogadores (Trio):** 2 moedas bônus
- **4 Jogadores (Grupo Completo):** 3 moedas bônus

### Bônus de Dificuldade
Se o nível de dificuldade selecionado for **3 ou superior** (Caveira Amarela, Caveira Vermelha ou Caveira Preta), **+1 moeda bônus** adicional é concedida a todos no grupo.

*Nota: Estas moedas bônus são entregues diretamente na mochila de cada jogador imediatamente após a morte do boss, logo antes de serem teleportados para a sala dos baús de recompensa.*

---

## Escalonamento de Dificuldade da Masmorra
As masmorras apresentam um sistema de escalonamento baseado na dificuldade escolhida pelo jogador (Normal, Hard, Expert, Master, Torment, Hell). A dificuldade altera vários aspectos da masmorra, desde a força dos monstros até a qualidade das recompensas.

Aqui estão os multiplicadores exatos que mudam de acordo com a dificuldade escolhida:

| Dificuldade | Nome    | HP do Monstro | Dano do Monstro | Bônus de XP | Bônus de Ouro | Chance de Loot | Poder do Item |
| :---        | :---    | :---          | :---            | :---        | :---          | :---           | :---          |
| 1           | Normal  | 1.0x          | 1.0x            | 1.0x        | 1.0x          | 1.0x           | 1.0x          |
| 2           | Hard    | 2.0x          | 1.3x            | 1.75x       | 1.75x         | 1.0x           | 1.10x         |
| 3           | Expert  | 3.2x          | 1.9x            | 2.0x        | 2.0x          | 1.15x          | 1.15x         |
| 4           | Master  | 5.0x          | 2.8x            | 3.0x        | 3.0x          | 1.30x          | 1.20x         |
| 5           | Torment | 8.0x          | 4.0x            | 4.0x        | 4.0x          | 1.45x          | 1.30x         |
| 6           | Hell    | 13.0x         | 6.0x            | 5.0x        | 5.0x          | 1.60x          | 1.40x         |

### Detalhes das Recompensas
Ao completar uma masmorra, itens bônus extras são rolados. A dificuldade afeta esses itens de recompensa das seguintes maneiras:

1. **Chance de Loot**: Dificuldades mais altas melhoram a chance base de receber itens de recompensa bônus.
2. **Poder do Item**: Dificuldades mais altas aumentam o poder do item das recompensas.
3. **Raridade do Item**: A chance de um item rolar níveis de raridade mais altos (até o grau 4) melhora drasticamente com dificuldades mais altas.
