# Wiki Stat Guide Updates Design

## Overview
Update the GitBook wiki stat guide generation script to hide attributes that cannot be rolled, and streamline the table by removing internal server enums and progression details (soft cap, roll chance) that players do not need to know.

## Architecture & Components
We will modify the existing `generate-stat-guides.php` script located in `wiki/scripts/`.

### 1. Data Filtering
Inside the `renderGuide()` function, we will filter out any attribute where `chance <= 0` before constructing the table rows, so that unrollable stats are not displayed.

### 2. Table Column Adjustments
We will update the table headers and data rows in `renderGuide()` to output only the following three columns:
- **English:** `Attribute`, `Base maximum`, `Eligible categories`
- **Portuguese:** `Atributo`, `Máximo base`, `Categorias elegíveis`

The columns for "Server attribute", "Soft cap", and "Roll chance" will be removed.

### 3. Introductory Text Adjustments
Since players do not need to know about the soft cap, we will remove mentions of the "Soft Cap" from the guide's introductory text and the formula description to prevent confusion. 

## Scope
This spec strictly covers the changes to the `generate-stat-guides.php` script and the resulting markdown files. 

*Note: The user also requested an attribute calculator in the Laravel app. Since that involves a completely different application and technology stack, it is treated as a separate sub-project and will be designed/planned after these wiki script changes are completed.*
