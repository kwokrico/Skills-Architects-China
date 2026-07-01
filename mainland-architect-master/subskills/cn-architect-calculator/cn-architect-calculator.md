---
name: cn-architect-calculator
description: Mainland architect calculators for GB 50016 egress logic, GB/T 50353 building-area aggregation, and planning indicator checks with city-aware disclaimers.
user-invocable: true
disable-model-invocation: true
---

# Mainland Architect Calculator

All calculations use metric units and Mainland baseline standards. If city is missing, output national baseline with a local-amendment disclaimer.

---

## 1. Supported Runtime Calculator Types

| Tool Name | `calc_type` | Purpose |
|---|---|---|
| Egress calculator | `egress_gb50016` | Occupancy-sensitive travel distance and stair recommendation |
| Building area calculator | `building_area_gbt50353` | Countable vs non-countable building area aggregation |
| Layout sorter | `layout_sort` | OCR/layout coordinate sorting utility |

---

## 2. Input Templates

### 2.1 `egress_gb50016`
```json
{
  "length": 20,
  "width": 10,
  "occupancy_type": "office",
  "sprinklered": true,
  "occupant_load": 0
}
```

---

### 2.2 `building_area_gbt50353`
```json
{
  "items": [
    {"area": 1200, "category": "above_ground_main"},
    {"area": 80, "category": "refuge_space"}
  ]
}
```

---

## 3. Egress Calculation Notes

**Proxy limitation:** Runtime `egress_gb50016` uses room diagonal $\sqrt{L^2 + W^2}$ as a travel-distance **pre-check**, not actual route path length. Do not label **Pass** without confirming real egress paths against GB 50016 tables.

**Formulas:**

- Diagonal proxy: $d = \sqrt{L^2 + W^2}$
- Limit $d_{\max}$ from occupancy + sprinkler tables in `scripts/config/egress_rules.json` (GB 50016 baseline)
- Occupant load estimate when not supplied: $N \approx \lfloor A / \rho \rfloor$ with density $\rho$ by occupancy type

- Occupancy type drives load-density and stair-width assumptions.
- Travel distance logic must be checked with sprinkler condition.
- Atypical mixed-use floors should be calculated by functional zone, then consolidated.

---

## 4. Building Area Aggregation Notes

- Use `GB/T 50353` category logic for countable/non-countable area.
- Keep output unit in `m²`, typically two decimals.
- Do not apply HK exempt-GFA assumptions.

---

## 5. Planning Indicator Quick Formulas

```text
容积率 = 计容建筑面积 / 用地面积
建筑密度 = 建筑基底面积 / 用地面积
绿地率 = 绿地面积 / 用地面积
```

Always verify whether local control plan uses additional indicator definitions.

---

## 6. Practical Usage Rules

- Always pass `city_context` to `run_arch_calculator` when known.
- If city unknown, mark results as national baseline for pre-check only.
- Treat calculator output as technical aid; final compliance depends on local审图 and authority interpretation.

---

*Baseline references: GB 50016, GB/T 50353, and local supplements where applicable.*

## When to Use This Skill

| Question type | This skill | Use instead |
|---------------|------------|-------------|
| Egress/area numeric pre-check | `cn-architect-calculator` | `cn-fire-life-safety` |
| Fire strategy narrative | `cn-architect-calculator` | `cn-fire-life-safety` |
| Planning FAR check | `cn-architect-calculator` | `cn-spatial-planning` |
## References

Load from parent `references/` when needed (one hop):

* [compliance.md](../../references/compliance.md) — non-negotiable rules
* [operational.md](../../references/operational.md) — intake and escalation
* [domain_terms.json](../../references/domain_terms.json) — vocabulary
* [templates/](../../references/templates/) — output structures
