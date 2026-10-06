"""Tests for mainland-architect-master/scripts/dispatcher.py."""
import json
import os
import subprocess
import sys
import unittest

ROOT = os.path.join(os.path.dirname(__file__), "..", "mainland-architect-master")
DISPATCHER = os.path.join(ROOT, "scripts", "dispatcher.py")


def run_tool(tool: str, arguments: dict) -> dict:
    payload = json.dumps({"tool": tool, "arguments": arguments})
    proc = subprocess.run(
        [sys.executable, DISPATCHER],
        input=payload,
        text=True,
        capture_output=True,
        cwd=ROOT,
        check=False,
    )
    if proc.returncode != 0:
        raise RuntimeError(proc.stderr or proc.stdout)
    return json.loads(proc.stdout)


class TestDispatcher(unittest.TestCase):
    def test_load_canonical_skill(self):
        out = run_tool("load_sub_skill", {"skill_id": "cn-building-codes"})
        self.assertEqual(out.get("status"), "success")
        self.assertEqual(out.get("skill_id"), "cn-building-codes")
        self.assertIn("Mainland Building Codes", out.get("instructions", ""))

    def test_hk_alias_maps_to_cn(self):
        out = run_tool("load_sub_skill", {"skill_id": "hk-building-codes"})
        self.assertEqual(out.get("status"), "success")
        self.assertEqual(out.get("skill_id"), "cn-building-codes")

    def test_fsd_legacy_alias(self):
        out = run_tool("load_sub_skill", {"skill_id": "cn-fsd-licensing-compliance"})
        self.assertEqual(out.get("status"), "success")
        self.assertEqual(out.get("skill_id"), "cn-fire-acceptance-closeout")

    def test_egress_calculator_pass_fail(self):
        out = run_tool(
            "run_arch_calculator",
            {
                "calc_type": "egress_gb50016",
                "data": {
                    "length": 5,
                    "width": 5,
                    "occupancy_type": "office",
                    "sprinklered": True,
                },
                "city_context": "national",
            },
        )
        self.assertEqual(out.get("status"), "success")
        status = out["result"]["result"]["travel_distance_status"]
        self.assertIn(status, ("Pass", "Fail"))

    def test_hk_procurement_alias(self):
        out = run_tool("load_sub_skill", {"skill_id": "hk-procurement-strategy"})
        self.assertEqual(out.get("status"), "success")
        self.assertEqual(out.get("skill_id"), "cn-procurement-strategy")
        self.assertIn("Procurement Strategy", out.get("instructions", ""))

    def test_load_plan_of_work(self):
        out = run_tool("load_sub_skill", {"skill_id": "cn-plan-of-work"})
        self.assertEqual(out.get("status"), "success")
        self.assertIn("Plan of Work", out.get("instructions", ""))

    def test_load_site_establishment(self):
        out = run_tool("load_sub_skill", {"skill_id": "cn-site-establishment"})
        self.assertEqual(out.get("status"), "success")
        self.assertIn("Site Establishment", out.get("instructions", ""))

    def test_discover_skill_count(self):
        out = run_tool("load_sub_skill", {"skill_id": "cn-building-codes"})
        self.assertEqual(out.get("status"), "success")
        subskills_dir = os.path.join(ROOT, "subskills")
        count = sum(
            1
            for name in os.listdir(subskills_dir)
            if name.startswith("cn-")
            and os.path.isfile(os.path.join(subskills_dir, name, f"{name}.md"))
        )
        self.assertEqual(count, 45)

    def test_unknown_skill(self):
        out = run_tool("load_sub_skill", {"skill_id": "cn-nonexistent-module"})
        self.assertIn("error", out)

    def test_main_shim_delegates(self):
        payload = json.dumps({"tool": "load_sub_skill", "arguments": {"skill_id": "cn-building-codes"}})
        main_py = os.path.join(ROOT, "main.py")
        proc = subprocess.run(
            [sys.executable, main_py],
            input=payload,
            text=True,
            capture_output=True,
            cwd=ROOT,
            check=False,
        )
        self.assertEqual(proc.returncode, 0)
        out = json.loads(proc.stdout)
        self.assertEqual(out.get("status"), "success")


if __name__ == "__main__":
    unittest.main()
