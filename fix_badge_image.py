import re
import os

files_to_edit = [
    'SUMMARY.md',
    'README.md',
    'pt/README.md',
    'es/README.md',
    'pl/README.md'
]

badge_img = ' ![HOT](https://img.shields.io/badge/-HOT-red)'

for filename in files_to_edit:
    if not os.path.exists(filename):
        continue
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    # The current text is like: [🗺️ Custom Areas 🔥 HOT](en/custom-areas.md)
    # or [**Custom Areas** 🔥 HOT](en/custom-areas.md)
    # We want to change it to: [🗺️ Custom Areas](en/custom-areas.md) ![HOT](https://img.shields.io/badge/-HOT-red)
    
    # Regex breakdown:
    # \[([^\]]+) 🔥 HOT\]\(([^)]+)\)
    # Replacement:
    # [\1](\2) ![HOT](https://img.shields.io/badge/-HOT-red)

    pattern = r'\[([^\]]+) 🔥 HOT\]\(([^)]+)\)'
    content = re.sub(pattern, r'[\1](\2)' + badge_img, content)

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)

print("Done")
