import re
import os

files_to_edit = [
    'SUMMARY.md',
    'README.md',
    'pt/README.md',
    'es/README.md',
    'pl/README.md'
]

for filename in files_to_edit:
    if not os.path.exists(filename):
        continue
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    # For SUMMARY.md:
    # Find: [🗺️ Custom Areas](en/custom-areas.md) ![HOT](https://img.shields.io/badge/-HOT-red)
    # Replace with: [🗺️ Custom Areas [HOT]](en/custom-areas.md)
    pattern1 = r'\[([^\]]+)\]\(([^)]+)\) !\[HOT\]\(https://img\.shields\.io/badge/-HOT-red\)'
    content = re.sub(pattern1, r'[\1 [HOT]](\2)', content)

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)

print("Done")
