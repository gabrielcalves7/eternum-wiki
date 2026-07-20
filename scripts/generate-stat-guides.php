#!/usr/bin/env php
<?php

declare(strict_types=1);

const GUIDE_FILES = [
    'en/stat-guide.md',
    'pt/guia-de-atributos.md',
];

$configPath = getenv('RARITY_ATTRIBUTES_FILE');
if ($configPath === false || $configPath === '') {
    fwrite(STDERR, "RARITY_ATTRIBUTES_FILE is required.\n");
    exit(1);
}

$config = @file_get_contents($configPath);
if ($config === false) {
    fwrite(STDERR, "Unable to read RARITY_ATTRIBUTES_FILE: {$configPath}\n");
    exit(1);
}

function requiredMatch(string $pattern, string $subject, string $name): array
{
    if (preg_match($pattern, $subject, $matches) !== 1) {
        fwrite(STDERR, "Unable to parse {$name} from rarityAttributes.lua.\n");
        exit(1);
    }

    return $matches;
}

function formatNumber(float $value): string
{
    return rtrim(rtrim(sprintf('%.10F', $value), '0'), '.');
}

function markdownTable(array $headers, array $rows): string
{
    $header = '| ' . implode(' | ', $headers) . " |\n";
    $divider = '|' . implode('|', array_map(
        static fn (string $heading): string => str_contains($heading, 'maximum') || str_contains($heading, 'cap') || str_contains($heading, 'chance') || str_contains($heading, 'máximo') || str_contains($heading, 'teto') || str_contains($heading, 'Chance') || str_contains($heading, 'Multiplier') || str_contains($heading, 'Multiplicador') ? ' ---: ' : ' --- ',
        $headers
    )) . "|\n";

    return $header . $divider . implode('', array_map(
        static fn (array $row): string => '| ' . implode(' | ', $row) . " |\n",
        $rows
    ));
}

$basePower = (float) requiredMatch('/local BASE_POWER\\s*=\\s*([0-9.]+)/', $config, 'BASE_POWER')[1];
$softcapMultiplier = (float) requiredMatch('/local SOFTCAP_MULTIPLIER\\s*=\\s*([0-9.]+)/', $config, 'SOFTCAP_MULTIPLIER')[1];
$tierBlock = requiredMatch('/TierMultiplier\\s*=\\s*\\{(.*?)\\}/s', $config, 'TierMultiplier')[1];
preg_match_all('/\\[(\\d+)]\\s*=\\s*([0-9.]+)/', $tierBlock, $tierMatches, PREG_SET_ORDER);
if ($tierMatches === []) {
    fwrite(STDERR, "Unable to parse TierMultiplier entries from rarityAttributes.lua.\n");
    exit(1);
}

$tiers = [];
foreach ($tierMatches as $tier) {
    $tiers[(int) $tier[1]] = (float) $tier[2];
}
ksort($tiers, SORT_NUMERIC);

$attributesBlock = requiredMatch('/local AttributesConfig\\s*=\\s*\\{(.*)\\n\\}/s', $config, 'AttributesConfig')[1];
preg_match_all('/^\\s*(\\w+)\\s*=\\s*\\{\\s*(.*?)^\\s*\\},?/ms', $attributesBlock, $groupMatches, PREG_SET_ORDER);

$attributes = [];
foreach ($groupMatches as $group) {
    preg_match_all(
        '/\\{\\s*id\\s*=\\s*(ITEM_RND_[A-Z0-9_]+)\\s*,\\s*maxValue\\s*=\\s*([0-9.]+)\\s*,\\s*chance\\s*=\\s*([0-9.]+)\\s*,\\s*categories\\s*=\\s*\\{([^}]*)\\}\\s*\\}/',
        $group[2],
        $entryMatches,
        PREG_SET_ORDER
    );
    foreach ($entryMatches as $entry) {
        preg_match_all('/"([^"]+)"/', $entry[4], $categoryMatches);
        $attributes[] = [
            'group' => $group[1],
            'enum' => $entry[1],
            'maxValue' => (float) $entry[2],
            'chance' => (float) $entry[3],
            'categories' => $categoryMatches[1],
        ];
    }
}
if ($attributes === []) {
    fwrite(STDERR, "Unable to parse attribute rows from rarityAttributes.lua.\n");
    exit(1);
}
usort($attributes, static fn (array $left, array $right): int => [$left['group'], $left['enum']] <=> [$right['group'], $right['enum']]);

