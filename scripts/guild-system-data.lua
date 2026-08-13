-- Emits every figure the guild-system wiki pages quote, read out of the game
-- server's own config and cost formulas rather than copied.
--
-- Run from the root of the game server repo (TVP-Ravenor-Server), which is where
-- data/lib/custom/guild_system.lua lives:
--
--     OUT=/tmp/guild.tsv lua5.4 <wiki>/scripts/guild-system-data.lua
--
-- Then feed the TSV to generate-guild-system.py.

local src = io.open("data/lib/custom/guild_system.lua"):read("a")
GuildSystem = {}
load(src:match("(GuildSystem%.CONFIG = {.-\n})"))()
local C = GuildSystem.CONFIG
local body = {}
for _, n in ipairs({"getLevelCost","getMaxSlots","getBonus","getBuffCost","getBlockCost"}) do
    body[#body+1] = src:match("(function GuildSystem%." .. n .. ".-\nend)")
end
load("local CONFIG = GuildSystem.CONFIG\n" .. table.concat(body, "\n"))()

local out = io.open(os.getenv("OUT"), "w")
out:write("maxLevel\t", C.maxLevel, "\n")
out:write("blockMinutes\t", C.buffBlockMinutes, "\n")
out:write("maxMinutes\t", C.buffMaxMinutes, "\n")
out:write("priceStep\t", C.buffPriceStep, "\n")
out:write("minDonation\t", C.minDonation, "\n")
out:write("resetHour\t", C.buffResetHour, "\n")
for _, b in ipairs(C.buffOrder) do
    local cfg = C.buffs[b]
    out:write("buff\t", b, "\t", cfg.label, "\t", cfg.unlock, "\t", cfg.cap, "\t",
        GuildSystem.getBonus(b, C.maxLevel), "\t", cfg.baseCost, "\n")
end
local total = 0
for L = 1, C.maxLevel do
    -- level, cost to next, cumulative to reach L, slots, bonus per buff
    out:write("level\t", L, "\t", GuildSystem.getLevelCost(L), "\t", total, "\t", GuildSystem.getMaxSlots(L))
    for _, b in ipairs(C.buffOrder) do out:write("\t", GuildSystem.getBonus(b, L)) end
    -- per-member first block and first hour (4 escalating blocks)
    for _, members in ipairs({1, 20}) do
        for _, b in ipairs(C.buffOrder) do
            local hour = 0
            for p = 0, 3 do hour = hour + GuildSystem.getBlockCost(b, L, members, p) end
            out:write("\t", GuildSystem.getBlockCost(b, L, members, 0), "\t", hour)
        end
    end
    out:write("\n")
    total = total + GuildSystem.getLevelCost(L)
end
out:close()
