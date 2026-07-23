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

    # Replace ' [HOT]' with ' 🔥 HOT'
    content = content.replace(' [HOT]', ' 🔥 HOT')

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)

print("Done")
