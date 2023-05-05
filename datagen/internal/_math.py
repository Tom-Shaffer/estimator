import math
import random


def generate_random_decimal():
    # Generate a random number with a normal distribution
    x = random.gauss(0, 0.4)
    # Scale the result to fit between 0 and 1
    return (x / 5) + 0.5

def generate_cubic_feet(squareFeet: int):
    cubicFeet = round(math.sqrt(squareFeet)**3,0)
    return math.floor(cubicFeet)
