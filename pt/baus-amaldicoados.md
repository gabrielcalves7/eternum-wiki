# Baús Amaldiçoados (Cursed Chests)

O sistema de **Baús Amaldiçoados** é um evento customizado onde baús especiais aparecem aleatoriamente no mundo, ao redor das principais cidades. Jogadores podem abrir esses baús para iniciar um evento de combate em múltiplas ondas. Se completado com sucesso, o baú concede recompensas poderosas, incluindo itens com atributos de raridade e diversos orbes de upgrade.

## 1. Tiers e Requisitos

Os Baús Amaldiçoados aparecem em quatro tiers (níveis) distintos, que determinam o nível mínimo para abri-los, a dificuldade dos monstros evocados e a qualidade dos prêmios.

| Tier | Tipo de Baú | Nível Mín. | Chance de Aparecer | Monstros por Onda |
| :--- | :--- | :--- | :--- | :--- |
| 1 | Comum | 20 | 70% | 3 |
| 2 | Raro | 40 | 50% | 3 |
| 3 | Épico | 60 | 30% | 4 |
| 4 | Lendário | 90 | 10% | 4 |

## 2. Mecânicas de Spawn

- **Intervalo:** Novos baús tentam aparecer a cada hora (60 minutos).
- **Localizações:** Os baús nascem num raio de 500 tiles em torno dos templos das principais cidades (Ankrahmun, Darashia, Thais, Carlin, Edron, Venore, Ab'Dendriel, Yalahar, Svargrond).
- **Restrições de Distância:** Baús não nascerão mais perto que 100 tiles de um templo e são espaçados em no mínimo 15 tiles de outros baús ativos.
- **Capacidade:** O servidor cria até 6 baús globalmente por ciclo.
- **Visuais:** Enquanto ociosos, os baús emitem um efeito de "morcegos" e exibem um texto flutuante com seu tier (ex: "Legendary Cursed Chest").

## 3. O Evento (Ondas e Combate)

Abrir um baú inicia o evento. O jogador (e quem mais estiver perto) deverá derrotar **5 ondas** de monstros.

- **Seleção de Monstros:** Os monstros são escolhidos dinamicamente da lista de tarefas diárias (daily tasks), baseando-se no tier do baú. O poder dos monstros escala progressivamente da onda 1 até a 5.
- **Caveiras e Dificuldade (Skulls):** Monstros têm chances crescentes de nascer com caveiras de nível maior (White, Green, Yellow, Red, Black). Caveiras funcionam como modificadores de poder. Na onda 5, a chance de encontrar monstros Red e Black skull é significativamente maior.
- **Aviso (Blink):** Antes de um monstro nascer, o tile em que ele vai aparecer pisca com uma contagem regressiva em segundos e o efeito da caveira, dando tempo de o jogador se preparar ou reposicionar.
- **Limites de Tempo:** Existe um tempo limite de 5 minutos, que força a próxima onda se a atual não for limpa rapidamente, e um limite de 1 hora no geral, caso contrário o baú desaparece completamente.

## 4. Recompensas

Se os jogadores vencerem as 5 ondas, o baú é desbloqueado (indicado por um efeito de embrulho de presente e a mensagem "Chest Unlocked!"). Você terá então **60 segundos** para pegar as recompensas dentro dele, antes que desapareça.

Aqueles que concluírem com sucesso o desafio dos Baús Amaldiçoados receberão ótimas recompensas, que incluem equipamentos poderosos e diversas orbes de upgrade usadas no sistema de Forja. A qualidade e raridade das recompensas escalam diretamente com o tier do baú derrotado.
