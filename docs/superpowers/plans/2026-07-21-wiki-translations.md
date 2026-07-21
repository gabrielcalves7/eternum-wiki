# Wiki Spanish and Polish Translations Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Translate the existing English (`en/`) documentation and the root `README.md` into Spanish (`es/`) and Polish (`pl/`), and update `SUMMARY.md` to index all the new translations.

**Architecture:** We will create two new root directories: `es/` for Spanish and `pl/` for Polish. We will mirror the file structure from `en/`. We will translate the content to Spanish and Polish while strictly retaining all GitBook callouts (`{% hint %}`), emojis, markdown tables, headers, and bullet points.

**Tech Stack:** Markdown, GitBook.

## Global Constraints

- Never modify the auto-generated data tables (e.g. in `stat-guide.md`). Leave the data rows as-is or minimally translate only the table headers.
- All GitBook components (`{% hint style="..." %}`, `{% endhint %}`) must be retained verbatim.
- All file names should be translated to the target language (just like we did for Portuguese, e.g. `items-and-extras.md` -> `es/objetos-y-extras.md`).
- Ensure the exact same directory structure and file layout as the English version.

---

### Task 1: Setup and Root Translations

**Files:**
- Create: `es/README.md`
- Create: `pl/README.md`
- Modify: `SUMMARY.md`

**Interfaces:**
- Consumes: `README.md`
- Produces: Translated READMEs and updated `SUMMARY.md`

- [ ] **Step 1: Translate README.md to Spanish**
  Read `README.md` and translate it completely into Spanish, keeping links and markdown intact. Write to `es/README.md`.
- [ ] **Step 2: Translate README.md to Polish**
  Read `README.md` and translate it completely into Polish, keeping links and markdown intact. Write to `pl/README.md`.
- [ ] **Step 3: Update SUMMARY.md**
  Read `SUMMARY.md` and append two new primary sections: `## Español` (with links to `es/README.md` and the future translated guides) and `## Polski` (with links to `pl/README.md` and the future translated guides). Match the structure of the English section exactly, translating the link texts.
- [ ] **Step 4: Commit**
```bash
git add es/README.md pl/README.md SUMMARY.md
git commit -m "feat(wiki): add spanish and polish root readmes and update summary"
```

---

### Task 2: Translate Guides to Spanish (Batch 1)

**Files:**
- Create: `es/sistema-de-autoloot.md` (from `en/autoloot-system.md`)
- Create: `es/cofres-malditos.md` (from `en/cursed-chests.md`)
- Create: `es/areas-personalizadas.md` (from `en/custom-areas.md`)
- Create: `es/mazmorras.md` (from `en/dungeons.md`)
- Create: `es/eventos-y-pases.md` (from `en/events-and-passes.md`)
- Create: `es/atajos.md` (from `en/hotkeys.md`)
- Create: `es/proteccion-de-objetos.md` (from `en/item-protection.md`)
- Create: `es/objetos-y-extras.md` (from `en/items-and-extras.md`)
- Create: `es/transmision-en-vivo.md` (from `en/live-cast.md`)
- Create: `es/mercado.md` (from `en/market.md`)

- [ ] **Step 1: Read the English files and translate to Spanish.** 
  Ensure all Markdown elements (`{% hint %}`, `*`, `##`) are preserved exactly.
- [ ] **Step 2: Save the files to the `es/` directory.**
- [ ] **Step 3: Commit**
```bash
git add es/
git commit -m "feat(wiki): add spanish translations batch 1"
```

---

### Task 3: Translate Guides to Spanish (Batch 2)

**Files:**
- Create: `es/sistema-de-estrellas-de-monstruos.md` (from `en/monster-star-system.md`)
- Create: `es/sistema-de-reliquias.md` (from `en/relic-system.md`)
- Create: `es/sistema-de-sacrificio.md` (from `en/sacrifice-system.md`)
- Create: `es/entrenamiento-seguro.md` (from `en/safe-training.md`)
- Create: `es/sistema-de-conjuntos.md` (from `en/sets-system.md`)
- Create: `es/experiencia-compartida.md` (from `en/shared-experience.md`)
- Create: `es/hechizos.md` (from `en/spells.md`)
- Create: `es/guia-de-atributos.md` (from `en/stat-guide.md`)
- Create: `es/tareas.md` (from `en/tasks.md`)
- Create: `es/sistemas-de-mejora.md` (from `en/upgrade-systems.md`)

- [ ] **Step 1: Read the English files and translate to Spanish.** 
  For `stat-guide.md`, preserve all table data/math exactly; translate only text and headers.
- [ ] **Step 2: Save the files to the `es/` directory.**
- [ ] **Step 3: Commit**
```bash
git add es/
git commit -m "feat(wiki): add spanish translations batch 2"
```

---

### Task 4: Translate Guides to Polish (Batch 1)

**Files:**
- Create: `pl/system-autoloot.md` (from `en/autoloot-system.md`)
- Create: `pl/przeklete-skrzynie.md` (from `en/cursed-chests.md`)
- Create: `pl/niestandardowe-obszary.md` (from `en/custom-areas.md`)
- Create: `pl/lochy.md` (from `en/dungeons.md`)
- Create: `pl/wydarzenia-i-przepustki.md` (from `en/events-and-passes.md`)
- Create: `pl/skroty-klawiszowe.md` (from `en/hotkeys.md`)
- Create: `pl/ochrona-przedmiotow.md` (from `en/item-protection.md`)
- Create: `pl/przedmioty-i-dodatki.md` (from `en/items-and-extras.md`)
- Create: `pl/transmisja-na-zywo.md` (from `en/live-cast.md`)
- Create: `pl/rynek.md` (from `en/market.md`)

- [ ] **Step 1: Read the English files and translate to Polish.** 
  Ensure all Markdown elements (`{% hint %}`, `*`, `##`) are preserved exactly.
- [ ] **Step 2: Save the files to the `pl/` directory.**
- [ ] **Step 3: Commit**
```bash
git add pl/
git commit -m "feat(wiki): add polish translations batch 1"
```

---

### Task 5: Translate Guides to Polish (Batch 2)

**Files:**
- Create: `pl/system-gwiazd-potworow.md` (from `en/monster-star-system.md`)
- Create: `pl/system-reliktow.md` (from `en/relic-system.md`)
- Create: `pl/system-poswiecen.md` (from `en/sacrifice-system.md`)
- Create: `pl/bezpieczny-trening.md` (from `en/safe-training.md`)
- Create: `pl/system-zestawow.md` (from `en/sets-system.md`)
- Create: `pl/dzielone-doswiadczenie.md` (from `en/shared-experience.md`)
- Create: `pl/czary.md` (from `en/spells.md`)
- Create: `pl/przewodnik-po-statystykach.md` (from `en/stat-guide.md`)
- Create: `pl/zadania.md` (from `en/tasks.md`)
- Create: `pl/systemy-ulepszen.md` (from `en/upgrade-systems.md`)

- [ ] **Step 1: Read the English files and translate to Polish.** 
  For `stat-guide.md`, preserve all table data/math exactly; translate only text and headers.
- [ ] **Step 2: Save the files to the `pl/` directory.**
- [ ] **Step 3: Commit**
```bash
git add pl/
git commit -m "feat(wiki): add polish translations batch 2"
```
