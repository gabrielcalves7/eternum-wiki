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

    # Move the shield badge outside the link!
    pattern = r'\[([^\]]+) !\[HOT\]\(https://img\.shields\.io/badge/-HOT-red\)\]\(([^)]+)\)'
    content = re.sub(pattern, r'[\1](\2) ![HOT](https://img.shields.io/badge/-HOT-red)', content)

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
print("Done")
