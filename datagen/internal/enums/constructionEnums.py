from enum import Enum


hvac = Enum('hvac',['forced air', 'boiler', 'heat pump','geothermal'])
building = Enum('building',['residential', 'commercial', 'industrial'])
efficiency = Enum('efficiency',['low', 'medium', 'high'])