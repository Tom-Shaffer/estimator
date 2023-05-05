from enum import Enum
import random
from internal.enums.constructionEnums import building, hvac, efficiency
import math

def _gen_area(buildingType: Enum, budget: int) -> int:
    if buildingType == building.residential:
        return math.floor(budget / random.triangular(1.75,2.50))
    elif buildingType == building.commercial:
        return math.floor(budget / random.triangular(15,21))
    elif buildingType == building.industrial:
        return math.floor(budget / random.triangular(22,27))
    else:
        return

def _gen_vol(sqFootage: int) -> int:
    sqrt_number = math.sqrt(sqFootage)
    volume = sqrt_number ** 3
    return math.floor(volume)

def _gen_deadline(buildingType: Enum, sqFootage: int) -> int:
    hours = 0
    if buildingType == building.residential:
        hours = random.triangular(sqFootage / 6, sqFootage / 12)
    elif buildingType == building.commercial:
        hours =  random.triangular(sqFootage / 4, sqFootage / 6)
    elif buildingType == building.industrial:
        hours = random.triangular(sqFootage / 1,sqFootage / 4)
    else:
        return
    
    return math.floor(hours / 168) + 6

    return

def _gen_buildtype() -> str:
    return random.choice(list(building))

def _gen_efficiency(buildingType: Enum) -> Enum:
    if buildingType == building.residential:
        return random.choices(list(efficiency),[.7,.2,.1])[0]
    elif buildingType == building.commercial:
        return random.choices(list(efficiency),[.5,.3,.2])[0]
    elif buildingType == building.industrial:
        return random.choices(list(efficiency),[.3,.2,.5])[0]
    else:
        return

def _gen_hvac_type(buildingType: Enum) -> Enum:
    if buildingType == building.residential:
        return random.choices(list(hvac),[.7,.175,.1,.025])[0]
    elif buildingType == building.commercial:
        return random.choices(list(hvac),[.5,.1,.2,.2])[0]
    elif buildingType == building.industrial:
        return random.choices(list(hvac),[.2,.2,.3,.3])[0]
    else:
        return