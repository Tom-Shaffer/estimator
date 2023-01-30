# This python script is used to generate test data for creating the neural network which
# will allow us to accurately estimate the cost of a construction project.
import random
import math
import os
import json

hvac_types = ['forced air', 'boiler', 'heat pump','geothermal']
building_types = ['residential', 'commercial', 'industrial']
efficiency_levels = ['high', 'medium', 'low']

def generate_random_decimal():
    return random.normalvariate(1, 0.1)

def generate_cubic_feet(squareFeet: int):
    cubicFeet = round(math.sqrt(squareFeet)**3 * generate_random_decimal(),0)
    return math.floor(cubicFeet)

def generate_test_row(currentData: dict()):
    budget = math.floor(random.uniform(50, 50000))
    currentData['budget'].append(round(budget * generate_random_decimal(),2))
    currentData['building_area'].append(math.floor(round(int(budget/2) * generate_random_decimal(),0)))
    currentData['building_volume'].append(generate_cubic_feet(currentData['building_area'][-1]))
    currentData['deadline_months'].append(math.floor(round(int(budget/1000) * generate_random_decimal(),0)))

    if currentData['building_area'][-1] > 5000:
        currentData['building_type'].append('industrial')
    else:
        currentData['building_type'].append(random.choice(['residential', 'commercial']))

    if budget > 40000:
        currentData['efficiency_level'].append('high')
        currentData['hvac_type'].append('geothermal')
    else:
        currentData['efficiency_level'].append(random.choice(efficiency_levels))
        currentData['hvac_type'].append(random.choice(hvac_types[:3]))

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
        testData = generate_test_row(testData)

    filepath = os.path.join(os.getcwd() + "/output/", filename + ".json")

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
    

numRows: int = input("How many rows of data would you like to generate?\r\n")
nameFile: str = input("What filename would you like to create/append the data to?\r\n")
generate_test_data(int(numRows),nameFile)