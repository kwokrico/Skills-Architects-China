# Independent behavioural evaluation — 2026-11-07

**Final result: 26/26 behavioural cases pass; 10/10 dispatcher tests pass; translation-map JSON schema passes.** The blind runs exposed two procedural failures and conflicting source guidance, corrected and rechecked across the full suite. Raw responses and failed attempts are preserved below.

## Method

Responders were fresh subagents with no inherited conversation (`fork_turns: none`). They received the skill entrypoint and prompt-only case packets, not expected outputs, suspected defects, proposed fixes, or previous responses. They were instructed not to read the repository's evaluation directory, golden questions, diffs, or other response artifacts. Each reported its actual file/tool/source use. Generated responses were first saved outside the repository, then copied here unchanged.

The primary editing agent graded the responses against `../../evals.json` and the golden-question requirements. This separates blind response generation from rubric-based grading; grading itself was not independent of the editor. Isolation was by fresh context and read instructions, not a filesystem access barrier. Cases shared context within each batch, except the final isolated case 1. This is a qualitative regression exercise, not a statistical benchmark or project compliance certification.

## Runs

| Run | Coverage | Responders | Outcome |
|---|---|---|---|
| Baseline | New cases 15–26 | `blind_baseline_a/b/c`, four cases each | 10 pass, 2 partial |
| First full regression | Cases 1–26 | `blind_regression_a/b/c`, 9/9/8 cases | 25 pass, 1 routing failure |
| Second full regression | Case 1 isolated; cases 2–14; cases 15–26 | `blind_final_quick`, `blind_final_original`, `blind_final_new` | 25 pass, 1 required-source-read failure |
| Final full regression | Cases 1–26 | `blind_verified_a/b/c`, 9/9/8 cases | 26 pass |

Baseline partials: case 15 corrected the authority error but omitted the separate opening-check distinction; case 26 gave safe coordination advice without identifying one primary skill. The first full regression failed case 1's master-only quick-reference requirement: its factual answer was acceptable, but it loaded two specialist skills. The isolated second-regression case 1 passes and reads no sub-skills. In that same run, case 12 failed to read the required atlas index despite giving a safe answer. A post-run audit clarification confirmed that the file had not been read; see `atlas-audit-clarification.txt`.

Final cases 1 and 12 meet both the response and source-use requirements. Across the baseline and three full regressions, 12 fresh responder contexts produced 90 case responses. These are repeated qualitative checks, not 90 statistically independent samples.

## Changes supported by the responses

1. **Fire authority and pathway:** Baseline cases 15 and 23 explicitly found that local skill text incorrectly assigned construction fire acceptance to 消防救援局. Corrected the master, glossary, contextual FSD translation, templates, fire-life-safety and closeout instructions. Added authority/pathway sources and distinguished special-project acceptance, other-project filing/spot checks, and public-gathering opening checks. Sources: [MOHURD consolidated provisions, Articles 2–3](https://www.mohurd.gov.cn/gongkai/zc/wjk/art/2023/art_17339_774791.html), [Fire Protection Law, Articles 13 and 15](https://www.beijing.gov.cn/zhengce/zhengcefagui/qtwj/202307/t20230726_3207767.html).
2. **Residential applicability:** Baseline case 16 identified GB 55038-2025, absent from the master. Added applicability/transition reminders and the GB 50033-2013 clause 4.0.1 repeal warning; removed an unqualified typical residential-height shortcut. The expectation for existing case 13 was strengthened before regression, preserving its sunlight/daylight distinction. Source: [MOHURD residential-code announcement](https://www.mohurd.gov.cn/gongkai/zc/wjk/art/2025/art_66adac27fa2144bb86f98fe4c297efd6.html). No numerical design criteria were added.
3. **Mixed-topic routing:** Baseline case 26 did not identify a single primary skill. Clarified compliance-led versus layout-led coordination and explicit secondary routing in the master.
4. **Routine hierarchy routing:** First-regression case 1 loaded specialists unnecessarily. Added an explicit master-only rule for routine code-hierarchy questions; the final rerun isolates this prompt from deeper fire cases.
5. **Imported contract reference:** First-regression cases 4 and 23 identified a leftover HKIA reference in the completion skill. Replaced it with the executed project contract and applicable Mainland requirements.
6. **Atlas evidence read:** Second-regression case 12 omitted the required atlas index. The master and compliance rule now explicitly require opening both the index and the relevant code digest for atlas-as-compliance questions, while retaining the requirement to withhold unverified clauses and check current atlas status externally.

The earlier daylight-table and floor-plate-method fixes predate this independent evaluation and remain in the tested skill. Calculator algorithms were not changed. Runtime numeric defaults remain proxy/model values; cases 2 and 18 test that responses do not promote them to statutory conclusions.

## Evidence and reproducibility

- `baseline-*.md`: original blind responses for new cases.
- `regression-*.md`: first full regression, including the failed routing case.
- `final-*.md`: second full regression responses, including the isolated case 1 and failed source-read case 12. Filenames retain the responders' original names.
- `verified-*.md`: final full regression responses after the atlas-read correction.
- `*-prompts-*.json`: prompt-only packets used for the full regressions.
- `grades.json`: per-case judgments and evidence filenames.
- `skill-manifest.json`: SHA-256 hashes of 133 skill/runtime/reference files for the first full regression.
- `final-skill-manifest.json`: hashes for the second full regression.
- `verified-skill-manifest.json`: hashes after the atlas-read correction, for the final full regression.

All 133 final skill/resource hashes were rechecked after response collection and matched. The report and grading files are outside that source manifest.

### Citation check

The final raw case 1 answer uses a GB 55036 announcement URL ending in `.html37`. A separate source check reproduced that variant in official-domain search results, alongside the [standard announcement URL](https://www.mohurd.gov.cn/gongkai/zc/wjk/art/2022/art_17339_767704.html). It is not attributed to an evaluator-invented citation. The standard URL is supplied here for convenience; the raw transcript remains unchanged. Direct fetching timed out, while official search returned the announcement content.

## Executable checks and limits

- `.venv\Scripts\python.exe -B -m unittest discover -s tests -v`: **10/10 pass** on the final skill revision. Execution used approved escalation because the installed Python is inaccessible from the sandbox.
- PowerShell `Test-Json -SchemaFile .../translation_map.schema.json`: **pass**. Python's optional `jsonschema` package is absent, so the runtime reports skipped schema validation; the separate PowerShell validation covers the edited configuration.
- Evaluation JSON: **26 unique sequential IDs and 26 unique slugs**.
- `git diff --check`: **pass**; Git emitted only line-ending conversion notices.
- Bundled skill quick-validator could not run because Python lacks `yaml`. Frontmatter changes are limited to existing fields; no success claim is made for that validator.
- The first full regression could not download the official GB 55030 attachment. Case 12 correctly withheld an unsupported clause and dimensions. This is an expected uncertainty response, not a successful numerical compliance check.

Official sources were checked for disputed assertions, not exhaustively for every standard in the suite. Missing project inputs remain explicit in the answers. A passing scenario establishes only that the sampled response met its rubric.
