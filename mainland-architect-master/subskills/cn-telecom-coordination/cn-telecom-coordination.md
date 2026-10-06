---
name: cn-telecom-coordination
description: Coordinates in-building telecom rooms and external cable diversions with Mainland carriers. It does not replace the carrier's design or a road-occupation permit.
user-invocable: true
disable-model-invocation: true
---

# Mainland Telecom Coordination

Carrier plant, in-building telecom rooms, and cable diversions. Road occupation and hoarding stay in `cn-traffic-coordination` and `cn-site-establishment`.

## When to Use This Skill

| Question type | This skill | Use instead |
|---------------|------------|-------------|
| Operator rooms, fibre entry, cable diversion | `cn-telecom-coordination` | `cn-site-establishment` |
| 占道 traffic plan | `cn-telecom-coordination` | `cn-traffic-coordination` |
| Structured cabling specification inside the tenant fit-out | `cn-telecom-coordination` | `cn-building-services` |

## 1. Scope — Do Not Conflate

| Topic | Owner |
|-------|--------|
| External duct and fibre in the public road | Carrier and municipal pipeline authority |
| Building entry and telecom room | Architect with the carrier's room standard |
| Landlord riser and tray | Architect / MEP |
| Tenant IT active equipment | Tenant |
| Mobile rooftop stations | Carrier structure; architect checks planning, structure, and facade |
| Road-opening permit | Municipal / traffic authority |

There is no single Hong Kong OFCA licensed-works regime to copy. Name the carrier and the city.

## 2. When It Is Triggered

- Basement or site formation crosses existing ducts.
- A new building needs fibre entry from China Mobile, China Telecom, or China Unicom (confirm which operators the city requires).
- A rooftop or facade base station is in the brief.
- An existing building alteration moves a telecom room.
- The planning permit requires pipeline coordination.

## 3. Coordination Framework

1. Ask the city pipeline platform or the client for existing duct records. Treat drawings without a site survey as incomplete.
2. Send the carrier a room and entry sketch before 施工图 freeze: area, clear height, power, earth, cooling, and fire separation.
3. Record the carrier's written room standard and its date. Standards differ by city and year.
4. Diversion design is the carrier's or a qualified pipeline designer's. The architect shows the spatial reservation.
5. Public-road works need the municipal excavation permit. Sequence them in `cn-site-establishment`.

## 4. Site-Establishment Interface

| Step | Predecessor |
|------|-------------|
| Survey of live cables | Before piling |
| Temporary protection | Before excavation beside a duct |
| Diversion and outage | Carrier window |
| Permanent entry ducts | Before basement waterproofing closes |
| Room fit-out for carrier equipment | Before the carrier's install date |

Do not assume a diversion can happen in the same week as the hoarding.

## 5. Construction Coordination

- Cast-in ducts and sleeves are a structure hold point (`cn-construction-programme`).
- Fire stopping where cables cross a compartment is a fire-strategy item (`cn-fire-life-safety`).
- Rooftop masts need structure, planning height limits, and aviation clearance if the site is under an obstacle-limitation surface (`cn-spatial-planning`).
- As-built duct routes go to the pipeline authority when the city requires it.

## 6. Review Context

审图 may comment on telecom-room fire separation, waterproofing of entry ducts, and electrical capacity. Carrier acceptance of the room is a separate letter. Do not treat one as the other.

## 7. Risk Hotspots

- Records that omit a live fibre.
- Room sized to an old carrier standard.
- Entry duct on the wrong elevation after the massing freeze.
- Base station added after 审图.
- Shared trench with power or gas without the separation the pipeline rule requires. Confirm the city's separation rule; do not invent a millimetre dimension.

## 8. Cross-References

- Mobilisation sequence: `cn-site-establishment`.
- Road opening: `cn-traffic-coordination`.
- MEP trays and power: `cn-building-services`.
- Guide: [cn-telecom-coordination-guide.md](../../references/cn-telecom-coordination-guide.md).

## 9. Output Checklist

- City and carriers named.
- Existing-duct survey status stated.
- Room standard date recorded or requested.
- Diversion versus in-building scope separated.
- Public excavation permit assigned.
- No invented separation distance.

## References

Load from parent `references/` when needed (one hop):

* [compliance.md](../../references/compliance.md) — non-negotiable rules
* [operational.md](../../references/operational.md) — intake and escalation
* [domain_terms.json](../../references/domain_terms.json) — vocabulary
* [templates/](../../references/templates/) — output structures
* [cn-telecom-coordination-guide.md](../../references/cn-telecom-coordination-guide.md) — carrier coordination guide