$labels = [
    'ITEM_RND_ATTACK' => ['Attack', 'Ataque'], 'ITEM_RND_ARMOR' => ['Armor', 'Armadura'], 'ITEM_RND_DEF' => ['Defense', 'Defesa'],
    'ITEM_RND_SKILL' => ['Skill bonus', 'Bônus de habilidade'], 'ITEM_RND_WEIGHT_REDUCTION' => ['Weight reduction', 'Redução de peso'],
    'ITEM_RND_MANA_REGEN' => ['Mana regeneration', 'Regeneração de mana'], 'ITEM_RND_HEALTH_REGEN' => ['Health regeneration', 'Regeneração de vida'],
    'ITEM_RND_MAX_HEALTH' => ['Maximum health', 'Vida máxima'], 'ITEM_RND_MAX_MANA' => ['Maximum mana', 'Mana máxima'],
    'ITEM_RND_RESISTANCE' => ['Resistance', 'Resistência'], 'ITEM_RND_ATTACK_SPEED' => ['Attack speed', 'Velocidade de ataque'],
    'ITEM_RND_CRITICAL' => ['Critical chance', 'Chance de crítico'], 'ITEM_RND_PARRY' => ['Parry', 'Aparo'],
    'ITEM_RND_PERSEVERANCE' => ['Perseverance', 'Perseverança'], 'ITEM_RND_BERSERK' => ['Berserk', 'Berserker'],
    'ITEM_RND_CRUSHING_BLOW' => ['Crushing blow', 'Golpe esmagador'], 'ITEM_RND_FAST_HAND' => ['Fast hand', 'Mão rápida'],
    'ITEM_RND_SHARPSHOOTER' => ['Sharpshooter', 'Atirador de elite'], 'ITEM_RND_BLEEDING' => ['Bleeding', 'Sangramento'],
    'ITEM_RND_ELETRICFYING' => ['Electrifying', 'Eletrificação'], 'ITEM_RND_BURNING' => ['Burning', 'Queimadura'], 'ITEM_RND_POISONING' => ['Poisoning', 'Envenenamento'],
    'ITEM_RND_SPEED' => ['Movement speed', 'Velocidade de movimento'], 'ITEM_RND_LIFELEECH_CHANCE' => ['Life leech chance', 'Chance de roubo de vida'],
    'ITEM_RND_LIFELEECH_AMOUNT' => ['Life leech amount', 'Quantidade de roubo de vida'], 'ITEM_RND_MANALEECH_CHANCE' => ['Mana leech chance', 'Chance de roubo de mana'],
    'ITEM_RND_MANALEECH_AMOUNT' => ['Mana leech amount', 'Quantidade de roubo de mana'], 'ITEM_RND_MULTISHOT' => ['Multishot', 'Disparo múltiplo'],
    'ITEM_RND_LOOT_CHANCE' => ['Loot chance', 'Chance de saque'], 'ITEM_RND_PARALYZE' => ['Paralyze', 'Paralisia'],
    'ITEM_RND_RESIST_PHYSICAL' => ['Physical resistance', 'Resistência física'], 'ITEM_RND_RESIST_FIRE' => ['Fire resistance', 'Resistência a fogo'],
    'ITEM_RND_RESIST_POISON' => ['Poison resistance', 'Resistência a veneno'], 'ITEM_RND_RESIST_ENERGY' => ['Energy resistance', 'Resistência a energia'],
    'ITEM_RND_RESIST_ICE' => ['Ice resistance', 'Resistência a gelo'], 'ITEM_RND_RESIST_HOLY' => ['Holy resistance', 'Resistência sagrada'],
    'ITEM_RND_RESIST_DEATH' => ['Death resistance', 'Resistência a morte'], 'ITEM_RND_DAMAGE_PHYSICAL' => ['Physical damage', 'Dano físico'],
    'ITEM_RND_DAMAGE_FIRE' => ['Fire damage', 'Dano de fogo'], 'ITEM_RND_DAMAGE_ICE' => ['Ice damage', 'Dano de gelo'],
    'ITEM_RND_DAMAGE_EARTH' => ['Earth damage', 'Dano de terra'], 'ITEM_RND_DAMAGE_ENERGY' => ['Energy damage', 'Dano de energia'],
    'ITEM_RND_DAMAGE_HOLY' => ['Holy damage', 'Dano sagrado'], 'ITEM_RND_DAMAGE_DEATH' => ['Death damage', 'Dano de morte'],
    'ITEM_RND_HOLY_STRIKE_CHANCE' => ['Holy strike chance', 'Chance de golpe sagrado'], 'ITEM_RND_FIRE_STRIKE_CHANCE' => ['Fire strike chance', 'Chance de golpe de fogo'],
    'ITEM_RND_DEATH_STRIKE_CHANCE' => ['Death strike chance', 'Chance de golpe de morte'], 'ITEM_RND_EARTH_STRIKE_CHANCE' => ['Earth strike chance', 'Chance de golpe de terra'],
    'ITEM_RND_ICE_STRIKE_CHANCE' => ['Ice strike chance', 'Chance de golpe de gelo'], 'ITEM_RND_ENERGY_STRIKE_CHANCE' => ['Energy strike chance', 'Chance de golpe de energia'],
    'ITEM_RND_MAGICLEVEL_PERCENT' => ['Magic level percentage', 'Porcentagem de nível mágico'], 'ITEM_RND_EXP_BONUS' => ['Experience bonus', 'Bônus de experiência'],
];

