#!/usr/bin/env python3
"""Generate the guild-system wiki page in four languages from the server config.

Every number on those pages is derived, so none of them should ever be edited by
hand: rerun this after any guild balance change instead.

    # from the game server repo, which owns the formulas:
    OUT=/tmp/guild.tsv lua5.4 <wiki>/scripts/guild-system-data.lua
    # then from anywhere:
    python3 <wiki>/scripts/generate-guild-system.py /tmp/guild.tsv <wiki>

The two-step split is because the figures come from running the server's real
GuildSystem.CONFIG and its cost formulas, which live in another repository
(TVP-Ravenor-Server, data/lib/custom/guild_system.lua). Only the prose in the
LANGUAGES table below is written by hand.
"""
import pathlib, sys

TSV = pathlib.Path(sys.argv[1])
WIKI = pathlib.Path(sys.argv[2])

meta, buffs, levels = {}, [], {}
for line in TSV.read_text().splitlines():
    f = line.split('\t')
    if f[0] == 'buff':
        buffs.append({'key': f[1], 'label': f[2], 'unlock': int(f[3]),
                      'cap': float(f[4]), 'max': float(f[5]), 'base': int(f[6])})
    elif f[0] == 'level':
        L = int(f[1])
        n = len(buffs)
        levels[L] = {
            'next': int(f[2]), 'cum': int(f[3]), 'slots': int(f[4]),
            'bonus': [float(x) for x in f[5:5 + n]],
            'price': [(int(f[5 + n + 2 * i]), int(f[6 + n + 2 * i])) for i in range(n)],
            'price20': [(int(f[5 + 3 * n + 2 * i]), int(f[6 + 3 * n + 2 * i])) for i in range(n)],
        }
    else:
        meta[f[0]] = f[1]

MAXLVL = int(meta['maxLevel'])
BLOCK = int(meta['blockMinutes'])
MAXMIN = int(meta['maxMinutes'])
STEP = float(meta['priceStep'])
MINDON = int(meta['minDonation'])
RESET = int(meta['resetHour'])
BLOCKS_PER_DAY_CAP = MAXMIN // BLOCK


def n(x):
    return f'{int(x):,}'


def pct(x):
    return '—' if x == 0 else (f'+{int(x)}%' if x % 1 == 0 else f'+{x:g}%')


# --- language strings -------------------------------------------------------

