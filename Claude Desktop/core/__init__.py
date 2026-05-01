"""
Mainland Architect Core Logic Package
Contains mathematical engines for egress, building area, and data sorting.
"""

from .calculators import (
    EgressCalculator,
    BuildingAreaCalculator,
    DataSorter,
    run_calculation
)

# You can also define package-wide constants here
VERSION = "1.0.0"
AUTHOR = "Rico Kwok"

# This defines what is exported when someone runs 'from core import *'
__all__ = [
    "EgressCalculator",
    "BuildingAreaCalculator",
    "DataSorter",
    "run_calculation"
]