# GitBook Styling Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Apply GitBook styling (Markdown formatting, callouts, emojis, hierarchy) to all wiki pages.

**Architecture:** The agent will systematically read the markdown files and use the `multi_replace_file_content` tool or direct file overwrites to apply semantic formatting. Notes/Warnings will become `{% hint %}` blocks. Headers will be standardized.

**Tech Stack:** Markdown, GitBook.

## Global Constraints

- Do not modify the data rows in `stat-guide.md` or `guia-de-atributos.md` (they are auto-generated).
- All files must retain their original content meaning; only the presentation/formatting should be changed.
- Use `{% hint style="info" %}` for general notes, `warning` for warnings, `success` for tips, and `danger` for critical alerts.
- Emojis should be used tastefully in headers (e.g., `# ⚔️ PvP Hotkeys`).

---

### Task 1: Format Root Files and READMEs

**Files:**
- Modify: `README.md`
- Modify: `pt/README.md`
- Modify: `SUMMARY.md`

**Interfaces:**
- Consumes: None
- Produces: Formatted root navigation

- [ ] **Step 1: Update English README.md**
Add a welcome emoji to the title. Format the list of links into a cleaner structure if possible, or just add bolding/emojis to the links.
```bash
# Agent: read the file, use tool to replace content
```

- [ ] **Step 2: Update Portuguese README.md**
Apply the exact same visual structure and emojis used in the English README.md.

- [ ] **Step 3: Update SUMMARY.md**
Ensure the summary matches the new aesthetic (though SUMMARY.md in Gitbook is usually just a raw list, so minimal changes here).

- [ ] **Step 4: Commit**
```bash
git add README.md pt/README.md SUMMARY.md
git commit -m "style: format root wiki files and navigations"
```

### Task 2: Format English Gameplay Guides (Batch 1)

**Files:**
- Modify: `en/tasks.md`
- Modify: `en/dungeons.md`
- Modify: `en/custom-areas.md`
- Modify: `en/hotkeys.md`
- Modify: `en/market.md`

- [ ] **Step 1: Format `en/tasks.md` and `en/dungeons.md`**
Add emojis to the H1 headers (e.g., `# 📜 Daily Tasks`, `# 🏰 Dungeon System`). Ensure bullet points are clean. Add `{% hint style="info" %}` around notes like the "Finishing a creature task...".

- [ ] **Step 2: Format `en/custom-areas.md`, `en/hotkeys.md`, `en/market.md`**
Standardize headers. Emphasize key terms (bolding).

- [ ] **Step 3: Commit**
```bash
git add en/tasks.md en/dungeons.md en/custom-areas.md en/hotkeys.md en/market.md
git commit -m "style: format english gameplay guides batch 1"
```

### Task 3: Format English System Guides (Batch 2)

**Files:**
- Modify: `en/sets-system.md`
- Modify: `en/spells.md`
- Modify: `en/upgrade-systems.md`
- Modify: `en/relic-system.md`
- Modify: `en/autoloot-system.md`

- [ ] **Step 1: Format Sets, Spells, and Upgrade Systems**
Add relevant emojis to H1s. Look for warnings or tips to convert into `{% hint %}` blocks. Standardize any list data into tables if appropriate.

- [ ] **Step 2: Format Relic and Autoloot Systems**
Apply consistent formatting, bolding, and callouts.

- [ ] **Step 3: Commit**
```bash
git add en/sets-system.md en/spells.md en/upgrade-systems.md en/relic-system.md en/autoloot-system.md
git commit -m "style: format english system guides batch 2"
```

### Task 4: Format Remaining English Guides (Batch 3)

**Files:**
- Modify: `en/cursed-chests.md`, `en/events-and-passes.md`, `en/item-protection.md`, `en/items-and-extras.md`, `en/live-cast.md`, `en/monster-star-system.md`, `en/sacrifice-system.md`, `en/safe-training.md`, `en/shared-experience.md`, `en/stat-guide.md`

- [ ] **Step 1: Format Cursed Chests, Events, Item Protection, Items & Extras**
Apply standard headers, emojis, and hints.

- [ ] **Step 2: Format Live Cast, Monster Star, Sacrifice, Safe Training, Shared Exp**
Convert plain text notes to hint blocks.

- [ ] **Step 3: Format `en/stat-guide.md` header**
Only modify the content ABOVE the generated tables (add an emoji to the H1 and maybe an info hint). Do NOT modify the tables.

- [ ] **Step 4: Commit**
```bash
git add en/
git commit -m "style: format remaining english guides"
```

### Task 5: Format Portuguese Guides (Batches 1 & 2 Equivalent)

**Files:**
- Modify: `pt/tarefas.md`, `pt/masmorras.md`, `pt/areas-customizadas.md`, `pt/atalhos.md`, `pt/mercado.md`, `pt/sistema-de-conjuntos.md`, `pt/magias.md`, `pt/sistemas-de-upgrade.md`, `pt/sistema-de-reliquias.md`, `pt/sistema-de-autoloot.md`

- [ ] **Step 1: Process the Portuguese translations of Task 2 & 3 files**
Apply the exact same formatting structure, emojis, and `{% hint %}` block styles used in the English equivalents.

- [ ] **Step 2: Commit**
```bash
git add pt/tarefas.md pt/masmorras.md pt/areas-customizadas.md pt/atalhos.md pt/mercado.md pt/sistema-de-conjuntos.md pt/magias.md pt/sistemas-de-upgrade.md pt/sistema-de-reliquias.md pt/sistema-de-autoloot.md
git commit -m "style: format portuguese guides batch 1 and 2"
```

### Task 6: Format Remaining Portuguese Guides (Batch 3 Equivalent)

**Files:**
- Modify: `pt/baus-amaldicoados.md`, `pt/eventos-e-passes.md`, `pt/protecao-de-item.md`, `pt/itens-e-extras.md`, `pt/live-cast.md`, `pt/sistema-de-estrelas-de-monstros.md`, `pt/sistema-de-sacrificio.md`, `pt/treino-seguro.md`, `pt/experiencia-compartilhada.md`, `pt/guia-de-atributos.md`

- [ ] **Step 1: Process the Portuguese translations of Task 4 files**
Apply standard headers, emojis, and hints.

- [ ] **Step 2: Format `pt/guia-de-atributos.md` header**
Only modify the content ABOVE the generated tables.

- [ ] **Step 3: Commit**
```bash
git add pt/
git commit -m "style: format remaining portuguese guides"
```
