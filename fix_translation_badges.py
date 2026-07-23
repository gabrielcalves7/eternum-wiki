import re
import os

configs = [
    {
        'file': 'pt/README.md',
        'targets': [
            'areas-customizadas.md', 'sistemas-de-upgrade.md', 'treino-seguro.md',
            'sistema-de-reliquias.md', 'masmorras.md', 'protecao-de-item.md',
            'baus-amaldicoados.md', 'sistema-de-autoloot.md', 'sistema-de-conjuntos.md',
            'magias.md'
        ]
    },
    {
        'file': 'es/README.md',
        'targets': [
            'areas-personalizadas.md', 'sistemas-de-mejora.md', 'entrenamiento-seguro.md',
            'sistema-de-reliquias.md', 'mazmorras.md', 'proteccion-de-objetos.md',
            'cofres-malditos.md', 'sistema-de-autoloot.md', 'sistema-de-conjuntos.md',
            'hechizos.md'
        ]
    },
    {
        'file': 'pl/README.md',
        'targets': [
            'niestandardowe-obszary.md', 'systemy-ulepszen.md', 'bezpieczny-trening.md',
            'system-reliktow.md', 'lochy.md', 'ochrona-przedmiotow.md',
            'przeklete-skrzynie.md', 'system-autoloot.md', 'system-zestawow.md',
            'czary.md'
        ]
    }
]

badge = ' ![HOT](https://img.shields.io/badge/-HOT-red)'

for cfg in configs:
    filename = cfg['file']
    if not os.path.exists(filename):
        continue
    
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    for target in cfg['targets']:
        # Find [text](target) and append badge if not present
        pattern = r'(\[.*?\]\(' + re.escape(target) + r'\))(?! !\[HOT\])'
        content = re.sub(pattern, r'\1' + badge, content)

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)

print("Done")
