# Sistema de Autoloot

## Visão Geral
O Sistema de Autoloot permite que os jogadores coletem automaticamente itens específicos dos corpos dos monstros. Foi criado para trazer conveniência, permitindo gerenciar sua lista de coleta de forma simples.

## Funcionalidades e Mecânicas

### Autoloot Básico
- **Capacidade Inicial:** Você começa com **8 espaços** para itens na sua lista de autoloot.
- **Mecânica:** Ao abrir o corpo de um monstro, o sistema extrai automaticamente os itens que estão na sua lista e os coloca no seu inventário.

### Loot Sem Clique
- **Mecânica:** Os jogadores podem desbloquear a habilidade "Loot Sem Clique" (Loot Without Click) usando um item específico.
- Uma vez desbloqueada, os itens da sua lista são coletados direto para o seu inventário no momento em que o monstro morre, eliminando a necessidade de interagir fisicamente com o corpo.

### Moedas para o Banco (Midas Permit)
- **Mecânica:** Usar um Midas Permit concede acesso permanente à função de envio de moedas para o banco. Você pode ativar ou desativar essa função.
- Quando ativa, qualquer gold, platinum ou crystal coin coletada ignora o seu inventário e é depositada diretamente no saldo do seu banco.

### Expansão de Capacidade
- **Mecânica:** Os jogadores podem aumentar permanentemente o número máximo de espaços do autoloot usando um item específico de expansão.

## Comandos do Jogador
Você pode gerenciar a sua configuração de autoloot usando o comando de chat `!autoloot`. É possível usar o nome dos itens diretamente.

- `!autoloot add, <nome>`: Adiciona um item à lista de autoloot.
- `!autoloot remove, <nome>`: Remove um item da lista.
- `!autoloot show`: Mostra todos os itens atualmente na lista de autoloot.
- `!autoloot clear`: Esvazia completamente a lista de autoloot.
- `!autoloot bankcoins`: Ativa/desativa o envio automático de moedas (requer o Midas Permit).

*Nota: O comando suporta separação por vírgula (`!autoloot add, gold coin`) ou espaço (`!autoloot add gold coin`).*

## Mapeamento de Contêineres (Loot Categorizado)
Você pode organizar seus saques direcionando categorias específicas de itens para contêineres designados (como mochilas específicas) dentro do seu inventário através da interface do client.

**Categorias Disponíveis:**
- Equipamentos (Equipment)
- Valiosos (Valuables)
- Poções (Potions)
- Runas (Runes)
- Diversos (Miscellaneous)
- Ouro (Gold)
- Munição (Ammo)
- Padrão (Default)
