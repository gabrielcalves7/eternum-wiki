import re
import os

files_to_edit = [
    'SUMMARY.md',
    'README.md',
    'pt/README.md',
    'es/README.md',
    'pl/README.md'
]

targets = [
    'en/custom-areas.md',
    'en/upgrade-systems.md',
    'en/safe-training.md',
    'en/relic-system.md',
    'en/dungeons.md',
    'en/item-protection.md',
    'en/cursed-chests.md',
    'en/autoloot-system.md',
    'en/sets-system.md',
    'en/spells.md',
    
    'pt/areas-customizadas.md',
    'pt/sistemas-de-upgrade.md',
    'pt/treino-seguro.md',
    'pt/sistema-de-reliquias.md',
    'pt/masmorras.md',
    'pt/protecao-de-item.md',
    'pt/baus-amaldicoados.md',
    'pt/sistema-de-autoloot.md',
    'pt/sistema-de-conjuntos.md',
    'pt/magias.md',
    
    'es/areas-personalizadas.md',
    'es/sistemas-de-mejora.md',
    'es/entrenamiento-seguro.md',
    'es/sistema-de-reliquias.md',
    'es/mazmorras.md',
    'es/proteccion-de-objetos.md',
    'es/cofres-malditos.md',
    'es/sistema-de-autoloot.md',
    'es/sistema-de-conjuntos.md',
    'es/hechizos.md',
    
    'pl/niestandardowe-obszary.md',
    'pl/systemy-ulepszen.md',
    'pl/bezpieczny-trening.md',
    'pl/system-reliktow.md',
    'pl/lochy.md',
    'pl/ochrona-przedmiotow.md',
    'pl/przeklete-skrzynie.md',
    'pl/system-autoloot.md',
    'pl/system-zestawow.md',
    'pl/czary.md'
]

for filename in files_to_edit:
    if not os.path.exists(filename):
        continue
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    for target in targets:
        # In SUMMARY.md it looks like: [🗺️ Custom Areas](en/custom-areas.md)
        # In README.md it looks like: [**Custom Areas**](en/custom-areas.md)
        
        # Regex to find the link text and append 🔥 before the closing bracket
        # Look for [SOMETHING](target)
        pattern = r'(\[.*?)(?! 🔥)(\]\(' + re.escape(target) + r'\))'
        
        def repl(m):
            text = m.group(1)
            # Avoid adding multiple times
            if not text.endswith(' 🔥'):
                return text + ' 🔥' + m.group(2)
            return m.group(0)

        content = re.sub(pattern, repl, content)

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)

print("Done")
