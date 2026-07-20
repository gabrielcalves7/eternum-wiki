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
    image="${image#../}"
    require_file "$image"
  done < <(grep -oE '!\[[^]]*\]\(\.\./assets/[^)]+' "$root/$path" | sed -E 's/.*\(\.\.\///')
}

pages=(
  en/forge-system.md en/hotkeys.md en/tasks.md en/custom-areas.md
  pt/sistema-de-forja.md pt/atalhos.md pt/tarefas.md pt/areas-customizadas.md
)

for page in "${pages[@]}"; do
  require_file "$page"
  check_images "$page"
done

require_text en/forge-system.md '# Forge System'
require_text en/forge-system.md 'Tier 6'
require_text en/forge-system.md '+10'
require_text en/hotkeys.md '# PvP Hotkeys'
require_text en/hotkeys.md 'Magic Wall'
require_text en/tasks.md '# Daily Tasks'
require_text en/tasks.md '10 available tasks'
require_text en/tasks.md '3 active tasks'
require_text en/tasks.md '5 tasks per day'
require_text en/custom-areas.md '# Custom Areas'
require_text en/custom-areas.md '50 Lizard Scales'
require_text en/custom-areas.md '50 Lizard Leathers'

require_text pt/sistema-de-forja.md '# Sistema de Forja'
require_text pt/sistema-de-forja.md 'Tier 6'
require_text pt/sistema-de-forja.md '+10'
require_text pt/atalhos.md '# Atalhos no PvP'
require_text pt/atalhos.md 'Magic Wall'
require_text pt/tarefas.md '# Tarefas Diárias'
require_text pt/tarefas.md '10 tarefas disponíveis'
require_text pt/tarefas.md '3 tarefas ativas'
require_text pt/tarefas.md '5 tarefas por dia'
require_text pt/areas-customizadas.md '# Áreas Customizadas'
require_text pt/areas-customizadas.md '50 Lizard Scales'
require_text pt/areas-customizadas.md '50 Lizard Leathers'

if [[ "$failed" -ne 0 ]]; then
  exit 1
fi

echo 'Guide content validation passed.'
