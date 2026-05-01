import math


DEFAULT_EGRESS_RULES = {
    "occupancy_limits_m": {
        "residential": {"sprinklered": 45, "unsprinklered": 30},
        "office": {"sprinklered": 45, "unsprinklered": 30},
        "commercial": {"sprinklered": 45, "unsprinklered": 30},
        "assembly": {"sprinklered": 30, "unsprinklered": 20},
    },
    "occupancy_load_density_m2_per_person": {
        "office": 9.3,
        "commercial": 3.0,
        "assembly": 1.5,
        "residential": 25.0,
    },
    "min_stair_width_m": {
        "office": 1.1,
        "commercial": 1.2,
        "assembly": 1.3,
        "residential": 1.1,
    },
}

DEFAULT_AREA_RULES = {
    "categories": {
        "above_ground_main": {"countable": True},
        "below_ground_main": {"countable": True},
        "equipment_room": {"countable": True},
        "refuge_space": {"countable": False},
        "open_balcony": {"countable": False},
    }
}


class EgressCalculator:
    """Egress checks using configurable GB-style rule tables."""

    def calculate(self, data):
        payload = data or {}
        rules = payload.get("rules") or DEFAULT_EGRESS_RULES
        occupancy = payload.get("occupancy_type", "office")
        sprinklered = bool(payload.get("sprinklered", True))
        length = float(payload.get("length", 0))
        width = float(payload.get("width", 0))
        occupant_load = float(payload.get("occupant_load", 0))

        diagonal = math.sqrt(length ** 2 + width ** 2)
        occupancy_limits = rules.get("occupancy_limits_m", {}).get(
            occupancy, rules["occupancy_limits_m"]["office"]
        )
        limit = occupancy_limits["sprinklered" if sprinklered else "unsprinklered"]
        travel_ok = diagonal <= limit

        density = rules.get("occupancy_load_density_m2_per_person", {}).get(occupancy, 9.3)
        stairs_by_density = 1
        if occupant_load <= 0 and length > 0 and width > 0:
            occupant_load = max(1, round((length * width) / density))
        if occupant_load > 300:
            stairs_by_density = 3
        elif occupant_load > 100:
            stairs_by_density = 2

        min_stair_width = rules.get("min_stair_width_m", {}).get(occupancy, 1.1)

        return {
            "regulatory_basis": "GB 50016 (national baseline, verify local amendments)",
            "inputs": {
                "occupancy_type": occupancy,
                "sprinklered": sprinklered,
                "length_m": length,
                "width_m": width,
                "occupant_load": occupant_load,
            },
            "result": {
                "diagonal_travel_distance_m": round(diagonal, 2),
                "max_allowed_distance_m": limit,
                "travel_distance_status": "Pass" if travel_ok else "Fail",
                "recommended_stair_count": stairs_by_density,
                "minimum_stair_width_m": min_stair_width,
            },
        }


class BuildingAreaCalculator:
    """Building area aggregation using GB/T 50353-style countable categories."""

    def aggregate(self, floor_data, rules=None):
        items = floor_data or []
        active_rules = rules or DEFAULT_AREA_RULES
        categories = active_rules.get("categories", {})
        total_area = 0.0
        countable_area = 0.0
        non_countable_area = 0.0

        for item in items:
            area = float(item.get("area", 0))
            category = item.get("category", "above_ground_main")
            countable = categories.get(category, {}).get("countable", True)

            total_area += area
            if countable:
                countable_area += area
            else:
                non_countable_area += area

        return {
            "regulatory_basis": "GB/T 50353 (national baseline, verify local amendments)",
            "total_building_area_m2": round(total_area, 2),
            "countable_area_m2": round(countable_area, 2),
            "non_countable_area_m2": round(non_countable_area, 2),
        }


class DataSorter:
    """Sort OCR/layout data top-to-bottom and left-to-right."""

    def sort_by_layout(self, items):
        if not items or not isinstance(items, list):
            return []
        tolerance = 10
        return sorted(
            items,
            key=lambda b: (b.get("y", 0) // tolerance, b.get("x", 0)),
        )


def run_calculation(calc_type, data):
    """Factory function for dispatcher calculator routing."""
    if calc_type in {"egress_gb50016", "egress_1004_7"}:
        return EgressCalculator().calculate(data)
    if calc_type in {"building_area_gbt50353", "gfa_aggregator"}:
        payload = data or []
        if isinstance(payload, dict):
            return BuildingAreaCalculator().aggregate(
                payload.get("items", []), payload.get("rules")
            )
        return BuildingAreaCalculator().aggregate(payload)
    if calc_type == "layout_sort":
        return DataSorter().sort_by_layout(data)
    return {"error": f"Calculator type {calc_type} not implemented."}