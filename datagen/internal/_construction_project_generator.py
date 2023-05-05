from enum import StrEnum
import random
from enums.constructionEnums import building, hvac, efficiency
import math

def _gen_area(buildingType: StrEnum, budget: int) -> int:
    if buildingType == building.residential:
        return budget /  math.triangular(1.75,2.50)
    elif buildingType == building.commercial:
        return budget / math.triangular(15,21)
    elif buildingType == building.industrial:
        return budget / math.triangular(22,27)
    else:
        return

def _gen_vol(sqFootage: int) -> int:
    return

def _gen_deadline(buildingType: StrEnum, sqFootage: int) -> int:
    if buildingType == building.residential:
        return random.triangular(6 // sqFootage, 12 // sqFootage)
    elif buildingType == building.commercial:
        return random.triangular(3 // sqFootage, 6 // sqFootage)
    elif buildingType == building.industrial:
        return random.triangular(1 // sqFootage, 4 // sqFootage)
    else:
        return
    return

def _gen_buildtype() -> str:
    return random.choice(building)

def _gen_efficiency(buildingType: StrEnum) -> StrEnum:
    if buildingType == building.residential:
        return random.choices(efficiency,[.7,.2,.1])[0]
    elif buildingType == building.commercial:
        return random.choices(efficiency,[.5,.3,.2])[0]
    elif buildingType == building.industrial:
        return random.choices(efficiency,[.3,.2,.5])[0]
    else:
        return

def _gen_hvac_type(buildingType: StrEnum) -> StrEnum:
    if buildingType == building.residential:
        return random.choices(hvac,[.7,.175,.1,.025])[0]
    elif buildingType == building.commercial:
        return random.choices(hvac,[.5,.1,.2,.2])[0]
    elif buildingType == building.industrial:
        return random.choices(hvac,[.2,.2,.3,.3])[0]
    else:
        return