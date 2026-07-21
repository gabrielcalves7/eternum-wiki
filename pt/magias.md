# ✨ Guia de Magias Customizadas e Pós-7.4

O Eternum usa o protocolo 7.72, mas expande profundamente o sistema de combate ao incorporar mecânicas do Tibia moderno e magias totalmente customizadas. Abaixo está um guia sobre os comportamentos de magias personalizadas e magias pós-7.4 que você encontrará no servidor.

## 🛡️ Mecânicas de Provocação (Exeta Res)

No 7.4 padrão, o `exeta res` simplesmente fazia com que o monstro mudasse de alvo para o Knight por um breve momento. No Eternum, ele funciona de forma completamente diferente, sendo um verdadeiro **taunt**:

{% hint style="info" %}
**Mecânicas de Provocação:**
- **Travar Alvo (Aggro Lock):** Ao ser conjurado (`exeta res`), afeta uma área 3x3 ao redor do Knight. Qualquer monstro suscetível atingido fica **travado no Knight por 5 segundos**.
- **Sem Troca de Alvo:** Durante esses 5 segundos, a tendência natural do monstro de mudar de alvo é completamente ignorada. Eles não podem trocar de alvo sob nenhuma circunstância.
- **Sem Fuga:** Mesmo se um monstro chegar à vida crítica (vermelha) ou for um Elite fugitivo, o travamento de 5 segundos os força a continuar lutando.
{% endhint %}

## 🧪 Magias de Limpeza de Condições

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

## ⚔️ Magias Modernas em um Cliente Retrô

Para proporcionar uma experiência de combate mais dinâmica, o Eternum inclui muitas magias normalmente encontradas nas versões 8.0+:

### Magias de Knight
| Magia | Palavras | Descrição |
| --- | --- | --- |
| **Fierce Berserk** | `exori gran` | Uma versão significativamente mais forte do Berserk que causa dano físico massivo em uma área 3x3. |
| **Groundshaker** | `exori mas` | Um ataque físico em área ainda maior que atinge uma grande área circular (raio 3) ao redor do Knight. |
| **Whirlwind Throw** | `exori hur` | Permite aos Knights atacarem de longe arremessando sua arma (alcance de 3 SQM). |

### Magias de Paladin
| Magia | Palavras | Descrição |
| --- | --- | --- |
| **Ethereal Spear** | `exori con` | Uma magia de ataque físico à distância contra um único alvo, que escala com nível e skill de Distance. |
| **Divine Healing** | `exura san` | Uma cura rápida e altamente eficiente feita especificamente para Paladins. |
| **Holy Strike** | `exori san` | Um ataque de alvo único causando dano Holy. |
| **Divine Caldera** | `exevo mas san` | Uma explosão em área de dano Holy em uma grande área circular (raio 3) ao redor do Paladin. |

### Magias Elementais de Mage (Strikes)
Os magos têm acesso ao conjunto completo de magias de alvo único (strikes) modernos, com tempos de recarga (cooldowns) muito baixos, permitindo que utilizem magias entre os ataques de runas:

| Categoria | Palavras | Descrição |
| --- | --- | --- |
| **Strikes Normais** | `exori flam`, `exori vis`, `exori frigo`, `exori tera`, `exori mort` | Strikes elementais de alvo único com baixo tempo de recarga. |
| **Great Strikes** | `exori gran flam`, `exori gran vis`, `exori gran frigo` | Expandem para uma área 3x3 ao redor do alvo com custo de mana mais alto, causando o mesmo dano que os strikes normais. |
| **Strong Ice Wave** | `exevo gran frigo hur` | Uma poderosa onda direcional de gelo exclusiva para Druids. |

## 🔄 Magias Retrô e Runas Alteradas

Algumas magias e runas clássicas tiveram seus tipos de dano ajustados para melhor se adequarem às mecânicas customizadas:

| Magia / Runa | Palavras | Tipo de Dano / Alteração de Comportamento |
| --- | --- | --- |
| **Runa de Sudden Death (SD)** | `adori vita vis` | Causa dano de **Morte** (em vez de dano Físico como no 7.4 padrão). |
| **Ultimate Explosion** | `exevo gran mas vis` | Causa dano **Físico**. |
| **Poison Storm** | `exevo gran mas pox` | Causa dano **Físico**. |
