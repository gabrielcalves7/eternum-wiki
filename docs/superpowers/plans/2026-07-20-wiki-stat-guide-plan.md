# Wiki Stat Guide Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Streamline the Wiki Stat Guide by hiding unrollable stats (chance <= 0) and removing unnecessary columns like Server attribute, Soft cap, and Roll chance.

**Architecture:** Modify the `renderGuide()` function in `generate-stat-guides.php` to filter data and trim down output columns and introductory text.

**Tech Stack:** PHP

## Global Constraints

- Do not modify how `rarityAttributes.lua` is parsed.
- Keep changes contained to the presentation layer in `renderGuide()`.

---

### Task 1: Update renderGuide Filtering and Text

**Files:**
- Modify: `wiki/scripts/generate-stat-guides.php`

**Interfaces:**
- Consumes: The parsed array of `$attributes` from the Lua script.
- Produces: Correctly filtered and formatted markdown output for `en/stat-guide.md` and `pt/guia-de-atributos.md`.

- [ ] **Step 1: Filter unrollable stats in `renderGuide`**

In `wiki/scripts/generate-stat-guides.php`, inside `renderGuide`, modify the `$attributeRows` loop to skip attributes with 0 chance.

```php
    $attributeRows = [];
    foreach ($attributes as $attribute) {
        if ($attribute['chance'] <= 0) {
            continue;
        }
        if (!isset($labels[$attribute['enum']])) {
```

- [ ] **Step 2: Remove unwanted columns from `$attributeRows`**

Update the row creation logic to output only 3 columns instead of 6:

```php
        $categories = array_map(static fn (string $category): string => $categoryLabels[$category][$isPortuguese ? 1 : 0] ?? $category, $attribute['categories']);
        $attributeRows[] = [
            $labels[$attribute['enum']][$isPortuguese ? 1 : 0],
            formatNumber($attribute['maxValue']),
            implode(', ', $categories),
        ];
```

- [ ] **Step 3: Update Table Headers**

Update the `$headers` variable in `renderGuide` to match the 3 columns:

```php
    $headers = $isPortuguese
        ? ['Atributo', 'Máximo base', 'Categorias elegíveis']
        : ['Attribute', 'Base maximum', 'Eligible categories'];
```

- [ ] **Step 4: Update Introductory Text and Formula**

Remove references to the Soft Cap from the guide's intro and formula. Modify these lines:

```php
    $formula = $isPortuguese
        ? '`máximo = limitar(Poder do Item × fator, 1, máximo base)`'
        : '`maximum = clamp(Item Power × factor, 1, base maximum)`';
```

And update the return statement:

```php
    return "# {$title}\n\n> {$source}: `rarityAttributes.lua` — " . ($isPortuguese ? 'Poder Base ' : 'Base Power ') . formatNumber($basePower) . ".\n\n## {$scaleHeading}\n\n{$formula}\n\n## {$tierHeading}\n\n"
```

- [ ] **Step 5: Run the script to regenerate guides**

Run the script to verify and apply the updates:

```bash
cd wiki/scripts
php generate-stat-guides.php
```
Expected: The script runs without errors, and the markdown files are updated.

- [ ] **Step 6: Commit the changes**

```bash
git add wiki/scripts/generate-stat-guides.php wiki/en/stat-guide.md wiki/pt/guia-de-atributos.md
git commit -m "feat: streamline stat guide and filter unrollable attributes"
```
