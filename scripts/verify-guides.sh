#!/usr/bin/env bash
set -euo pipefail

root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
failed=0

require_file() {
  local path="$1"
  if [[ ! -f "$root/$path" ]]; then
    echo "Missing required file: $path" >&2
    failed=1
  fi
}

require_text() {
  local path="$1"
  local text="$2"
  if ! grep -Fq -- "$text" "$root/$path"; then
    echo "Missing required text in $path: $text" >&2
    failed=1
  fi
}

check_images() {
  local path="$1"
  local image
  while IFS= read -r image; do
    image="${image#*(}"
    image="${image#../}"
    require_file "$image"
  done < <(grep -oE '!\[[^]]*\]\(\.\./(assets|\.gitbook/assets)/[^)]+' "$root/$path")
}

pages=(
  en/upgrade-systems.md en/hotkeys.md en/tasks.md en/custom-areas.md
  en/stat-guide.md
  pt/sistemas-de-upgrade.md pt/atalhos.md pt/tarefas.md pt/areas-customizadas.md
  pt/guia-de-atributos.md
)

for page in "${pages[@]}"; do
  require_file "$page"
  check_images "$page"
done

require_text en/upgrade-systems.md '# Upgrade Systems'
require_text en/upgrade-systems.md 'Tier 6'
require_text en/upgrade-systems.md '+10'
require_text en/hotkeys.md '# PvP Hotkeys'
require_text en/hotkeys.md 'Magic Wall'
require_text en/tasks.md '# Daily Tasks'
require_text en/tasks.md '10 available tasks'
require_text en/tasks.md '3 active tasks'
require_text en/tasks.md '5 tasks per day'
require_text en/custom-areas.md '# Custom Areas'
require_text en/custom-areas.md '50 Lizard Scales'
require_text en/custom-areas.md '50 Lizard Leathers'
require_text en/stat-guide.md '# Stat Guide'

require_text pt/sistemas-de-upgrade.md '# Sistemas de Upgrade'
require_text pt/sistemas-de-upgrade.md 'Tier 6'
require_text pt/sistemas-de-upgrade.md '+10'
require_text pt/atalhos.md '# Atalhos no PvP'
require_text pt/atalhos.md 'Magic Wall'
require_text pt/tarefas.md '# Tarefas Diárias'
require_text pt/tarefas.md '10 tarefas disponíveis'
require_text pt/tarefas.md '3 tarefas ativas'
require_text pt/tarefas.md '5 tarefas por dia'
require_text pt/areas-customizadas.md '# Áreas Customizadas'
require_text pt/areas-customizadas.md '50 Lizard Scales'
require_text pt/areas-customizadas.md '50 Lizard Leathers'
require_text pt/guia-de-atributos.md '# Guia de Atributos'

if [[ -n "${RARITY_ATTRIBUTES_FILE:-}" ]]; then
  if ! RARITY_ATTRIBUTES_FILE="$RARITY_ATTRIBUTES_FILE" php "$root/scripts/generate-stat-guides.php" --check; then
    failed=1
  fi
fi

if [[ "$failed" -ne 0 ]]; then
  exit 1
fi

echo 'Guide content validation passed.'
