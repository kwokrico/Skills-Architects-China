# Statutory source register

Collection list for instruments the suite must not number from memory. A row here is not a clause. Saved official copies, retrieved 2026-11-19, are listed in [CATALOG.md](../../reference/statutory-sources/CATALOG.md). A digest remains an original routing note. Quote a number only when that digest records it, and name the edition.

Abbreviations: GB is Guobiao (国家标准, national standard); GB/T is a recommended national standard (推荐性国家标准); JGJ is a Ministry of Housing and Urban-Rural Development (住房和城乡建设部) professional standard (行业标准); DB, DGJ, and DBJ are local standards (地方标准). MOHURD is that ministry.

Practice cities already routed by the suite: Beijing, Shanghai, Shenzhen, Guangzhou, Chengdu, Hangzhou. Their planning rules are in tranche D. Do not reuse one city's number in another city.

The egress calculator is unchanged. `egress_gb50016` stays a geometric pre-check until a GB 50016 digest actually contains the travel-distance tables and those tables have been read against `scripts/config/egress_rules.json`.

## Tranche A — architect drawing decisions

| Instrument | Status | Owner |
|---|---|---|
| GB 55038-2025 住宅项目规范. MOHURD Announcement 2025 No. 39, issued 2025-03-13, in force 2025-05-01. [Announcement](https://www.mohurd.gov.cn/gongkai/zc/wjk/art/2025/art_66adac27fa2144bb86f98fe4c297efd6.html). Local copies: [announcement](../../reference/statutory-sources/mohurd/gb-55038-2025-announcement.html), [code PDF](../../reference/statutory-sources/mohurd/gb-55038-2025-residential-project-code.pdf) | Announcement and code PDF saved 2026-11-19. Code articles are not copied into the digest. [GB_55038_2025_Residential_CS.md](../../cn_s_reference/MOHURD/summaries/GB_55038_2025_Residential_CS.md). Catalog: [CATALOG.md](../../reference/statutory-sources/CATALOG.md) | `cn-building-codes`, `cn-building-programming`, `cn-daylighting-design`, `cn-acoustic-design` |
| GB 50016-2014（2018年版）建筑设计防火规范, read with the GB 55037 repeal list | Relationship note only. Tables are not stored. [GB_50016_Fire_Code_Relationship_CS.md](../../cn_s_reference/Fire%20and%20Rescue/summaries/GB_50016_Fire_Code_Relationship_CS.md). Announcement saved: [GB 55037](../../reference/statutory-sources/mohurd/gb-55037-2022-announcement.html) ([official URL](https://www.mohurd.gov.cn/gongkai/zc/wjk/art/2023/art_17339_770016.html)). The full-code attachment was not downloaded | `cn-fire-life-safety` |
| GB 50084 自动喷水灭火系统设计规范 | Not ingested. Mandatory floor remains GB 55036 | `cn-fire-life-safety` |
| GB 50974 消防给水及消火栓系统技术规范 | Not ingested | `cn-building-services`, `cn-fire-life-safety` |
| GB 50116 火灾自动报警系统设计规范 | Not ingested | `cn-building-services`, `cn-fire-life-safety` |
| GB 50067 汽车库、修车库、停车场设计防火规范 | Not ingested | `cn-fire-life-safety` |
| GB 50222 建筑内部装修设计防火规范 | Not ingested | `cn-fire-life-safety`, `cn-minor-works` |
| GB 8624 建筑材料及制品燃烧性能分级 | Not ingested | `cn-material-selection`, `cn-building-envelope` |
| GB 50033 建筑采光设计标准 | Not ingested. GB 55016 is the floor. GB 55038 announcement repeals GB 50033-2013 clause 4.0.1 | `cn-daylighting-design` |
| GB 50118 民用建筑隔声设计规范 | Not ingested. GB 55016 is the floor. GB 55038 announcement repeals GB 50118-2010 clauses 4.2.1, 4.2.2, and 4.2.5 | `cn-acoustic-design` |
| GB 55025-2022 宿舍、旅馆建筑项目规范 | Title recorded from the published full-text mandatory series. The MOHURD announcement was not opened here. Confirm it before quoting a hotel or dormitory area | `cn-building-programming`, `cn-building-typology` |
| 办公建筑设计标准, cited elsewhere as JGJ/T 67-2019 | Edition not confirmed as still current. Do not quote an office area | `cn-building-programming` |
| 中小学校设计规范, commonly GB 50099 | Edition not confirmed. Do not quote a school area | `cn-building-programming` |
| 综合医院建筑设计规范, commonly GB 51039 | Edition not confirmed. Do not quote a hospital area | `cn-building-programming` |
| GB 50096-2011 住宅设计规范 | Do not use as the residential floor. The GB 55038 announcement repeals named mandatory clauses. Open that announcement before using any remaining clause | `cn-building-programming` |
| 建质函〔2016〕247号 建筑工程设计文件编制深度规定（2016年版）, in force 2017-01-01, replaces the 2008 edition. [Notice](https://www.mohurd.gov.cn/gongkai/zc/wjk/art/2016/art_17339_229701.html). Local copies: [notice](../../reference/statutory-sources/mohurd/jianzhihan-2016-247-notice.html), [depth document](../../reference/statutory-sources/mohurd/jianzhihan-2016-247-design-file-depth.doc) | Notice and attachment saved 2026-11-19. The attachment is a legacy Word file. Drawing-list articles are not copied into the digest. [Design_File_Depth_Provisions_CS.md](../../cn_s_reference/MOHURD/summaries/Design_File_Depth_Provisions_CS.md) | `cn-construction-documentation`, `cn-deliverables-workstages` |
| 建质函〔2016〕287号 装配式混凝土结构建筑工程施工图设计文件技术审查要点 | Not ingested | `cn-mic-dfma`, `cn-construction-documentation` |
| 装配式建筑评价标准, commonly GB/T 51129 | Edition not confirmed | `cn-mic-dfma` |
| 装配式混凝土建筑技术标准, commonly GB/T 51231 | Edition not confirmed | `cn-mic-dfma` |

Smoke control is already digested: GB 51251. Do not collect it again.

## Tranche B — specialist floors

Bring the mandatory general code before the older detailed standard. Each general-code announcement's repeal list is part of the source. None of the GB or JGJ texts below are stored. The seismic administration regulation page is saved.

| Instrument | Status | Owner |
|---|---|---|
| GB 55001-2021 工程结构通用规范 | Not ingested. In force 2022-01-01 on the published series list. Confirm the announcement | `cn-structural-systems` |
| GB 55002-2021 建筑与市政工程抗震通用规范 | Not ingested. Same | `cn-structural-systems` |
| GB 50011 建筑抗震设计规范 | Not ingested. Sits under GB 55002 where they conflict | `cn-structural-systems` |
| JGJ 3 高层建筑混凝土结构技术规程 | Not ingested | `cn-structural-systems` |
| 超限高层建筑工程抗震设防专项审查技术要点 | Not ingested. Confirm the current MOHURD edition | `cn-structural-systems` |
| 《建设工程抗震管理条例》, State Council Order No. 744, in force 2021-09-01. [Text](https://www.gov.cn/zhengce/zhengceku/2021-08/04/content_5629341.htm). Local copy: [HTML](../../reference/statutory-sources/state-council/seismic-administration-regulation-order-744.html) | Statute digest, no article paste. Page saved 2026-11-19. [Seismic_Administration_Regulation_CS.md](../../cn_s_reference/MOHURD/summaries/Seismic_Administration_Regulation_CS.md) | `cn-structural-systems` |
| GB 55003-2021 建筑与市政地基基础通用规范 | Not ingested | `cn-structural-systems` |
| GB 50007 建筑地基基础设计规范 | Not ingested. Sits under GB 55003 | `cn-structural-systems` |
| GB 55008-2021 混凝土结构通用规范 | Not ingested. In force 2022-04-01 on the published series list | `cn-structural-systems` |
| GB 50010 concrete design standard | Not ingested. Confirm the title on the cover. Sits under GB 55008 | `cn-structural-systems` |
| GB 55006-2021 钢结构通用规范 | Not ingested. Collect only when the project is steel | `cn-structural-systems` |
| GB 55021-2021 既有建筑鉴定与加固通用规范 | Not ingested. Confirm the announcement | `cn-alterations-additions` |
| GB 55022-2021 既有建筑维护与改造通用规范 | Not ingested. Confirm the announcement | `cn-alterations-additions` |
| GB 55020-2021 建筑给水排水与节水通用规范 | Not ingested. In force 2022-04-01 | `cn-building-services` |
| GB 55024-2022 建筑电气与智能化通用规范 | Not ingested. Confirm the announcement | `cn-building-services` |
| GB 50015 建筑给水排水设计标准 | Not ingested. Under GB 55020 | `cn-building-services` |
| GB 50736 民用建筑供暖通风与空气调节设计规范 | Not ingested | `cn-building-services` |
| GB 50034 建筑照明设计标准 | Not ingested | `cn-building-services` |
| GB 51348 民用建筑电气设计标准 | Not ingested. Under GB 55024 | `cn-building-services` |
| JGJ 26 severe-cold and cold residential energy | Not ingested. Under GB 55015, which is already digested | `cn-building-sustainability` |
| JGJ 134 hot-summer cold-winter residential energy | Not ingested. Under GB 55015 | `cn-building-sustainability` |
| JGJ 75 hot-summer warm-winter residential energy | Not ingested. Under GB 55015 | `cn-building-sustainability` |
| GB/T 51350 near-zero energy buildings | Not ingested. A target above GB 55015, not a substitute | `cn-building-sustainability` |
| JGJ 102 玻璃幕墙工程技术规范 | Not ingested | `cn-building-envelope` |
| JGJ 133 金属与石材幕墙工程技术规范 | Not ingested | `cn-building-envelope` |
| GB/T 21086 建筑幕墙 | Not ingested. Facade fire class still comes from GB 55037 and GB 8624 | `cn-building-envelope` |
| 《中华人民共和国人民防空法》 and GB 50038 人民防空地下室设计规范 | Not ingested. Collect only for a civil-defence basement. This is not GB 55038 | `cn-building-codes` |

GB 50009 actions, GB 50176 climate zones, GB 50189, and GB/T 50378 already have digests. Do not collect them again.

## Tranche C — land, heritage, procurement, cost

These do not set a plan dimension. Contract interpretation still stops and goes to counsel.

| Instrument | Status | Owner |
|---|---|---|
| 《中华人民共和国土地管理法》, 2019 amendment in force 2020-01-01. [NPC text](http://www.npc.gov.cn/npc/c2/c30834/201909/t20190905_300663.html). Local copy: [HTML](../../reference/statutory-sources/npc/land-administration-law-2019.html) | Statute digest. Page saved 2026-11-19. [Land_Administration_Law_CS.md](../../cn_s_reference/MNR/summaries/Land_Administration_Law_CS.md) | `cn-lease-compliance` |
| 《中华人民共和国城市房地产管理法》, same 2019 amendment, in force 2020-01-01. [NPC text](http://www.npc.gov.cn/npc/c2/c30834/201909/t20190905_300665.html). Local copy: [HTML](../../reference/statutory-sources/npc/urban-real-estate-law-2019.html) | Statute digest. Page saved 2026-11-19. [Urban_Real_Estate_Law_CS.md](../../cn_s_reference/MNR/summaries/Urban_Real_Estate_Law_CS.md) | `cn-lease-compliance` |
| 《历史文化名城名镇名村保护条例》, State Council Order No. 524, in force 2008-07-01. [2008 text](https://www.gov.cn/zhengce/2008-04/29/content_2602508.htm). Local copy: [HTML](../../reference/statutory-sources/state-council/historic-city-protection-regulation-order-524.html) | Statute digest. Page saved 2026-11-19. Confirm a later consolidation before citing an article. [Historic_City_Protection_Regulation_CS.md](../../cn_s_reference/NCHA/summaries/Historic_City_Protection_Regulation_CS.md) | `cn-heritage-conservation` |
| 《房屋建筑和市政基础设施项目工程总承包管理办法》, 建市规〔2019〕12号, in force 2020-03-01. [Text](https://www.gov.cn/zhengce/zhengceku/2019-12/31/content_5465928.htm). Local copy: [HTML](../../reference/statutory-sources/state-council/epc-measures-jianshigui-2019-12.html) | Measures digest. Page saved 2026-11-19. [EPC_Measures_CS.md](../../cn_s_reference/MOHURD/summaries/EPC_Measures_CS.md) | `cn-procurement-strategy` |
| GB/T 50500 建设工程工程量清单计价标准 | Announcement saved 2026-11-19: [HTML](../../reference/statutory-sources/mohurd/gbt-50500-2024-announcement.html) ([official URL](https://www.mohurd.gov.cn/gongkai/zc/wjk/art/2024/art_6186304e164c4c4982904f8734983235.html)). It states GB/T 50500-2024, in force 2025-09-01. The standard PDF was not downloaded. No measurement rule is in the digest. [GB_T_50500_Bill_of_Quantities_CS.md](../../cn_s_reference/MOHURD/summaries/GB_T_50500_Bill_of_Quantities_CS.md) | `cn-cost-consultancy` |
| GF-2017-0201 建设工程施工合同（示范文本） | Not ingested. Model contract, not a statute. Confirm the GF number before quoting a clause | `cn-tender-contract-administration` |
| GF-2020-0216 建设项目工程总承包合同（示范文本） | Not ingested. Same | `cn-procurement-strategy`, `cn-tender-contract-administration` |
| 《注册建筑师条例实施细则》 | Not ingested. The ordinance already has a digest. Confirm the current ministry order before citing the rules | `cn-professional-indemnity` |

Skip the Civil Code (民法典). The master skill already sends contract interpretation to counsel.

## Tranche D — six practice cities

The suite's city keys are `beijing`, `shanghai`, `shenzhen`, `guangzhou`, `chengdu`, and `hangzhou`. Title-level digest: [City_Planning_Technical_Rules_CS.md](../../cn_s_reference/MNR/summaries/City_Planning_Technical_Rules_CS.md). No plot ratio, sunlight hour, or parking ratio is copied there.

For each city, sunlight, parking, plot ratio (容积率), site coverage (建筑密度), and green ratio (绿地率) are read first from the named technical rules, then from that project's regulatory plan (控规) and land-grant conditions (出让条件). A separate local building standard (DB, DGJ, DBJ, or SJG) is still not ingested. Ask for the edition named on the drawing-review opinion.

Local green-building rules, prefabrication-rate policy, and local fire-review rules were not identified as a single current document in this pass. Ask the municipal housing bureau and the fire-review window.

Per project, still required and not a library item: the land-grant contract, the planning conditions, the red-line drawing, and any drawing-review opinion.

| City | Planning instrument to open | Local building series still missing |
|---|---|---|
| Beijing | 北京地区建设工程规划设计通则（试行）, 市规发〔2003〕514号. The municipal planning and natural-resources commission said on 2020-07-27 that it remains in force, except where a later business-environment or approval-reform document governs. Local copies: [notice](../../reference/statutory-sources/cities/beijing/2020-07-27-tongze-still-in-force-notice.html), [通则 PDF](../../reference/statutory-sources/cities/beijing/shiguifa-2003-514-tongze.pdf), and the attached [2018 repeal notice](../../reference/statutory-sources/cities/beijing/jingguizifa-2018-11-repeal-notice.pdf). [Official notice](https://ghzrzyw.beijing.gov.cn/zhengwuxinxi/zcwj/qtwj/202409/t20240911_3864639.html) | DB11 |
| Shanghai | 上海市城市规划管理技术规定（土地使用、建筑管理）. Shanghai Government Order No. 12 (2003), amended and reissued under Order No. 52 (2010). Covers capacity, spacing, setback, height, greenery, and parking. Local copy: [HTML](../../reference/statutory-sources/cities/shanghai/planning-technical-rules-land-and-building.html). [Official text](https://ghzyj.sh.gov.cn/nw2522/20231011/cae7434a8d4f4323a0dadfe0dd881421.html). An application interpretation was reissued on 2023-09-26 and was not downloaded | DGJ08 / DG/TJ08 |
| Shenzhen | 深圳市城市规划标准与准则（修订汇总版）, notice dated 2025-11-03. [Notice](http://pnr.sz.gov.cn/gkmlpt/content/12/12471/post_12471240.html) returned HTTP 403. Page failed. Not saved | SJG |
| Guangzhou | 广州市城乡规划技术规定. Guangzhou Government Order No. 71 (2012), third revision Order No. 168 (2019). Local copy: [HTML](../../reference/statutory-sources/cities/guangzhou/urban-rural-planning-technical-rules.html). [Official text](https://ghzyj.gz.gov.cn/sjb/zw/zcfg/content/post_9466527.html) | Guangdong DBJ |
| Chengdu | 成都市城市规划管理技术规定（2024）, approved by 成府函〔2024〕41号 on 2024-06-15. Obtain the text from the Chengdu planning and natural-resources bureau. A later supplement was seen only as a consultation draft with a blank effective date. Do not apply that draft | Sichuan / Chengdu DB |
| Hangzhou | 杭州市城市规划管理技术规定, issued by the Hangzhou planning and natural-resources bureau on 2026-02-05. Local copies: [gazette HTML](../../reference/statutory-sources/cities/hangzhou/2026-02-05-planning-technical-rules.html), [PDF](../../reference/statutory-sources/cities/hangzhou/2026-02-05-planning-technical-rules.pdf). [Official gazette](https://zfgb.hangzhou.gov.cn/11/102220263/t112220263024/530195.shtml). It applies to the urban built-up area; counties may use it as a reference | Zhejiang / Hangzhou DB |

## What is not a source

A WeChat summary, a training-centre comparison table, or a 图集 (standard atlas, 标准图集) used as the clause. A PDF with no cover year and no announcement number does not unblock a numeric answer.