$categoryLabels = [
    'helmet' => ['Helmet', 'Elmo'], 'chest' => ['Chest armor', 'Armadura de peito'], 'legs' => ['Legs', 'Pernas'], 'boots' => ['Boots', 'Botas'],
    'melee' => ['Melee weapons', 'Armas corpo a corpo'], 'distance' => ['Distance weapons', 'Armas à distância'], 'wand' => ['Wands', 'Varinhas'],
    'shield' => ['Shields', 'Escudos'], 'amulet' => ['Amulets', 'Amuletos'], 'ring' => ['Rings', 'Anéis'], 'backpack' => ['Backpacks', 'Mochilas'],
    'quiver' => ['Quivers', 'Aljavas'], 'trinket' => ['Trinkets', 'Bugigangas'], 'two-handed' => ['Two-handed weapons', 'Armas de duas mãos'],
    'armor' => ['Armor', 'Armaduras'], 'weapons' => ['Weapons', 'Armas'], 'jewelry' => ['Jewelry', 'Joias'], 'all' => ['All equipment', 'Todos os equipamentos'],
];

function renderGuide(string $language, float $basePower, float $softcapMultiplier, array $tiers, array $attributes, array $labels, array $categoryLabels): string
{
    $isPortuguese = $language === 'pt';
    $title = $isPortuguese ? 'Guia de Atributos' : 'Stat Guide';
    $source = $isPortuguese ? 'Fonte' : 'Source';
    $scaleHeading = $isPortuguese ? 'Como as rolagens de atributos escalam' : 'How attribute rolls scale';
    $tierHeading = $isPortuguese ? 'Multiplicadores de tier' : 'Tier multipliers';
    $attributeHeading = $isPortuguese ? 'Rolagens de atributos' : 'Attribute rolls';
    $softcapText = number_format($softcapMultiplier, 2, '.', '');
    $formula = $isPortuguese
        ? '`máximo = limitar(Poder do Item × fator, 1, máximo base × ' . $softcapText . ')`'
        : '`maximum = clamp(Item Power × factor, 1, base maximum × ' . $softcapText . ')`';

    $tierRows = [];
    foreach ($tiers as $tier => $multiplier) {
        $tierRows[] = [($isPortuguese ? 'Tier ' : 'Tier ') . $tier, 'x' . formatNumber($multiplier)];
    }
    $attributeRows = [];
    foreach ($attributes as $attribute) {
        if (!isset($labels[$attribute['enum']])) {
            fwrite(STDERR, "Missing player-facing label for {$attribute['enum']}.\n");
            exit(1);
        }
        $categories = array_map(static fn (string $category): string => $categoryLabels[$category][$isPortuguese ? 1 : 0] ?? $category, $attribute['categories']);
        $attributeRows[] = [
            '`' . $attribute['enum'] . '`',
            $labels[$attribute['enum']][$isPortuguese ? 1 : 0],
            formatNumber($attribute['maxValue']),
            formatNumber($attribute['maxValue'] * $softcapMultiplier),
            formatNumber($attribute['chance']) . '%',
            implode(', ', $categories),
        ];
    }
    $headers = $isPortuguese
        ? ['Atributo do servidor', 'Atributo', 'Máximo base', 'Teto suave', 'Chance de rolagem', 'Categorias elegíveis']
        : ['Server attribute', 'Attribute', 'Base maximum', 'Soft cap', 'Roll chance', 'Eligible categories'];
    $note = $isPortuguese
        ? 'Gerado de rarityAttributes.lua; não edite manualmente as linhas de atributos.'
        : 'Generated from rarityAttributes.lua; do not edit attribute rows manually.';

    return "# {$title}\n\n> {$source}: `rarityAttributes.lua` — " . ($isPortuguese ? 'Poder Base ' : 'Base Power ') . formatNumber($basePower) . '; ' . ($isPortuguese ? 'Teto Suave ' : 'Soft Cap ') . $softcapText . ".\n\n## {$scaleHeading}\n\n{$formula}\n\n## {$tierHeading}\n\n"
        . markdownTable([$isPortuguese ? 'Tier' : 'Tier', $isPortuguese ? 'Multiplicador' : 'Multiplier'], $tierRows)
        . "\n## {$attributeHeading}\n\n"
        . markdownTable($headers, $attributeRows)
        . "\n{$note}\n";
}

$guides = [
    'en/stat-guide.md' => renderGuide('en', $basePower, $softcapMultiplier, $tiers, $attributes, $labels, $categoryLabels),
    'pt/guia-de-atributos.md' => renderGuide('pt', $basePower, $softcapMultiplier, $tiers, $attributes, $labels, $categoryLabels),
];
$root = dirname(__DIR__);

if (($argv[1] ?? '') === '--check') {
    foreach ($guides as $path => $guide) {
        $fullPath = $root . '/' . $path;
        if (!is_file($fullPath)) {
            fwrite(STDERR, "Generated Stat Guide is missing: {$path}\n");
            exit(1);
        }
        if (file_get_contents($fullPath) !== $guide) {
            fwrite(STDERR, "Generated Stat Guide is out of date: {$path}\n");
            exit(1);
        }
    }
    echo "Stat guides match rarityAttributes.lua.\n";
    exit(0);
}

foreach ($guides as $path => $guide) {
    file_put_contents($root . '/' . $path, $guide);
}
