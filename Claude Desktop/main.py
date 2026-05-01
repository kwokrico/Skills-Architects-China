import os
import json
import sys
from pathlib import Path

try:
    from jsonschema import Draft202012Validator
except ImportError:
    Draft202012Validator = None

try:
    from core.calculators import run_calculation
except ImportError:
    run_calculation = None


class MainlandArchitectDispatcher:
    def __init__(self):
        self.base_path = os.path.dirname(os.path.abspath(__file__))
        self.sub_skills_base = os.path.join(self.base_path, "sub_skills")
        self.config_base = os.path.join(self.base_path, "config")

        # Optional per-skill filename overrides (defaults assume `sub_skills/<skill_id>/<skill_id>.md`)
        self.skill_file_overrides = {}

        # Discover installed sub-skills (folders are canonical `cn-*` names).
        self.cn_skill_ids = self._discover_cn_skill_ids()

        self.translation_map = {}
        self.translation_status = {"status": "not_loaded"}
        self._load_translation_assets()

    def _discover_cn_skill_ids(self):
        skill_ids = []
        if not os.path.isdir(self.sub_skills_base):
            return skill_ids

        for entry in os.listdir(self.sub_skills_base):
            folder = os.path.join(self.sub_skills_base, entry)
            if not os.path.isdir(folder):
                continue
            if not entry.startswith("cn-"):
                continue
            expected_md = os.path.join(folder, f"{entry}.md")
            if os.path.isfile(expected_md):
                skill_ids.append(entry)

        return sorted(skill_ids)

    def _load_json_file(self, path):
        with Path(path).open("r", encoding="utf-8") as f:
            return json.load(f)

    def _load_translation_assets(self):
        map_path = os.path.join(self.config_base, "translation_map.json")
        schema_path = os.path.join(self.config_base, "translation_map.schema.json")

        if not os.path.exists(map_path) or not os.path.exists(schema_path):
            self.translation_status = {
                "status": "warning",
                "message": "translation_map assets not found in /config",
            }
            return

        try:
            loaded_map = self._load_json_file(map_path)
            loaded_schema = self._load_json_file(schema_path)
            if Draft202012Validator is None:
                self.translation_map = loaded_map
                self.translation_status = {
                    "status": "warning",
                    "message": "jsonschema package not installed; schema validation skipped",
                }
                return

            validator = Draft202012Validator(loaded_schema)
            errors = sorted(validator.iter_errors(loaded_map), key=lambda e: list(e.path))
            if errors:
                top = errors[0]
                loc = ".".join(str(p) for p in top.path) or "<root>"
                self.translation_status = {
                    "status": "error",
                    "message": f"translation_map validation failed at {loc}: {top.message}",
                }
                return

            self.translation_map = loaded_map
            self.translation_status = {"status": "success"}
        except Exception as exc:
            self.translation_status = {
                "status": "error",
                "message": f"translation_map load failed: {str(exc)}",
            }

    def _normalize_skill_id(self, skill_id):
        if not skill_id:
            return None
        if skill_id in self.cn_skill_ids:
            return skill_id

        # Legacy alias: allow `hk-*` IDs to map to canonical `cn-*` skills.
        if skill_id.startswith("hk-"):
            candidate = f"cn-{skill_id[3:]}"
            if candidate in self.cn_skill_ids:
                return candidate

        return None

    def _resolve_skill_file_path(self, canonical_skill_id):
        if canonical_skill_id not in self.cn_skill_ids:
            return None, None

        folder = canonical_skill_id
        default_file = f"{canonical_skill_id}.md"
        filename = self.skill_file_overrides.get(canonical_skill_id) or default_file
        file_path = os.path.join(self.sub_skills_base, folder, filename)
        ref_path = os.path.join(self.sub_skills_base, folder, "references")
        return file_path, ref_path

    def load_sub_skill(self, skill_id):
        canonical_skill_id = self._normalize_skill_id(skill_id)
        if canonical_skill_id is None:
            return {"error": f"Skill ID '{skill_id}' not recognized."}

        file_path, ref_path = self._resolve_skill_file_path(canonical_skill_id)
        if not file_path:
            return {"error": f"Skill file for '{canonical_skill_id}' not configured."}

        try:
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()

            available_refs = []
            if os.path.exists(ref_path):
                available_refs = os.listdir(ref_path)

            return {
                "status": "success",
                "skill_id": canonical_skill_id,
                "instructions": content,
                "references_available": available_refs,
            }
        except FileNotFoundError:
            return {"error": f"Expected file at {file_path} not found."}
        except Exception as e:
            return {"error": str(e)}

    def _city_disclaimer(self, city_context):
        overrides = self.translation_map.get("city_overrides", {})
        selected = city_context if city_context in overrides else "national"
        selected_obj = overrides.get(selected, {})
        national_obj = overrides.get("national", {})
        return selected_obj.get("disclaimer") or national_obj.get("disclaimer")

    def run_arch_calculator(self, calc_type, data=None, city_context=None):
        if not run_calculation:
            return {"error": "Calculator module not found in /core."}
        result = run_calculation(calc_type, data or {})
        if isinstance(result, dict) and result.get("error"):
            return result

        return {
            "status": "success",
            "calc_type": calc_type,
            "city_context": city_context or "national",
            "disclaimer": self._city_disclaimer(city_context),
            "translation_map_status": self.translation_status,
            "result": result,
        }


def main():
    try:
        raw_input = sys.stdin.read()
        if not raw_input:
            return

        input_data = json.loads(raw_input)
        tool_name = input_data.get("tool")
        arguments = input_data.get("arguments", {})

        dispatcher = MainlandArchitectDispatcher()

        if tool_name == "load_sub_skill":
            result = dispatcher.load_sub_skill(arguments.get("skill_id"))
        elif tool_name in {"run_arch_calculator", "run_hk_calculator"}:
            result = dispatcher.run_arch_calculator(
                arguments.get("calc_type"),
                arguments.get("data"),
                arguments.get("city_context"),
            )
        else:
            result = {"error": f"Unknown tool: {tool_name}"}

        sys.stdout.write(json.dumps(result))

    except Exception as e:
        sys.stdout.write(json.dumps({"error": f"Dispatcher Error: {str(e)}"}))


if __name__ == "__main__":
    main()