LANGUAGES = {
'en': dict(
    file='en/guild-system.md',
    summary_after='* [🩸 Sacrifice System](en/sacrifice-system.md)',
    summary='  * [🏛️ Guild System](en/guild-system.md)',
    title='🏛️ Guild System',
    intro=('Guilds level up on gold. Members donate into a shared **treasury**, and the leadership '
           'spends it on guild levels — which grant member slots — and on five guild-wide **buffs** '
           'that apply to every member online while they run.'),
    hint_founding=(f'Founding a guild costs no gold, but your character must be at least '
                   f'**level {50}**. You can create one straight from the Guild window in the client.'),
    h_treasury='💰 The Treasury',
    treasury=[
        f'**Any member can donate.** The minimum donation is **{n(MINDON)} gold**, taken from your inventory and your bank balance together.',
        '**Only the leader and vice-leaders can spend it** — on guild levels and on buffs.',
        'Every donation is recorded per character, so the guild can see who has funded it.',
        '**Donations are never refunded.** Gold that goes into the treasury stays there.',
    ],
    h_levels='📈 Guild Levels and Member Slots',
    levels=(f'A guild runs from level 1 to **level {MAXLVL}**. Levels are counted in brackets of ten, '
            f'and each bracket grants **5 more member slots** and one more step of every unlocked buff.'),
    t_level='Guild level', t_slots='Member slots',
    h_buffs='✨ The Five Buffs',
    buffs_intro=('Each buff is unlocked by a guild level and then grows with it. A buff always runs at '
                 'the **full bonus your guild level supports** — gold buys uptime, not strength.'),
    t_buff='Buff', t_effect='Effect', t_unlock='Unlocks at', t_atunlock='Bonus at unlock', t_max=f'Max (level {MAXLVL})',
    effects={
        'magic': 'Magic level advances faster',
        'skill': 'Weapon and shielding skills advance faster',
        'exp': 'More experience from kills',
        'elite': 'Higher chance for monsters to spawn as Elite',
        'loot': 'More loot from monsters',
    },
    h_bonus='📊 Bonus by Guild Level',
    bonus_intro=(f'Up to level 50 each bracket adds **+2%** (**+1%** for Elite Monster Chance). After 50 the '
                 f'curve continues at half that rate, **+1%** per bracket (**+0.5%** for Elite), to the maximum at level {MAXLVL}.'),
    h_price='🪙 Buff Prices',
    price_intro=[
        f'Buffs are sold in **{BLOCK}-minute blocks**. A guild may hold up to **{MAXMIN} minutes** of a single buff at once.',
        f'The price depends on **your guild level and your member count**: a bigger, higher guild pays more for the same block.',
        f'**Every purchase of that buff that day costs ×{STEP} more than the last.** The counter resets at **{RESET}:00 server time**.',
    ],
    price_formula_h='The formula',
    price_formula=(f'`block = base cost × members × (1 + guild level / 20) / 4`, then multiplied by '
                   f'`{STEP}` for each block of that buff already bought today.'),
    t_perm=f'Cost **per member**: first {BLOCK}-minute block / first full hour',
    perm_note=(f'A full hour is four blocks, and the escalation applies inside it, so an hour costs '
               f'**8.125×** a single block rather than four times it. Multiply these by your member count.'),
    t_example=f'Example: a 20-member guild',
    example_note='The actual price a 20-member guild pays, for its first purchase of the day.',
    t_ladder='Blocks bought today', t_mult='Price multiplier',
    ladder_note=(f'Filling all {MAXMIN} minutes in one day therefore costs **{sum(STEP**i for i in range(BLOCKS_PER_DAY_CAP)):.2f}×** '
                 f'a single block — deliberately far more than {BLOCKS_PER_DAY_CAP} times it.'),
    h_cost='🏦 Gold Needed for Every Guild Level',
    cost_intro='Cost of the next level, and the running total donated since level 1.',
    t_from='Level', t_next='Cost of next level', t_cum='Total from level 1',
    hint_cost=(f'Reaching level 50 — where the first cap lands — takes **{n(levels[50]["cum"])} gold**, and '
               f'maxing the guild at level {MAXLVL} takes **{n(levels[MAXLVL]["cum"])} gold** in total.'),
),
'pt': dict(
    file='pt/sistema-de-guildas.md',
    summary_after='* [🩸 Sistema de Sacrifício](pt/sistema-de-sacrificio.md)',
    summary='  * [🏛️ Sistema de Guildas](pt/sistema-de-guildas.md)',
    title='🏛️ Sistema de Guildas',
    intro=('Guildas sobem de nível com ouro. Os membros doam para um **tesouro** compartilhado, e a '
           'liderança o gasta em níveis de guilda — que concedem vagas de membro — e em cinco **bônus** '
           'de guilda que valem para todos os membros online enquanto estiverem ativos.'),
    hint_founding=('Fundar uma guilda não custa ouro, mas seu personagem precisa ter no mínimo '
                   '**nível 50**. Você pode criá-la direto pela janela de Guilda no cliente.'),
    h_treasury='💰 O Tesouro',
    treasury=[
        f'**Qualquer membro pode doar.** A doação mínima é de **{n(MINDON)} de ouro**, retirada do seu inventário e do seu banco somados.',
        '**Somente o líder e os vice-líderes podem gastar** — em níveis de guilda e em bônus.',
        'Cada doação é registrada por personagem, então a guilda vê quem a financiou.',
        '**Doações nunca são devolvidas.** Ouro que entra no tesouro fica lá.',
    ],
    h_levels='📈 Níveis de Guilda e Vagas de Membro',
    levels=(f'Uma guilda vai do nível 1 ao **nível {MAXLVL}**. Os níveis são contados em faixas de dez, '
            f'e cada faixa concede **mais 5 vagas de membro** e mais um degrau de cada bônus já desbloqueado.'),
    t_level='Nível da guilda', t_slots='Vagas de membro',
    h_buffs='✨ Os Cinco Bônus',
    buffs_intro=('Cada bônus é desbloqueado por um nível de guilda e cresce junto com ele. Um bônus sempre '
                 'roda no **valor máximo que o nível da sua guilda permite** — o ouro compra tempo, não força.'),
    t_buff='Bônus', t_effect='Efeito', t_unlock='Desbloqueia no', t_atunlock='Valor ao desbloquear', t_max=f'Máximo (nível {MAXLVL})',
    effects={
        'magic': 'Magic level sobe mais rápido',
        'skill': 'Skills de arma e shielding sobem mais rápido',
        'exp': 'Mais experiência por abate',
        'elite': 'Mais chance de monstros nascerem Elite',
        'loot': 'Mais loot dos monstros',
    },
    h_bonus='📊 Bônus por Nível de Guilda',
    bonus_intro=('Até o nível 50 cada faixa soma **+2%** (**+1%** para Chance de Monstro Elite). Depois do 50 a '
                 f'curva continua pela metade, **+1%** por faixa (**+0.5%** para Elite), até o máximo no nível {MAXLVL}.'),
    h_price='🪙 Preço dos Bônus',
    price_intro=[
        f'Os bônus são vendidos em **blocos de {BLOCK} minutos**. Uma guilda pode acumular até **{MAXMIN} minutos** de um mesmo bônus.',
        'O preço depende do **nível da guilda e da quantidade de membros**: uma guilda maior e mais alta paga mais pelo mesmo bloco.',
        f'**Cada compra daquele bônus no dia custa ×{STEP} a anterior.** O contador zera às **{RESET}:00 do horário do servidor**.',
    ],
    price_formula_h='A fórmula',
    price_formula=(f'`bloco = custo base × membros × (1 + nível da guilda / 20) / 4`, multiplicado por '
                   f'`{STEP}` para cada bloco daquele bônus já comprado no dia.'),
    t_perm=f'Custo **por membro**: primeiro bloco de {BLOCK} min / primeira hora cheia',
    perm_note=('Uma hora são quatro blocos, e o aumento já vale dentro dela, então a hora custa '
               '**8.125×** um bloco, e não quatro vezes. Multiplique pelo número de membros.'),
    t_example='Exemplo: guilda com 20 membros',
    example_note='O preço real que uma guilda de 20 membros paga, na primeira compra do dia.',
    t_ladder='Blocos comprados hoje', t_mult='Multiplicador de preço',
    ladder_note=(f'Encher os {MAXMIN} minutos em um único dia custa, portanto, **{sum(STEP**i for i in range(BLOCKS_PER_DAY_CAP)):.2f}×** '
                 f'um bloco — de propósito, muito mais do que {BLOCKS_PER_DAY_CAP} vezes.'),
    h_cost='🏦 Ouro Necessário para Cada Nível de Guilda',
    cost_intro='Custo do próximo nível e o total acumulado desde o nível 1.',
    t_from='Nível', t_next='Custo do próximo nível', t_cum='Total desde o nível 1',
    hint_cost=(f'Chegar ao nível 50 — onde o primeiro teto acontece — custa **{n(levels[50]["cum"])} de ouro**, e '
               f'maximizar a guilda no nível {MAXLVL} custa **{n(levels[MAXLVL]["cum"])} de ouro** no total.'),
),
'es': dict(
    file='es/sistema-de-gremios.md',
    summary_after='* [🩸 Sistema de Sacrificio](es/sistema-de-sacrificio.md)',
    summary='  * [🏛️ Sistema de Gremios](es/sistema-de-gremios.md)',
    title='🏛️ Sistema de Gremios',
    intro=('Los gremios suben de nivel con oro. Los miembros donan a un **tesoro** común, y el liderazgo '
           'lo gasta en niveles de gremio — que otorgan plazas de miembro — y en cinco **bonificaciones** '
           'de gremio que se aplican a todos los miembros conectados mientras estén activas.'),
    hint_founding=('Fundar un gremio no cuesta oro, pero tu personaje debe ser al menos de '
                   '**nivel 50**. Puedes crearlo directamente desde la ventana de Gremio en el cliente.'),
    h_treasury='💰 El Tesoro',
    treasury=[
        f'**Cualquier miembro puede donar.** La donación mínima es de **{n(MINDON)} de oro**, tomada de tu inventario y de tu banco en conjunto.',
        '**Solo el líder y los vicelíderes pueden gastarlo** — en niveles de gremio y en bonificaciones.',
        'Cada donación se registra por personaje, así el gremio ve quién lo ha financiado.',
        '**Las donaciones no se devuelven nunca.** El oro que entra al tesoro se queda allí.',
    ],
    h_levels='📈 Niveles de Gremio y Plazas de Miembro',
    levels=(f'Un gremio va del nivel 1 al **nivel {MAXLVL}**. Los niveles se cuentan en tramos de diez, '
            f'y cada tramo otorga **5 plazas más** y un escalón más de cada bonificación desbloqueada.'),
    t_level='Nivel de gremio', t_slots='Plazas de miembro',
    h_buffs='✨ Las Cinco Bonificaciones',
    buffs_intro=('Cada bonificación se desbloquea con un nivel de gremio y crece con él. Una bonificación '
                 'siempre corre al **máximo que permite tu nivel de gremio** — el oro compra tiempo, no potencia.'),
    t_buff='Bonificación', t_effect='Efecto', t_unlock='Se desbloquea en', t_atunlock='Valor al desbloquear', t_max=f'Máximo (nivel {MAXLVL})',
    effects={
        'magic': 'El magic level sube más rápido',
        'skill': 'Las skills de arma y shielding suben más rápido',
        'exp': 'Más experiencia por muerte',
        'elite': 'Más probabilidad de que los monstruos aparezcan como Elite',
        'loot': 'Más loot de los monstruos',
    },
    h_bonus='📊 Bonificación por Nivel de Gremio',
    bonus_intro=('Hasta el nivel 50 cada tramo suma **+2%** (**+1%** para Probabilidad de Monstruo Elite). '
                 f'A partir de 50 la curva sigue a la mitad, **+1%** por tramo (**+0.5%** para Elite), hasta el máximo en el nivel {MAXLVL}.'),
    h_price='🪙 Precio de las Bonificaciones',
    price_intro=[
        f'Se venden en **bloques de {BLOCK} minutos**. Un gremio puede acumular hasta **{MAXMIN} minutos** de una misma bonificación.',
        'El precio depende del **nivel del gremio y del número de miembros**: un gremio más grande y más alto paga más por el mismo bloque.',
        f'**Cada compra de esa bonificación en el día cuesta ×{STEP} la anterior.** El contador se reinicia a las **{RESET}:00 hora del servidor**.',
    ],
    price_formula_h='La fórmula',
    price_formula=(f'`bloque = coste base × miembros × (1 + nivel de gremio / 20) / 4`, multiplicado por '
                   f'`{STEP}` por cada bloque de esa bonificación ya comprado hoy.'),
    t_perm=f'Coste **por miembro**: primer bloque de {BLOCK} min / primera hora completa',
    perm_note=('Una hora son cuatro bloques, y el aumento ya se aplica dentro de ella, así que la hora cuesta '
               '**8.125×** un bloque, no cuatro veces. Multiplica por tu número de miembros.'),
    t_example='Ejemplo: gremio de 20 miembros',
    example_note='El precio real que paga un gremio de 20 miembros, en su primera compra del día.',
    t_ladder='Bloques comprados hoy', t_mult='Multiplicador de precio',
    ladder_note=(f'Llenar los {MAXMIN} minutos en un solo día cuesta por tanto **{sum(STEP**i for i in range(BLOCKS_PER_DAY_CAP)):.2f}×** '
                 f'un bloque — a propósito, mucho más que {BLOCKS_PER_DAY_CAP} veces.'),
    h_cost='🏦 Oro Necesario para Cada Nivel de Gremio',
    cost_intro='Coste del siguiente nivel y el total acumulado desde el nivel 1.',
    t_from='Nivel', t_next='Coste del siguiente nivel', t_cum='Total desde el nivel 1',
    hint_cost=(f'Llegar al nivel 50 — donde está el primer tope — cuesta **{n(levels[50]["cum"])} de oro**, y '
               f'maximizar el gremio en el nivel {MAXLVL} cuesta **{n(levels[MAXLVL]["cum"])} de oro** en total.'),
),
'pl': dict(
    file='pl/system-gildii.md',
    summary_after='* [🩸 System Poświęceń](pl/system-poswiecen.md)',
    summary='  * [🏛️ System Gildii](pl/system-gildii.md)',
    title='🏛️ System Gildii',
    intro=('Gildie zdobywają poziomy za złoto. Członkowie wpłacają do wspólnego **skarbca**, a przywództwo '
           'wydaje je na poziomy gildii — dające miejsca dla członków — oraz na pięć **wzmocnień**, '
           'które działają na wszystkich członków online, dopóki są aktywne.'),
    hint_founding=('Założenie gildii nie kosztuje złota, ale twoja postać musi mieć co najmniej '
                   '**poziom 50**. Możesz ją utworzyć bezpośrednio w oknie Gildii w kliencie.'),
    h_treasury='💰 Skarbiec',
    treasury=[
        f'**Wpłacać może każdy członek.** Minimalna wpłata to **{n(MINDON)} złota**, pobierane łącznie z ekwipunku i z banku.',
        '**Wydawać mogą tylko lider i wiceliderzy** — na poziomy gildii i na wzmocnienia.',
        'Każda wpłata jest zapisywana przy postaci, więc gildia widzi, kto ją finansuje.',
        '**Wpłaty nigdy nie są zwracane.** Złoto, które trafi do skarbca, zostaje w nim.',
    ],
    h_levels='📈 Poziomy Gildii i Miejsca dla Członków',
    levels=(f'Gildia rozwija się od poziomu 1 do **poziomu {MAXLVL}**. Poziomy liczone są w przedziałach po dziesięć, '
            f'a każdy przedział daje **5 dodatkowych miejsc** i jeden stopień każdego odblokowanego wzmocnienia.'),
    t_level='Poziom gildii', t_slots='Miejsca dla członków',
    h_buffs='✨ Pięć Wzmocnień',
    buffs_intro=('Każde wzmocnienie odblokowuje się na danym poziomie gildii i rośnie razem z nim. Wzmocnienie '
                 'zawsze działa na **maksimum, na które pozwala poziom gildii** — złoto kupuje czas, nie moc.'),
    t_buff='Wzmocnienie', t_effect='Efekt', t_unlock='Odblokowanie', t_atunlock='Wartość na starcie', t_max=f'Maksimum (poziom {MAXLVL})',
    effects={
        'magic': 'Szybszy przyrost magic level',
        'skill': 'Szybszy przyrost skilli broni i shieldingu',
        'exp': 'Więcej doświadczenia za zabicia',
        'elite': 'Większa szansa na potwory Elite',
        'loot': 'Więcej lootu z potworów',
    },
    h_bonus='📊 Wzmocnienia Według Poziomu Gildii',
    bonus_intro=('Do poziomu 50 każdy przedział dodaje **+2%** (**+1%** dla szansy na potwora Elite). Powyżej 50 '
                 f'krzywa biegnie o połowę wolniej, **+1%** na przedział (**+0.5%** dla Elite), aż do maksimum na poziomie {MAXLVL}.'),
    h_price='🪙 Ceny Wzmocnień',
    price_intro=[
        f'Wzmocnienia sprzedawane są w **blokach po {BLOCK} minut**. Gildia może zgromadzić najwyżej **{MAXMIN} minut** jednego wzmocnienia.',
        'Cena zależy od **poziomu gildii i liczby członków**: większa i wyżej rozwinięta gildia płaci za ten sam blok więcej.',
        f'**Każdy kolejny zakup tego wzmocnienia w danym dniu kosztuje ×{STEP} więcej.** Licznik zeruje się o **{RESET}:00 czasu serwera**.',
    ],
    price_formula_h='Wzór',
    price_formula=(f'`blok = koszt bazowy × liczba członków × (1 + poziom gildii / 20) / 4`, pomnożone przez '
                   f'`{STEP}` za każdy blok tego wzmocnienia kupiony już dzisiaj.'),
    t_perm=f'Koszt **na członka**: pierwszy blok {BLOCK} min / pierwsza pełna godzina',
    perm_note=('Godzina to cztery bloki, a podwyżka działa już w jej trakcie, więc godzina kosztuje '
               '**8.125×** jeden blok, a nie cztery razy tyle. Pomnóż przez liczbę członków.'),
    t_example='Przykład: gildia licząca 20 członków',
    example_note='Rzeczywista cena dla gildii liczącej 20 członków, przy pierwszym zakupie danego dnia.',
    t_ladder='Bloki kupione dzisiaj', t_mult='Mnożnik ceny',
    ladder_note=(f'Zapełnienie wszystkich {MAXMIN} minut jednego dnia kosztuje więc **{sum(STEP**i for i in range(BLOCKS_PER_DAY_CAP)):.2f}×** '
                 f'jeden blok — celowo znacznie więcej niż {BLOCKS_PER_DAY_CAP} razy.'),
    h_cost='🏦 Złoto Potrzebne na Każdy Poziom Gildii',
    cost_intro='Koszt następnego poziomu i suma wpłacona od poziomu 1.',
    t_from='Poziom', t_next='Koszt następnego poziomu', t_cum='Łącznie od poziomu 1',
    hint_cost=(f'Dojście do poziomu 50 — gdzie kończy się pierwszy pułap — kosztuje **{n(levels[50]["cum"])} złota**, a '
               f'maksymalny poziom {MAXLVL} to łącznie **{n(levels[MAXLVL]["cum"])} złota**.'),
),
}


