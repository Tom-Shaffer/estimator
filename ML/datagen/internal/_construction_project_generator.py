from enum import Enum
import random
from internal.enums.constructionEnums import building, hvac, efficiency
import math

def _gen_budget(buildingType: Enum,) -> int:
    if buildingType == building.residential:
        return math.floor(10000 * (abs(random.gauss(0, .5)) + 1))
    elif buildingType == building.commercial:
        return math.floor(500000 * (abs(random.gauss(0, .5)) + 1))
    elif buildingType == building.industrial:
        return math.floor(1000000 * (abs(random.gauss(0, .5)) + 1))
    else:
        return 

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
    
    return math.floor(hours / 168 / 12) + 6

    return

def _gen_buildtype() -> str:
    return random.choice(list(building))

def _gen_efficiency(buildingType: Enum) -> Enum:
    if buildingType == building.residential:
        return random.choices(list(efficiency),[.8,.15,.05])[0]
    elif buildingType == building.commercial:
        return random.choices(list(efficiency),[.3,.5,.2])[0]
    elif buildingType == building.industrial:
        return random.choices(list(efficiency),[.05,.15,.8])[0]
    else:
        return

def _gen_hvac_type(buildingType: Enum) -> Enum:
    if buildingType == building.residential:
        return random.choices(list(hvac),[.7,.175,.1,.025])[0]
    elif buildingType == building.commercial:
        return random.choices(list(hvac),[.2,.35,.4,.05])[0]
    elif buildingType == building.industrial:
        return random.choices(list(hvac),[.05,.05,.3,.6])[0]
    else:
        return

def _modify_budget_based_on_settings(budget: int, efficiencyRating: Enum, hvacType: Enum) -> int:
    if efficiencyRating == efficiency.high:
        budget *= 1.1
    elif efficiencyRating == efficiency.low:
        budget *= .9
    
    if hvacType == hvac.forcedair:
        budget *= .8
    elif hvacType == hvac.boiler:
        budget *= .9
    elif hvacType == hvac.heatpump:
        budget *= 1.1
    elif hvacType == hvac.geothermal:
        budget *= 1.2
    
    return math.floor(budget)