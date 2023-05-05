from enum import Enum


hvac = Enum('hvac_type',['forced air', 'boiler', 'heat pump','geothermal'])
building = Enum('building_type',['residential', 'commercial', 'industrial'])
efficiency = Enum('efficiency_level',['low', 'medium', 'high'])