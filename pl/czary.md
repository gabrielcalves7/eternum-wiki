# ✨ Przewodnik po Czarach Niestandardowych i Spoza 7.4

Eternum korzysta z protokołu 7.72, ale znacznie rozbudowuje system walki, łącząc mechaniki ze współczesnej Tibii oraz całkowicie niestandardowe czary. Poniżej znajduje się przewodnik po działaniu niestandardowych czarów i czarów spoza wersji 7.4, które napotkasz na serwerze.

## 🛡️ Mechanika Wyzwania (Exeta Res)

W standardowej wersji 7.4 czar `exeta res` po prostu powodował, że potwór na krótką chwilę zmieniał cel na Knighta. W Eternum działa on zupełnie inaczej jako prawdziwa **mechanika prowokacji (taunt)**:

{% hint style="info" %}
**Mechanika Wyzwania:**
- **Blokada Agro:** Po rzuceniu (`exeta res`) działa na obszar 3x3 wokół Knighta. Każdy trafiony potwór podatny na taunt jest **zablokowany na Knightcie przez 5 sekund**.
- **Brak Zmiany Celu:** Podczas tych 5 sekund naturalna tendencja potwora do zmiany celu jest całkowicie ignorowana. Nie mogą zmienić celu pod żadnym pozorem.
- **Brak Ucieczki:** Nawet jeśli potwór osiągnie krytyczny czerwony poziom zdrowia (lub jest uciekającą Elitą), 5-sekundowa blokada wyzwania zmusza go do pozostania i walki.
{% endhint %}

## 🧪 Czary Oczyszczające Negatywne Efekty

Eternum zawiera wiele nowych szkodliwych efektów stanów (takich jak Krwawienie, Zamrażanie, Oślepienie, Klątwa czy Tonięcie). Aby z nimi walczyć, istnieje kilka niestandardowych czarów oczyszczających:

### Purify (`exana omni`)
- **Profesja:** Wszystkie Profesje (musi być jawnie nauczony).
- **Efekt:** Czar rzucany na siebie, który natychmiast leczy **wszystkie** szkodliwe efekty obrażeń ciągłych (DoT) naraz (Trucizna, Ogień, Energia, Krwawienie, Zamrażanie, Oślepienie, Klątwa, Tonięcie).

### Mass Cleanse (`exana mas res`)
- **Profesja:** Druidzi.
- **Efekt:** Obszarowy czar wspierający (AoE), który działa na duży okrągły obszar (promień 3) wokół rzucającego. Jednocześnie leczy sojuszników i nakłada efekt `Purify`, oczyszczając wszystkie negatywne efekty DoT z każdego trafionego gracza.

### Dedykowane Czary Leczące
- **Discharge (`exana vis`):** Natychmiast leczy stan Porażenia Energą.
- **Extinguish (`exana flam`):** Natychmiast leczy stan Podpalenia.

## ⚔️ Nowoczesne Czary w Retroidowym Kliencie

Aby zapewnić bardziej dynamiczną walkę, Eternum zawiera wiele czarów normalnie spotykanych w wersjach 8.0+:

### Czary Knighta
| Czar | Słowa | Opis |
| --- | --- | --- |
| **Fierce Berserk** | `exori gran` | Znacznie silniejsza wersja Berserka zadająca ogromne obrażenia fizyczne w obszarze 3x3. |
| **Groundshaker** | `exori mas` | Jeszcze większy obszarowy atak fizyczny (AoE) uderzający w duży okrągły obszar (promień 3) wokół Knighta. |
| **Whirlwind Throw** | `exori hur` | Pozwala Knightom atakować z dystansu poprzez rzucenie bronią (zasięg 3 kratek). |

### Czary Paladina
| Czar | Słowa | Opis |
| --- | --- | --- |
| **Ethereal Spear** | `exori con` | Pojedynczy fizyczny atak dystansowy skalujący się z umiejętnością Distance i Poziomem. |
| **Divine Healing** | `exura san` | Szybkie, niezwykle wydajne leczenie stworzone specjalnie dla Paladynów. |
| **Holy Strike** | `exori san` | Pojedynczy atak zadający obrażenia od świętości. |
| **Divine Caldera** | `exevo mas san` | Obszarowy wybuch świętych obrażeń (AoE) w dużym kołowym obszarze (promień 3) wokół Paladina. |

### Zaklęcia Żywiołów Magów
Magowie mają dostęp do pełnego zestawu nowoczesnych czarów jednoliczbowych o bardzo krótkim czasie odnowienia, co pozwala na przeplatanie czarów między atakami z run:

| Kategoria | Słowa | Opis |
| --- | --- | --- |
| **Zwykłe Ataki** | `exori flam`, `exori vis`, `exori frigo`, `exori tera`, `exori mort` | Ataki jednoliczbowe danym żywiołem z niskim czas odnowienia. |
| **Większe Ataki** | `exori gran flam`, `exori gran vis`, `exori gran frigo` | Rozszerzają się na obszar 3x3 wokół celu przy wyższym koszcie many, zadając takie same obrażenia jak zwykłe ataki. |
| **Strong Ice Wave** | `exevo gran frigo hur` | Potężna kierunkowa fala lodu przeznaczona specjalnie dla Druidów. |

## 🔄 Zmienione Klasyczne Czary i Runy

Kilka klasycznych czarów i run miało dostosowane typy obrażeń, aby lepiej pasować do niestandardowej mechaniki:

| Czar / Runa | Słowa | Typ Obrażeń / Zmiana Działania |
| --- | --- | --- |
| **Sudden Death Rune (SD)** | `adori vita vis` | Zadaje obrażenia od **Śmierci** (zamiast Obrażeń Fizycznych jak w standardowym 7.4). |
| **Ultimate Explosion** | `exevo gran mas vis` | Zadaje obrażenia **Fizyczne**. |
| **Poison Storm** | `exevo gran mas pox` | Zadaje obrażenia **Fizyczne**. |
