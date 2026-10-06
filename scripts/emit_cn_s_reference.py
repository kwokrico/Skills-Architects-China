"""Write the first-tranche cn_s_reference critical summaries and index tables.

Digests are original coordination notes. They do not reproduce standard or statute text.
"""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1] / "cn_s_reference"

DOCS: list[dict[str, str | list[str]]] = [
    {
        "folder": "MOHURD",
        "file": "Construction_Law_CS.md",
        "title": "Construction Law of the People's Republic of China (建筑法)",
        "edition": "Confirm the consolidated text on npc.gov.cn before citing an article",
        "authority": "National People's Congress",
        "overview": "The Construction Law is the primary statute for construction licensing, design and contractor qualifications, construction supervision, and quality. It sits above ministry rules and standards.",
        "topics": [
            "Construction cannot lawfully start merely because drawings exist; a construction permit is required unless a statutory exception applies.",
            "Design and construction must be carried out by qualified parties. An advisory note is not a sealed design.",
            "The owner, designer, contractor, and supervisor have distinct duties. Do not merge them in a checklist.",
            "Quality and safety obligations are statutory. A private contract cannot waive them.",
        ],
        "takeaway": "Name the permit, the qualified design institute, and the sealed 项目负责人 before describing the work as lawful.",
        "skill": "cn-consent-scheduling",
        "source": "https://www.npc.gov.cn/ (search 中华人民共和国建筑法 for the current consolidated text)",
    },
    {
        "folder": "MOHURD",
        "file": "Construction_Quality_Regulation_CS.md",
        "title": "Construction Quality Management Regulation (建设工程质量管理条例)",
        "edition": "State Council regulation; confirm the consolidated text",
        "authority": "State Council",
        "overview": "This regulation allocates quality duties among the owner, survey, design, contractor, and supervisor, and sets minimum warranty periods that a contract must not undercut.",
        "topics": [
            "Design documents must meet mandatory standards. 审图 is the mandatory third-party check of construction drawings for the projects in scope.",
            "The design institute remains responsible for design quality after the contractor is appointed.",
            "Minimum quality-warranty periods (foundation, waterproofing, and other parts) are statutory. Do not quote a number from memory; read the current article.",
            "Completion filing does not replace the quality warranty.",
        ],
        "takeaway": "Separate 审图合格, completion filing, and the statutory warranty. Do not let a contract defect-liability period shorten the statutory warranty.",
        "skill": "cn-cost-consultancy",
        "source": "https://www.gov.cn/ (search 建设工程质量管理条例)",
    },
    {
        "folder": "MOHURD",
        "file": "Construction_Safety_Regulation_CS.md",
        "title": "Construction Work Safety Management Regulation (建设工程安全生产管理条例)",
        "edition": "State Council regulation; confirm the consolidated text",
        "authority": "State Council",
        "overview": "This regulation sets construction-site safety duties. It is the legal neighbour of the hazardous-works rules, not a substitute for the building fire code.",
        "topics": [
            "The contractor is responsible for site safety management. The designer provides information needed to build the design safely.",
            "The owner must not compress the programme in a way that forces unsafe work.",
            "Dangerous divisional works need the special scheme the current catalogue requires.",
            "Building fire strategy (GB 55037) is a different document from the site safety plan.",
        ],
        "takeaway": "Use this digest for site-safety duty allocation. Send compartment and egress questions to the fire general code.",
        "skill": "cn-construction-health-safety",
        "source": "https://www.gov.cn/ (search 建设工程安全生产管理条例)",
    },
    {
        "folder": "MOHURD",
        "file": "Survey_and_Design_Regulation_CS.md",
        "title": "Construction Survey and Design Management Regulation (建设工程勘察设计管理条例)",
        "edition": "State Council regulation; confirm the consolidated text",
        "authority": "State Council",
        "overview": "Governs qualifications, design documents, and changes to approved design. It is the statute behind the rule that construction must follow the design that was reviewed.",
        "topics": [
            "Survey and design must be undertaken by qualified units.",
            "Design changes that affect safety or mandatory standards need a controlled revision, not a site sketch alone.",
            "The owner must not force the designer to breach mandatory standards.",
            "Foreign design participation still needs a qualified domestic design institute where the law requires it. Confirm the current article before advising.",
        ],
        "takeaway": "A site instruction that changes structure, fire, or planning indicators is a design change with a review path, not only a contract variation.",
        "skill": "cn-construction-documentation",
        "source": "https://www.gov.cn/ (search 建设工程勘察设计管理条例)",
    },
    {
        "folder": "MOHURD",
        "file": "Construction_Drawing_Review_Measures_CS.md",
        "title": "Construction Drawing Review Administrative Measures",
        "edition": "Commonly cited as MOHURD Order No. 13 (2013), later amended. Confirm the consolidated order before citing an article.",
        "authority": "Ministry of Housing and Urban-Rural Development",
        "overview": "Requires qualified third-party review of construction drawings for house-building and municipal projects in scope, before a construction permit.",
        "topics": [
            "Review covers compliance with mandatory standards and the approved planning parameters that the rules assign to the reviewer.",
            "A review opinion is not a planning permit and not a construction permit.",
            "Comments must be closed and the revised sheets identified. An oral acceptance is not a qualified certificate.",
            "Later design changes may need a delta review. Ask the review body; do not assume a Hong Kong-style minor-deviation threshold.",
        ],
        "takeaway": "Put 审图合格 on the programme as a predecessor of the construction permit, and keep a comment-response matrix.",
        "skill": "cn-construction-documentation",
        "source": "https://www.mohurd.gov.cn/ (search 施工图设计文件审查管理办法)",
    },
    {
        "folder": "MOHURD",
        "file": "Construction_Permit_CS.md",
        "title": "Construction Permit (施工许可证)",
        "edition": "Administrative measures commonly cited as MOHURD Order No. 18 (2014), later amended. Confirm the consolidated text and the city's checklist.",
        "authority": "Ministry of Housing and Urban-Rural Development; local housing bureau issues the permit",
        "overview": "The construction permit is the legal start of construction for projects in scope. Planning permission and drawing review are predecessors, not substitutes.",
        "topics": [
            "Typical predecessors include a planning permit, qualified construction drawings, appointed contractor and supervisor, and the city's fund and safety filings.",
            "Special-project fire design review, where it applies, is also a predecessor.",
            "Preparatory works that a city allows before the permit must be named in that city's rule. Do not generalise.",
            "A permit is site- and scope-specific. A change of contractor or a major design change can require an update.",
        ],
        "takeaway": "Do not show excavation as started on the day the permit is applied for.",
        "skill": "cn-consent-scheduling",
        "source": "https://www.mohurd.gov.cn/ (search 建筑工程施工许可管理办法)",
    },
    {
        "folder": "MOHURD",
        "file": "Tendering_and_Bidding_Law_CS.md",
        "title": "Tendering and Bidding Law (招标投标法)",
        "edition": "Confirm the consolidated law and the implementing regulation",
        "authority": "National People's Congress",
        "overview": "Requires tendering for the project types and thresholds the law and the State Council catalogue set, including many state-funded works. It governs process fairness, not design quality.",
        "topics": [
            "Confirm whether this client and this contract must be tendered before recommending a negotiated appointment.",
            "The tender documents define the scope. A later drawing that adds scope is a change, not a clarification.",
            "All tenderers receive the same addendum.",
            "Bid-rigging and discriminatory conditions are legal risks. Halt and send them to counsel.",
        ],
        "takeaway": "Ask whether public tendering applies before recommending a direct EPC award.",
        "skill": "cn-procurement-strategy",
        "source": "https://www.npc.gov.cn/ (search 中华人民共和国招标投标法)",
    },
    {
        "folder": "MOHURD",
        "file": "GB_55031_2022_Civil_Buildings_CS.md",
        "title": "GB 55031-2022 Code for Civil Buildings (民用建筑通用规范)",
        "edition": "GB 55031-2022, issued 2022-07-15, in force 2023-03-01. Mandatory general code: every article applies.",
        "authority": "Ministry of Housing and Urban-Rural Development",
        "overview": "Sets the mandatory baseline for civil buildings, including function, area and height definitions, outdoor site, common spaces, and components. Where an older standard conflicts, this code prevails.",
        "topics": [
            "Published structure covers general provisions, basic requirements, building area and height, outdoor site, common spaces (entrances, stairs, lifts, toilets, plant, basements), and components (roof, walls, floors, ceilings, doors and windows, guards, shafts).",
            "Do not copy a stair, guard, or headroom number from GB 50352 or from Hong Kong practice until it is checked against this code.",
            "Area rules here interact with GB/T 50353 and with local 计容 rules. They are not the same document.",
            "Older mandatory clauses in civil-design standards that conflict with this code are no longer the floor.",
        ],
        "takeaway": "Open GB 55031 before quoting a civil-design minimum. Cite the edition on the drawing note.",
        "skill": "cn-building-codes",
        "source": "https://www.mohurd.gov.cn/gongkai/zc/wjk/art/2022/art_17339_767703.html",
    },
    {
        "folder": "MOHURD",
        "file": "GB_50352_Civil_Design_Unified_Standard_CS.md",
        "title": "GB 50352 Standard for Design of Civil Buildings (民用建筑设计统一标准)",
        "edition": "The edition widely used in practice is GB 50352-2019. Confirm on the national standards catalogue before submission.",
        "authority": "Ministry of Housing and Urban-Rural Development",
        "overview": "Recommended unified design standard for civil buildings. It remains useful for topics the general code does not exhaust, but it does not override GB 55031.",
        "topics": [
            "Use it after GB 55031, not instead of GB 55031.",
            "Typology standards (residential, school, hospital, office) still add their own rules.",
            "Do not treat a GB 50352 figure as mandatory if GB 55031 states a different requirement.",
        ],
        "takeaway": "Cite GB 55031 as the mandatory floor and GB 50352 as the detailed standard where it does not conflict.",
        "skill": "cn-building-codes",
        "source": "https://openstd.samr.gov.cn/ (search GB 50352)",
    },
    {
        "folder": "MOHURD",
        "file": "GB_T_50353_Building_Area_CS.md",
        "title": "GB/T 50353 Calculation Code for Construction Area (建筑工程建筑面积计算规范)",
        "edition": "GB/T 50353-2013 is the edition commonly cited. Confirm whether a newer edition is in force before measurement.",
        "authority": "Ministry of Housing and Urban-Rural Development",
        "overview": "Defines how construction area is calculated. Planning 计容 area is a separate local rule and can exclude spaces that still count as construction area.",
        "topics": [
            "State whether the schedule is construction area, 计容 area, or internal usable area.",
            "Balconies, voids, equipment floors, and refuge floors need the rule and the city's planning note, not a Hong Kong exemption list.",
            "GB 55031 also contains area provisions. If they differ, the mandatory general code prevails.",
            "The suite calculator `building_area_gbt50353` is a pre-check, not a submission schedule.",
        ],
        "takeaway": "Label every area column with its rule. Do not add a 计容 column without the city's rule.",
        "skill": "cn-architect-calculator",
        "source": "https://openstd.samr.gov.cn/ (search GB/T 50353)",
    },
    {
        "folder": "MOHURD",
        "file": "GB_T_50326_Project_Management_CS.md",
        "title": "GB/T 50326 Code for Construction Project Management (建设工程项目管理规范)",
        "edition": "GB/T 50326-2017 is the edition commonly cited. Confirm the catalogue before treating it as the project manual.",
        "authority": "Ministry of Housing and Urban-Rural Development",
        "overview": "Recommended national project-management code. It is not a permit system and it does not replace the client's appointment or GB/T 50326's own limits.",
        "topics": [
            "Use it to structure the delivery plan: organisation, programme, cost, quality, safety, information, and closeout.",
            "It does not appoint the architect as 监理 or as contract administrator.",
            "Stage names in a private plan of work must still be mapped to 方案, 初设, 施工图, construction, and acceptance.",
        ],
        "takeaway": "Map the project manual to this code's topics, then to the statutory stages. Do not cite it as a permit.",
        "skill": "cn-project-management",
        "source": "https://openstd.samr.gov.cn/ (search GB/T 50326)",
    },
    {
        "folder": "MOHURD",
        "file": "GB_55015_2021_Energy_CS.md",
        "title": "GB 55015-2021 General Code for Energy Efficiency and Renewable Energy (建筑节能与可再生能源利用通用规范)",
        "edition": "GB 55015-2021, issued 2021-09-08, in force 2022-04-01. Mandatory general code.",
        "authority": "Ministry of Housing and Urban-Rural Development",
        "overview": "Mandatory baseline for energy efficiency of new buildings and for renewable-energy systems, plus retrofit and construction acceptance of those measures. It prevails over conflicting older energy standards, including conflicting mandatory clauses of GB 50189.",
        "topics": [
            "Envelope, HVAC, electrical, and plumbing energy measures are in scope, not only the architect's window-to-wall sketch.",
            "Climate-zone tables in the code control the limits. Do not reuse a Hong Kong OTTV number.",
            "Renewable systems (solar, ground-source, air-source) have their own sections. Do not claim a system is 'required' without the article.",
            "Green-building stars (GB/T 50378) are a rating above this floor, not a substitute for it.",
        ],
        "takeaway": "Freeze climate zone and envelope strategy against GB 55015 before value-engineering the facade.",
        "skill": "cn-building-sustainability",
        "source": "https://www.mohurd.gov.cn/ (search GB 55015-2021)",
    },
    {
        "folder": "MOHURD",
        "file": "GB_55030_2022_Waterproofing_CS.md",
        "title": "GB 55030-2022 General Code for Waterproofing (建筑与市政工程防水通用规范)",
        "edition": "GB 55030-2022. Mandatory general code. Confirm the in-force date on the ministry announcement.",
        "authority": "Ministry of Housing and Urban-Rural Development",
        "overview": "Mandatory waterproofing baseline for buildings and municipal works. It prevails where older waterproofing standards conflict.",
        "topics": [
            "Roof, basement, bathroom, and podium waterproofing grades are code questions. Do not invent an upstand height.",
            "The architectural detail, the structural joint, and the landscape level must use the same grade.",
            "A product warranty is not compliance with this code.",
        ],
        "takeaway": "State the waterproofing grade from the code before drawing a generic upstand.",
        "skill": "cn-building-envelope",
        "source": "https://www.mohurd.gov.cn/gongkai/zc/wjk/art/2022/art_17339_768499.html",
    },
    {
        "folder": "MOHURD",
        "file": "GB_55016_2021_Building_Environment_CS.md",
        "title": "GB 55016-2021 General Code for Building Environment (建筑环境通用规范)",
        "edition": "GB 55016-2021, issued 2021-09-08, in force 2022-04-01. Mandatory general code.",
        "authority": "Ministry of Housing and Urban-Rural Development",
        "overview": "Mandatory floor for sound, light, thermal performance, and indoor air quality in civil buildings and in auxiliary offices of industrial buildings. Process rooms, explosion protection, and disaster conditions are outside its stated scope.",
        "topics": [
            "Acoustic design, daylight, insulation, and indoor air each have mandatory outcomes. Specialist reports must meet this floor.",
            "It does not set the fire strategy and it does not replace GB 55015 for energy.",
            "Existing-building alterations should meet the floor unless an objective constraint is documented.",
        ],
        "takeaway": "Split environment questions: sound and light to this code, energy to GB 55015, fire to GB 55037.",
        "skill": "cn-acoustic-design",
        "source": "https://www.mohurd.gov.cn/ (announcement 2021 No. 172, GB 55016-2021)",
    },
    {
        "folder": "MOHURD",
        "file": "Barrier_Free_Environment_Law_CS.md",
        "title": "Barrier-Free Environment Construction Law (无障碍环境建设法)",
        "edition": "Adopted 2023. Confirm the in-force date and consolidated text on npc.gov.cn.",
        "authority": "National People's Congress",
        "overview": "National law requiring barrier-free buildings, roads, transport, and information. Design compliance is still demonstrated through GB 55019 and the detailed access standard.",
        "topics": [
            "New civil public buildings and many renovations are in scope. Confirm the article for the project type.",
            "The law does not replace GB 55019's technical articles.",
            "Information accessibility (signage, announcements) can be in scope as well as ramps and toilets.",
        ],
        "takeaway": "Treat access as a legal duty plus a general-code check, not as an optional green credit.",
        "skill": "cn-accessibility-design",
        "source": "https://www.npc.gov.cn/ (search 无障碍环境建设法)",
    },
    {
        "folder": "MOHURD",
        "file": "GB_55019_2021_Accessibility_CS.md",
        "title": "GB 55019-2021 General Code for Accessibility (建筑与市政工程无障碍通用规范)",
        "edition": "GB 55019-2021, ministry announcement 2021 No. 174, in force 2022-04-01. Mandatory general code.",
        "authority": "Ministry of Housing and Urban-Rural Development",
        "overview": "Mandatory access floor for buildings and municipal works. It prevails over conflicting mandatory clauses of older access standards, including GB 50763.",
        "topics": [
            "Routes, entrances, ramps, lifts, toilets, and municipal paths are in scope.",
            "GB 50763 remains the detailed recommended standard where it does not conflict.",
            "Do not quote a slope, a clear width, or a turning circle from memory.",
        ],
        "takeaway": "Check GB 55019 first, then GB 50763 for detail that does not conflict.",
        "skill": "cn-accessibility-design",
        "source": "https://www.gov.cn/zhengce/zhengceku/2022-03/30/content_5682480.htm",
    },
    {
        "folder": "MOHURD",
        "file": "GB_50763_Accessibility_Detail_CS.md",
        "title": "GB 50763 Codes for Accessibility Design (无障碍设计规范)",
        "edition": "Confirm the current edition on the standards catalogue. GB 55019 prevails on conflict.",
        "authority": "Ministry of Housing and Urban-Rural Development",
        "overview": "Detailed access design standard used for dimensions and arrangements that the general code does not fully draw.",
        "topics": [
            "Use it for detail after the mandatory floor is identified.",
            "A detail that contradicts GB 55019 is not acceptable because it 'follows GB 50763'.",
            "Residential, school, and transport codes may add stricter rules.",
        ],
        "takeaway": "Cite both codes in the access note, and say which one governs if they differ.",
        "skill": "cn-accessibility-design",
        "source": "https://openstd.samr.gov.cn/ (search GB 50763)",
    },
    {
        "folder": "MNR",
        "file": "Urban_Rural_Planning_Law_CS.md",
        "title": "Urban and Rural Planning Law (城乡规划法)",
        "edition": "2007 law, later amended. Confirm the consolidated text.",
        "authority": "National People's Congress; administered by natural-resources authorities",
        "overview": "Legal basis for the planning system, planning permits, and enforcement against works that breach a permit. Territorial spatial planning is the current policy frame; the statute still uses urban-rural planning permits.",
        "topics": [
            "Construction needs the planning permit the law requires for that project. A land contract is not the permit.",
            "Changing use, height, or density after permission can require an amendment.",
            "Works built against the permit are an enforcement risk (`cn-unauthorised-building-works`).",
            "A traffic study, if required, is evidence inside this permit path, not a separate building permit.",
        ],
        "takeaway": "Do not design to a brochure FAR. Read the statutory plan and the permit.",
        "skill": "cn-spatial-planning",
        "source": "https://www.npc.gov.cn/ (search 中华人民共和国城乡规划法)",
    },
    {
        "folder": "MNR",
        "file": "Regulatory_Plan_and_Land_Grant_CS.md",
        "title": "Regulatory Plan and Land-Grant Conditions (控规与出让条件)",
        "edition": "Site-specific. There is no national plot-ratio table.",
        "authority": "Local natural-resources bureau; land contract with the land authority",
        "overview": "Development intensity for a plot is set by the regulatory detailed plan and the state-owned land-grant or allocation contract, then by the planning permit.",
        "topics": [
            "Read 容积率, 建筑密度, 绿地率, 限高, setbacks, use, and 日照 together.",
            "用地红线 and 建筑红线 are different lines.",
            "A sales brochure or a masterplan sketch does not amend the grant.",
            "If the city is unknown, stop at the national process and request the plan extract.",
        ],
        "takeaway": "A massing conclusion without the 控规 extract and the land contract is incomplete.",
        "skill": "cn-lease-compliance",
        "source": "Local 控规 gazette and the executed 出让合同 (no single national URL)",
    },
    {
        "folder": "MNR",
        "file": "Planning_Permits_CS.md",
        "title": "Planning Permits (规划许可)",
        "edition": "City procedure under the Urban and Rural Planning Law",
        "authority": "Natural-resources / planning bureau",
        "overview": "Typical permits are the land-use planning permit and the project planning permit, plus the rural construction planning permit where that regime applies. Cities have merged some windows; the legal effect still has to be checked locally.",
        "topics": [
            "方案 approval and the planning permit are not the construction permit.",
            "Permit drawings control site plan, height, and use. Later 施工图 must match them or amend them.",
            "Conditions (traffic, heritage, aviation, education) are predecessors, not advice.",
        ],
        "takeaway": "File the permit drawing revision that 施工图 will follow. Do not let the two sets drift.",
        "skill": "cn-spatial-planning",
        "source": "https://www.npc.gov.cn/ (城乡规划法 permit articles) and the city's planning window",
    },
    {
        "folder": "MNR",
        "file": "Planning_Verification_CS.md",
        "title": "Planning Verification (规划核实)",
        "edition": "City procedure at completion",
        "authority": "Natural-resources / planning bureau",
        "overview": "Before or as part of completion filing, the as-built building is checked against the planning permit: position, height, use, and the area rules the city uses.",
        "topics": [
            "As-built surveys must use the same red lines as the permit.",
            "A contract practical-completion certificate does not prove planning compliance.",
            "Area discrepancies against 计容 rules are a common failure. Reconcile GB/T 50353 schedules with the city's 计容 sheet.",
        ],
        "takeaway": "Start the verification drawing set before the last facade panel, not after handover.",
        "skill": "cn-certificate-of-compliance",
        "source": "City natural-resources completion guide (no single national form)",
    },
    {
        "folder": "Fire and Rescue",
        "file": "Fire_Protection_Law_CS.md",
        "title": "Fire Protection Law (消防法)",
        "edition": "Confirm the consolidated text. A major revision took effect in 2021; later amendments may exist.",
        "authority": "National People's Congress",
        "overview": "Requires fire-safe design and construction and sets the acceptance or filing duty for completed projects. Technical numbers are in the fire general codes, not in the law.",
        "topics": [
            "Design must conform to national fire technical standards.",
            "The law distinguishes projects that need fire design review and acceptance from projects that file and may be sampled. The ministry rule states the operational split.",
            "Using the building before the required acceptance or filing is an enforcement risk.",
            "Hong Kong FSD certificates are not evidence under this law.",
        ],
        "takeaway": "Cite the Fire Protection Law for the duty, and GB 55037 plus the ministry rule for the procedure.",
        "skill": "cn-fire-life-safety",
        "source": "https://www.npc.gov.cn/ (search 中华人民共和国消防法)",
    },
    {
        "folder": "Fire and Rescue",
        "file": "Fire_Design_Review_and_Acceptance_Provisions_CS.md",
        "title": "Interim Provisions on Fire Design Review and Acceptance",
        "edition": "MOHURD Order No. 51, amended by Order No. 58, in force 2023-10-30.",
        "authority": "Ministry of Housing and Urban-Rural Development",
        "overview": "Special construction projects need fire design review and fire acceptance. Other projects use completion filing and classified sampling. Provinces publish the catalogue that splits ordinary and key projects.",
        "topics": [
            "Identify whether the project is a 特殊建设工程 before choosing the path. The order lists the categories; do not guess from height alone without the list.",
            "Special fire design (no national standard, new material, or heritage constraint) needs the extra technical file the order describes, which can include analysis and, for major or high-hazard cases, physical tests.",
            "Other projects file after completion. A complete filing receives a voucher; it is not the same document as a special-project acceptance opinion.",
            "Sampling failure has a rectification path. Do not advise the user to skip filing.",
        ],
        "takeaway": "Split the programme into special-project review/acceptance or other-project filing. Say which one applies.",
        "skill": "cn-fire-acceptance-closeout",
        "source": "https://www.gov.cn/gongbao/2023/issue_10766/202310/content_6909536.html",
    },
    {
        "folder": "Fire and Rescue",
        "file": "GB_55037_2022_Building_Fire_CS.md",
        "title": "GB 55037-2022 General Code for Building Fire Protection (建筑防火通用规范)",
        "edition": "GB 55037-2022, issued 2022-12-27, in force 2023-06-01. Mandatory general code.",
        "authority": "Ministry of Housing and Urban-Rural Development",
        "overview": "Mandatory fire baseline for planning, design, construction, use, and maintenance of buildings, except production and storage of civil explosives. Where GB 50016 or another standard conflicts, this code prevails. The ministry announcement repealed a long list of older mandatory clauses, including many in GB 50016.",
        "topics": [
            "Covers fire safety layout, fire resistance, means of escape, and related building measures at general-code level.",
            "Do not quote travel distance, stair width, or compartment area from an old GB 50016 table until the article is checked against this code.",
            "The suite calculator `egress_gb50016` is a geometric pre-check only. It is not this code.",
            "Fire-service installations are also governed by GB 55036.",
        ],
        "takeaway": "Any fire number in a report must cite GB 55037 if the article lives there, otherwise GB 50016 with a 'no conflict' check.",
        "skill": "cn-fire-life-safety",
        "source": "https://www.mohurd.gov.cn/gongkai/zc/wjk/art/2023/art_17339_770016.html",
    },
    {
        "folder": "Fire and Rescue",
        "file": "GB_50016_Fire_Code_Relationship_CS.md",
        "title": "GB 50016 Code for Fire Protection Design of Buildings — relationship note",
        "edition": "GB 50016-2014 (2018 edition) is the edition commonly in use. Mandatory clauses repealed by the GB 55037 announcement no longer apply.",
        "authority": "Ministry of Housing and Urban-Rural Development",
        "overview": "GB 50016 remains the detailed fire code for provisions that were not repealed and that do not conflict with GB 55037. It is not the Hong Kong Fire Services Code and it is not used alone.",
        "topics": [
            "Read GB 55037 first.",
            "Use GB 50016 for remaining detailed arrangements, still checking the repeal list in the GB 55037 announcement.",
            "Sprinkler and alarm detailed design also sits under the facilities general code and the specialist standards it did not repeal.",
            "Local fire-review guides may be stricter. Ask for the city.",
        ],
        "takeaway": "Do not answer 'what does GB 50016 require?' without stating the GB 55037 override.",
        "skill": "cn-fire-life-safety",
        "source": "https://www.mohurd.gov.cn/gongkai/zc/wjk/art/2023/art_17339_770016.html",
    },
    {
        "folder": "Fire and Rescue",
        "file": "GB_55036_2022_Fire_Facilities_CS.md",
        "title": "GB 55036-2022 General Code for Fire Facilities (消防设施通用规范)",
        "edition": "GB 55036-2022. Mandatory general code. Confirm the in-force date on the ministry announcement.",
        "authority": "Ministry of Housing and Urban-Rural Development",
        "overview": "Mandatory floor for design, installation, acceptance, use, and maintenance of fire facilities. It repealed listed mandatory clauses in older sprinkler, alarm, hydrant, and related standards.",
        "topics": [
            "Facility choice is not only an MEP decision. The building compartment strategy must match the facility set.",
            "Acceptance of the system is a functional test with a pass or fail, not a document-only check.",
            "Do not copy a Hong Kong FSI form as the acceptance record.",
        ],
        "takeaway": "Pair GB 55037 (building) with GB 55036 (facilities) in the fire strategy note.",
        "skill": "cn-building-services",
        "source": "https://www.mohurd.gov.cn/gongkai/zc/wjk/art/2022/art_17339_767704.html",
    },
    {
        "folder": "NCHA",
        "file": "Cultural_Relics_Protection_Law_CS.md",
        "title": "Cultural Relics Protection Law (文物保护法)",
        "edition": "Confirm the consolidated text. A revised law was adopted in 2024; verify the in-force edition.",
        "authority": "National People's Congress; National Cultural Heritage Administration",
        "overview": "Protects designated cultural relics and their protection zones. Construction, including change of use and new building nearby, can require heritage approval before planning or design freeze.",
        "topics": [
            "Identify the protection level and whether the site is inside a protection zone or a construction-control zone.",
            "Approval from the relics authority is separate from ordinary planning permission.",
            "Archaeological finds during excavation stop the work under the law. Build that hold point into the programme.",
        ],
        "takeaway": "Ask for the heritage plan extract before massing a site near an old city core.",
        "skill": "cn-heritage-conservation",
        "source": "https://www.ncha.gov.cn/ and https://www.npc.gov.cn/ (search 文物保护法)",
    },
    {
        "folder": "NCHA",
        "file": "Historic_Building_Interface_CS.md",
        "title": "Historic Buildings and Character Areas — architect interface",
        "edition": "City lists and conservation plans. Not a single national design code.",
        "authority": "Cultural heritage bureau and the planning bureau",
        "overview": "Many cities protect historic buildings and character areas that are not national key relics. The control (facade, height, colour, use) is in the conservation plan or the regulatory plan.",
        "topics": [
            "A 'historic look' is not compliance. Quote the plan's control.",
            "Alteration of a protected building is `cn-alterations-additions` plus this approval.",
            "Fire and access upgrades that cannot meet the national standard may need the special fire-design path. Do not ignore either the heritage control or the fire code.",
        ],
        "takeaway": "Write two columns: heritage control and fire/access floor. Gaps need a formal special-design route, not a silent omission.",
        "skill": "cn-heritage-conservation",
        "source": "City conservation plan (no single national drawing standard)",
    },
    {
        "folder": "MEE",
        "file": "Environmental_Impact_Assessment_Law_CS.md",
        "title": "Environmental Impact Assessment Law (环境影响评价法)",
        "edition": "Confirm the consolidated text and the current classified directory.",
        "authority": "Ministry of Ecology and Environment",
        "overview": "Some construction projects need an EIA report, a form, or a registration before construction. The category depends on the national directory and the local ecology bureau, not on the architect's judgement of 'greenness'.",
        "topics": [
            "Check the directory for the use (industry, hospital, large transport, and others). Ordinary offices are not automatically exempt.",
            "EIA approval, when required, is a programme predecessor.",
            "A green-building star does not replace EIA.",
        ],
        "takeaway": "Ask whether the directory classifies the project before promising a start date.",
        "skill": "cn-building-sustainability",
        "source": "https://www.mee.gov.cn/ (search 环境影响评价法 and the current 分类管理名录)",
    },
    {
        "folder": "MEE",
        "file": "Construction_Dust_and_Noise_Interface_CS.md",
        "title": "Construction Dust and Noise — architect interface",
        "edition": "City rules under national pollution-control laws. Confirm the city's site standards.",
        "authority": "Ecology and environment bureau; urban management where assigned",
        "overview": "Construction dust, wastewater, and noise are site controls. They affect hoarding, working hours, and sometimes facade installation methods.",
        "topics": [
            "Working-hour limits can remove evening concrete or facade works from the programme.",
            "The architect shows site drainage and hoarding that make compliance possible. The contractor operates the controls.",
            "These rules are not the indoor acoustic standard (GB 55016).",
        ],
        "takeaway": "Put the city's construction-noise hours on the programme before promising a floor cycle.",
        "skill": "cn-site-establishment",
        "source": "City ecology or housing-bureau site-environment guide",
    },
    {
        "folder": "CAAC",
        "file": "Airport_Obstacle_Limitation_CS.md",
        "title": "Airport Obstacle Limitation",
        "edition": "Civil Aviation Law and airport obstacle-management rules. Surfaces are airport-specific.",
        "authority": "Civil Aviation Administration of China and the airport",
        "overview": "Height near an airport is limited by obstacle-limitation surfaces and by the 控规. Neither number should be assumed from a national table in this digest.",
        "topics": [
            "Ask whether the site is inside an airport obstacle-protection zone.",
            "A 控规 height that exceeds the aviation surface does not win.",
            "Cranes during construction can breach the surface even if the building does not. Flag temporary works.",
            "Approval is from the aviation authority, not from the planning bureau alone.",
        ],
        "takeaway": "No building height conclusion near an airport without the surface clearance.",
        "skill": "cn-spatial-planning",
        "source": "https://www.caac.gov.cn/ (search 净空保护)",
    },
    {
        "folder": "MEM",
        "file": "Work_Safety_Law_CS.md",
        "title": "Work Safety Law (安全生产法)",
        "edition": "Confirm the consolidated text. The 2021 revision is the baseline many projects still cite; check later amendments.",
        "authority": "National People's Congress; Ministry of Emergency Management",
        "overview": "General work-safety duties for production and business units, including construction enterprises. It sets reporting of accidents and the duty to provide a safe workplace.",
        "topics": [
            "The contractor's principal responsible person carries the site safety duty.",
            "Designers who find a safety problem in the design must propose a correction. Do not leave it as a site RFI with no owner.",
            "Accident reporting thresholds and timelines are in the law and the reporting rules. Do not invent a deadline.",
            "This law is not the building fire code.",
        ],
        "takeaway": "Use this digest for duty and reporting. Use GB 55037 for fire design.",
        "skill": "cn-construction-health-safety",
        "source": "https://www.mem.gov.cn/ and https://www.npc.gov.cn/ (search 安全生产法)",
    },
    {
        "folder": "MEM",
        "file": "Hazardous_Divisional_Works_CS.md",
        "title": "Hazardous Divisional Works (危大工程)",
        "edition": "MOHURD order commonly cited as Order No. 37 (2018) on safety management of hazardous divisional works. Confirm the consolidated text and the current catalogue before citing a height or depth.",
        "authority": "Ministry of Housing and Urban-Rural Development, with emergency-management oversight of accidents",
        "overview": "Certain construction activities (deep excavation, high formwork, scaffolding, cranes, demolition, and others on the catalogue) need a special construction scheme. Activities above a further threshold need an expert argument.",
        "topics": [
            "The catalogue, not this digest, decides whether an activity qualifies. Do not reuse a remembered metre limit.",
            "The scheme is the contractor's document. Expert argument is by the experts the rule requires. The architect does not sign either as approval.",
            "The scheme is a programme predecessor of the activity.",
            "A design change that creates a new dangerous activity reopens the scheme.",
        ],
        "takeaway": "List candidate activities and write 'threshold to be confirmed against the current catalogue'.",
        "skill": "cn-construction-health-safety",
        "source": "https://www.mohurd.gov.cn/ (search 危险性较大的分部分项工程安全管理规定)",
    },
    {
        "folder": "SAMR",
        "file": "Special_Equipment_Safety_Law_CS.md",
        "title": "Special Equipment Safety Law (特种设备安全法)",
        "edition": "Confirm the consolidated text.",
        "authority": "National People's Congress; State Administration for Market Regulation",
        "overview": "Lifts, escalators, and some pressure vessels and boilers are special equipment. They need licensed installation and a use registration or inspection before passengers use them.",
        "topics": [
            "Architectural shaft, pit, headroom, and machine-room sizes must match the product that will be inspected.",
            "Installation inspection is not the building fire acceptance and not practical completion.",
            "A goods hoist used only for construction is a different regime from the permanent passenger lift. Do not mix the certificates.",
        ],
        "takeaway": "Put lift inspection on the acceptance schedule as its own line.",
        "skill": "cn-building-services",
        "source": "https://www.samr.gov.cn/ and https://www.npc.gov.cn/ (search 特种设备安全法)",
    },
    {
        "folder": "SAMR",
        "file": "Lift_Inspection_Interface_CS.md",
        "title": "Lift Inspection — architect interface",
        "edition": "Product and inspection rules under the Special Equipment Safety Law. Confirm the current lift standard edition.",
        "authority": "Market regulation bureau and the licensed inspection body",
        "overview": "The architect coordinates shaft geometry and lobby access. The manufacturer and the inspection body confirm the lift.",
        "topics": [
            "Freeze shaft size with the manufacturer's shop drawing before the shaft walls close.",
            "Accessible lift controls must also meet GB 55019.",
            "Fire-service or evacuation lifts, if required, are a GB 55037 / GB 55036 question plus this inspection.",
        ],
        "takeaway": "Do not issue 'lift complete' because the car is installed. Wait for the inspection record.",
        "skill": "cn-building-services",
        "source": "https://www.samr.gov.cn/ (special equipment lift inspection rules)",
    },
    {
        "folder": "ASC",
        "file": "Registered_Architect_Regulation_CS.md",
        "title": "Registered Architect Regulation (注册建筑师条例)",
        "edition": "State Council regulation. Confirm the consolidated text and the implementing rules.",
        "authority": "State Council; national and local registered-architect boards",
        "overview": "Reserves defined design activities to registered architects and sets the Class 1 and Class 2 practice limits. An unregistered adviser must not present work as sealed design.",
        "topics": [
            "Check whether the project scale requires a Class 1 architect. Do not guess the square-metre or height cut-off; read the current rule.",
            "The seal and the design-institute qualification are both required where the law says so.",
            "This suite's outputs are advisory. They are not a seal.",
        ],
        "takeaway": "State that a registered architect must sign before the document is submitted as design.",
        "skill": "cn-professional-indemnity",
        "source": "https://www.gov.cn/ (search 注册建筑师条例)",
    },
    {
        "folder": "ASC",
        "file": "Architect_Seal_and_Liability_CS.md",
        "title": "Seal, Professional Liability, and Advisory Boundary",
        "edition": "Practice rule. Pair with the Registered Architect Regulation and the design-quality duties.",
        "authority": "Registered-architect administration and the design institute",
        "overview": "Drawings submitted for permit or review carry the institute's qualification and the registered professional's seal. Professional indemnity insurance is contractual, not a substitute for that seal.",
        "topics": [
            "Do not draft a note that says the assistant or the software 'certifies' compliance.",
            "Liability caps in an appointment do not cap statutory design duty.",
            "Cross-border Hong Kong architect seals do not replace Mainland registration.",
        ],
        "takeaway": "Every submission checklist ends with 'seal holder to confirm', not with this digest's conclusion.",
        "skill": "cn-professional-indemnity",
        "source": "https://www.gov.cn/ (search 注册建筑师条例)",
    },
    {
        "folder": "Green Building",
        "file": "GB_T_50378_Green_Building_CS.md",
        "title": "GB/T 50378 Assessment Standard for Green Building (绿色建筑评价标准)",
        "edition": "GB/T 50378-2019 is the widely used edition. A later revision may be in force. Confirm on the catalogue before targeting a star.",
        "authority": "Ministry of Housing and Urban-Rural Development",
        "overview": "Recommended rating standard for one-star, two-star, and three-star green buildings. Mandatory energy, fire, and access floors still apply whether or not a star is targeted.",
        "topics": [
            "A star is a client or planning target. Write the target down before claiming a credit path.",
            "Credits do not relax GB 55015, GB 55016, GB 55019, or GB 55037.",
            "Local green-building rules may require a star for some land grants. Read the grant.",
        ],
        "takeaway": "State the star, the edition, and the mandatory codes that sit underneath it.",
        "skill": "cn-building-sustainability",
        "source": "https://openstd.samr.gov.cn/ (search GB/T 50378)",
    },
    {
        "folder": "Green Building",
        "file": "GB_50189_Public_Building_Energy_CS.md",
        "title": "GB 50189 Design Standard for Energy Efficiency of Public Buildings",
        "edition": "Confirm the current edition. GB 55015-2021 prevails where the two conflict.",
        "authority": "Ministry of Housing and Urban-Rural Development",
        "overview": "Detailed public-building energy standard used where GB 55015 does not replace the provision. Residential energy standards are a different document.",
        "topics": [
            "Identify public versus residential before opening this standard.",
            "Window-to-wall ratio, shading, and plant efficiency are design-team items, not architect-only items.",
            "Do not import Hong Kong OTTV or RTTV limits.",
        ],
        "takeaway": "Cite GB 55015 as the floor and this standard only for the articles that remain applicable.",
        "skill": "cn-building-sustainability",
        "source": "https://openstd.samr.gov.cn/ (search GB 50189)",
    },
]