def page(t):
    o = []
    w = o.append
    w(f'# {t["title"]}\n')
    w(t['intro'] + '\n')
    w('{% hint style="info" %}\n' + t['hint_founding'] + '\n{% endhint %}\n')

    w(f'## {t["h_treasury"]}\n')
    for line in t['treasury']:
        w(f'- {line}')
    w('')

    w(f'## {t["h_levels"]}\n')
    w(t['levels'] + '\n')
    slot_levels = [1, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    w(f'| {t["t_level"]} | ' + ' | '.join(str(x) for x in slot_levels) + ' |')
    w('|---' * (len(slot_levels) + 1) + '|')
    w(f'| {t["t_slots"]} | ' + ' | '.join(str(levels[x]['slots']) for x in slot_levels) + ' |\n')

    w(f'## {t["h_buffs"]}\n')
    w(t['buffs_intro'] + '\n')
    w(f'| {t["t_buff"]} | {t["t_effect"]} | {t["t_unlock"]} | {t["t_atunlock"]} | {t["t_max"]} |')
    w('|---|---|---|---|---|')
    for i, b in enumerate(buffs):
        w(f'| **{b["label"]}** | {t["effects"][b["key"]]} | {b["unlock"]} | '
          f'{pct(levels[b["unlock"]]["bonus"][i])} | {pct(b["max"])} |')
    w('')

    w(f'## {t["h_bonus"]}\n')
    w(t['bonus_intro'] + '\n')
    w('| ' + t['t_level'] + ' | ' + ' | '.join(b['label'] for b in buffs) + ' |')
    w('|---' * (len(buffs) + 1) + '|')
    for lv in range(5, MAXLVL + 1, 5):
        w(f'| **{lv}** | ' + ' | '.join(pct(v) for v in levels[lv]['bonus']) + ' |')
    w('')

    w(f'## {t["h_price"]}\n')
    for line in t['price_intro']:
        w(f'- {line}')
    w('')
    w(f'**{t["price_formula_h"]}** — {t["price_formula"]}\n')

    w(f'### {t["t_perm"]}\n')
    w(t['perm_note'] + '\n')
    price_levels = [5, 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100]
    w('| ' + t['t_level'] + ' | ' + ' | '.join(b['label'] for b in buffs) + ' |')
    w('|---' * (len(buffs) + 1) + '|')
    for lv in price_levels:
        cells = []
        for i, b in enumerate(buffs):
            if lv < b['unlock']:
                cells.append('—')
            else:
                blk, hour = levels[lv]['price'][i]
                cells.append(f'{n(blk)} / {n(hour)}')
        w(f'| **{lv}** | ' + ' | '.join(cells) + ' |')
    w('')

    w(f'### {t["t_example"]}\n')
    w(t['example_note'] + '\n')
    w('| ' + t['t_level'] + ' | ' + ' | '.join(b['label'] for b in buffs) + ' |')
    w('|---' * (len(buffs) + 1) + '|')
    for lv in [25, 50, 75, 100]:
        cells = []
        for i, b in enumerate(buffs):
            blk, hour = levels[lv]['price20'][i]
            cells.append(f'{n(blk)} / {n(hour)}')
        w(f'| **{lv}** | ' + ' | '.join(cells) + ' |')
    w('')

    w(f'| {t["t_ladder"]} | ' + ' | '.join(str(i + 1) for i in range(BLOCKS_PER_DAY_CAP)) + ' |')
    w('|---' * (BLOCKS_PER_DAY_CAP + 1) + '|')
    w(f'| {t["t_mult"]} | ' + ' | '.join(f'×{STEP**i:.2f}'.rstrip('0').rstrip('.') for i in range(BLOCKS_PER_DAY_CAP)) + ' |\n')
    w('{% hint style="warning" %}\n' + t['ladder_note'] + '\n{% endhint %}\n')

    w(f'## {t["h_cost"]}\n')
    w(t['cost_intro'] + '\n')
    for start in range(1, MAXLVL, 25):
        end = min(start + 24, MAXLVL - 1)
        w(f'| {t["t_from"]} | {t["t_next"]} | {t["t_cum"]} |')
        w('|---|---|---|')
        for lv in range(start, end + 1):
            w(f'| {lv} → {lv + 1} | {n(levels[lv]["next"])} | {n(levels[lv + 1]["cum"])} |')
        w('')

    w('{% hint style="success" %}\n' + t['hint_cost'] + '\n{% endhint %}')
    return '\n'.join(o) + '\n'


summary = (WIKI / 'SUMMARY.md').read_text()
for lang, t in LANGUAGES.items():
    path = WIKI / t['file']
    path.write_text(page(t))
    print('wrote', path)

    anchor = t['summary_after']
    assert anchor.strip() in [x.strip() for x in summary.splitlines()], f'anchor not found: {anchor}'
    summary = summary.replace(anchor, anchor + '\n' + t['summary'], 1)

(WIKI / 'SUMMARY.md').write_text(summary)
print('updated SUMMARY.md')
