# Guia de Magias Customizadas e Pós-7.4

O Eternum usa o protocolo 7.72, mas expande profundamente o sistema de combate ao incorporar mecânicas do Tibia moderno e magias totalmente customizadas. Abaixo está um guia sobre os comportamentos de magias personalizadas e magias pós-7.4 que você encontrará no servidor.

## 1. Mecânicas de Provocação (Exeta Res)

No 7.4 padrão, o `exeta res` simplesmente fazia com que o monstro mudasse de alvo para o Knight por um breve momento. No Eternum, ele funciona de forma completamente diferente, sendo um verdadeiro "taunt":

- **Travar Alvo (Aggro Lock):** Ao ser conjurado (`exeta res`), afeta uma área 3x3 ao redor do Knight. Qualquer monstro suscetível atingido fica **travado no Knight por 5 segundos**.
- **Sem Troca de Alvo:** Durante esses 5 segundos, a chance natural de mudança de alvo (`changeTargetChance`) do monstro é completamente ignorada. Eles não podem trocar de alvo sob nenhuma circunstância.
- **Sem Fuga:** Mesmo se um monstro chegar à vida crítica (vermelha) ou for um Elite fugitivo, o travamento de 5 segundos os força a continuar lutando.

## 2. Magias de Limpeza de Condições

O Eternum possui várias novas condições negativas de status (como Bleeding, Freezing, Dazzled, Cursed e Drown). Para combater isso, existem diversas magias de limpeza customizadas:

### Purify (`exana omni`)
- **Vocação:** Todas as Vocações (deve ser aprendida explicitamente).
- **Efeito:** Uma magia para si mesmo que cura instantaneamente **todas** as condições nocivas de dano ao longo do tempo (Poison, Fire, Energy, Bleeding, Freezing, Dazzled, Cursed, Drown).

### Mass Cleanse (`exana mas res`)
- **Vocação:** Druids.
- **Efeito:** Uma magia de suporte em área que afeta uma grande área circular (raio 3) ao redor de quem conjurou. Ela simultaneamente cura os aliados e aplica o efeito do `Purify`, limpando todas as condições negativas (DoT) de cada jogador atingido.

### Curas Específicas
- **Discharge (`exana vis`):** Cura instantaneamente a condição de Energia (eletrificado).
- **Extinguish (`exana flam`):** Cura instantaneamente a condição de Queimadura (fogo).

## 3. Magias Modernas em um Cliente Retrô

Para proporcionar uma experiência de combate mais dinâmica, o Eternum inclui muitas magias normalmente encontradas nas versões 8.0+:

### Magias de Knight
- **Fierce Berserk (`exori gran`):** Uma versão significativamente mais forte do Berserk que causa dano físico massivo em uma área 3x3.
- **Groundshaker (`exori mas`):** Um ataque físico em área ainda maior que atinge uma grande área circular (raio 3) ao redor do Knight.
- **Whirlwind Throw (`exori hur`):** Permite aos Knights atacarem de longe arremessando sua arma (alcance de 3 SQM).

### Magias de Paladin
- **Ethereal Spear (`exori con`):** Uma magia de ataque físico à distância contra um único alvo, que escala com nível e skill de Distance.
- **Divine Healing (`exura san`):** Uma cura rápida e altamente eficiente feita especificamente para Paladins.
- **Holy Strike (`exori san`):** Um ataque de alvo único causando dano Holy.
- **Divine Caldera (`exevo mas san`):** Uma explosão em área de dano Holy em uma grande área circular (raio 3) ao redor do Paladin.

### Magias Elementais de Mage (Strikes)
Os magos têm acesso ao conjunto completo de magias de alvo único (strikes) modernos, com tempos de recarga (cooldowns) muito baixos, permitindo que utilizem magias entre os ataques de runas:
- **Strikes Normais:** Flame Strike (`exori flam`), Energy Strike (`exori vis`), Ice Strike (`exori frigo`), Terra Strike (`exori tera`), Death Strike (`exori mort`).
  - **Great Strikes:** Custo de mana mais alto, mas causam o **mesmo dano** que os strikes normais. Em vez de atingir um único alvo, eles expandem para uma área em formato 3x3 ao redor do alvo/posição conjurada (ex: `exori gran flam`, `exori gran vis`, `exori gran frigo`).
- **Strong Ice Wave (`exevo gran frigo hur`):** Uma poderosa onda direcional de gelo exclusiva para Druids.

## 4. Magias Retrô e Runas Alteradas

Algumas magias e runas clássicas tiveram seus tipos de dano ajustados para melhor se adequarem às mecânicas customizadas:
- **Runa de Sudden Death (SD):** Causa dano de **Morte** (Death damage), e não dano Físico como no 7.4 padrão.
- **Ultimate Explosion (`exevo gran mas vis`):** Causa dano **Físico** (Physical damage).
- **Poison Storm (`exevo gran mas pox`):** Causa dano **Físico** (Physical damage).