def render(doc: dict) -> str:
    topics = "\n".join(f"- {item}" for item in doc["topics"])
    return f"""# {doc['title']}

**Architect critical summary for schematic design**

{doc['edition']} | {doc['authority']}

> Scope note: This is an architect's digest for routing and early design. It is not the text of the law or standard. Confirm every number, clause, and edition in the official publication before design, tender, or submission.

## Regulatory Overview

{doc['overview']}

## Critical topics

{topics}

## Schematic-design takeaway

{doc['takeaway']}

## Related skill

`{doc['skill']}`

## Source

{doc['source']}
"""


def write_indexes() -> None:
    by_folder: dict[str, list[dict]] = {}
    for doc in DOCS:
        by_folder.setdefault(str(doc["folder"]), []).append(doc)
    for folder, items in by_folder.items():
        lines = [
            f"# {folder} — document index",
            "",
            "Critical summaries are digests, not the official texts.",
            "",
            "| Document | Summary | Related skill |",
            "|----------|---------|---------------|",
        ]
        for doc in items:
            lines.append(
                f"| {doc['title']} | [summaries/{doc['file']}](summaries/{doc['file']}) | `{doc['skill']}` |"
            )
        lines.append("")
        safe = folder.replace(" ", "_")
        path = ROOT / folder / f"{safe}_Table_English.md"
        path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    for doc in DOCS:
        folder = ROOT / str(doc["folder"]) / "summaries"
        folder.mkdir(parents=True, exist_ok=True)
        (folder / str(doc["file"])).write_text(render(doc), encoding="utf-8")
    write_indexes()
    readme = ROOT / "README.md"
    readme.write_text(
        """# Mainland statutory reference (`cn_s_reference`)

Architect critical summaries for the laws and national standards the skill suite cites.

Each `summaries/*_CS.md` file is an original digest: scope, what the architect must check, and which `cn-*` skill to load. It is not a copy of the standard or the statute. Confirm editions and clause numbers in the official text before submission.

City DB / DGJ packs are not in this tranche. If a binding local conclusion needs a city, the master skill halts and asks for that city.

Regenerate the inventory with `python scripts/build_cn_cs_inventory.py`.
""",
        encoding="utf-8",
    )
    print(f"wrote {len(DOCS)} summaries")


if __name__ == "__main__":
    main()
