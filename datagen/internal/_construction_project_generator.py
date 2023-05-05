from enum import StrEnum
from _math import generate_random_decimal, generate_cubic_feet
from enums.constructionEnums import building, hvac, efficiency
import math

def _gen_area(buildingType: StrEnum, budget: int) -> int:
    if buildingType == building.residential:
        return math.triangular(1.75,2.50) * budget
    elif buildingType == building.commercial:
        return math.triangular(15,21) * budget
    elif buildingType == building.industrial:
        return math.triangular(22,27) * budget
    else:
        return 0

def _gen_vol(sqFootage: int) -> int:
    # Need to call generate_cubic_feet function and return it's result
    return

def _gen_deadline(cost: float, sqFootage: int) -> int:
    return

def _gen_buildtype(cost: float, sqFootage: int) -> str:
    return

def _gen_efficiency(cost: float, sqFootage: int) -> str:
    return

def _gen_hvac_type(cost: float, sqFootage: int) -> str:
    return