# GitBook Wiki Styling Design

## Overview
The goal of this project is to apply a clean, professional, light-mode style with a Red/Crimson accent color to the Tibia Eternum GitBook wiki. Since modern GitBook.com restricts custom CSS files, styling will be achieved through native Markdown formatting enhancements and GitBook dashboard configurations.

## Architecture & Configuration

### 1. Dashboard Configuration (Manual)
The following settings must be applied manually by the user in the GitBook.com dashboard settings:
*   **Theme Mode:** Light
*   **Primary Accent Color:** Crimson/Red (e.g., `#DC143C` or `#B22222`)
*   **Logo:** The OTServer logo (if available)

### 2. Markdown Content Overhaul
The automated formatting will focus on the `en/` and `pt/` markdown files, standardizing them to look professional and structured.

#### Callouts & Hints
Plain text notes, warnings, and important tips will be converted to GitBook's native hint blocks:
```markdown
{% hint style="info" %}
Information text here.
{% endhint %}

{% hint style="warning" %}
Warning text here.
{% endhint %}
```

#### Tables for Data
List-based data, such as stats, item drops, and task rewards, will be converted into clean Markdown tables to improve readability and structure.

#### Typography & Hierarchy
*   **Headers:** Ensure consistent use of `H1` (Page Title), `H2` (Major Section), and `H3` (Minor Section).
*   **Emphasis:** Apply bold and italics consistently to key terms, item names, and server mechanics.
*   **Emojis:** Strategically place emojis in headers and lists to add visual breaks and professionalism (e.g., ⚔️ for PvP, 🛡️ for protection).

## Implementation Scope
The overhaul will be applied to the English (`en/`) and Portuguese (`pt/`) documentation files, as well as the root `README.md`. A script may be used or files may be edited individually.

## Testing & Validation
After the markdown formatting is applied, the changes will be pushed to the repository. The user will review the live GitBook.com site to ensure the formatting renders correctly with the new Light Mode and Crimson accent color.
