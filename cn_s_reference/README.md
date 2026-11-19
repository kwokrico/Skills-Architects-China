# Mainland statutory reference (`cn_s_reference`)

Architect critical summaries for the laws and national standards the skill suite cites.

Each `summaries/*_CS.md` file is an original digest: scope, what the architect must check, and which `cn-*` skill to load. It is not a copy of the standard or the statute. Confirm editions and clause numbers in the official text before submission.

Local DB / DGJ / DBJ editions are not in this library. Title-level planning rules for Beijing, Shanghai, Shenzhen, Guangzhou, Chengdu, and Hangzhou are indexed in `MNR/summaries/City_Planning_Technical_Rules_CS.md`. Instruments whose full text is still missing are listed in `mainland-architect-master/references/cn-statutory-source-register.md`. If a binding local conclusion needs a city edition that is not ingested, the master skill halts and asks for that edition.

Regenerate the inventory with `python scripts/build_cn_cs_inventory.py`.
