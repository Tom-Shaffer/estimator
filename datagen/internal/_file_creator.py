# This python script is used to generate test data for creating the neural network which
# will allow us to accurately estimate the cost of a construction project.
import random
import math
import os
import json

from _construction_project_generator import _gen_area, _gen_vol, _gen_deadline, _gen_buildtype, _gen_efficiency, _gen_hvac_type

def _generate_test_row(currentData: dict()):
    budget = math.floor(random.uniform(1,50))
    
    build_type = _gen_buildtype()
    efficiency = _gen_efficiency(build_type)
    hvac_type = _gen_hvac_type(build_type)
    area = _gen_area(build_type,budget)
    deadline = _gen_deadline(build_type,area)
    vol = _gen_vol(area)

    currentData['building_type'].append(build_type)
    currentData['building_area'].append(area)
    currentData['building_volume'].append(vol)
    currentData['deadline_months'].append(deadline)
    currentData['budget'].append(budget)
    currentData['efficiency_level'].append(efficiency)
    currentData['hvac_type'].append(hvac_type)

    return currentData

# Generates test data
# budget: Cost associated with the project in thousands of USD
# building_area: Size of building in square feet
# building_volume: Size of building in cubic feet
# deadline_months: desired schedule for project in months
def generate_test_data(rows: int, filename: str):
    if rows is None or filename is None:
        return

    testData = {
    "budget": [],
    "building_type": [],
    "building_area": [],
    "building_volume": [],
    "deadline_months": [],
    "efficiency_level": [],
    "hvac_type": []
    }

    for i in range(rows):
        testData = _generate_test_row(testData)
    filepath = os.path.join(os.getcwd() + "/output/", filename)

    firstKey = next(iter((testData)))
    output = []
    for i in range(len(testData[firstKey])):
        row = {}
        for key in testData:
            row[key] = testData[key][i]
        output.append(row)

    with open(filename, 'w') as jsonfile:
        json.dump(output, jsonfile, indent=4, separators=(',', ': '))
    print(f"File has been saved to {filepath}")