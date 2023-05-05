from enum import Enum


hvac = Enum('hvac',['forcedair', 'boiler', 'heatpump','geothermal'])
building = Enum('building',['residential', 'commercial', 'industrial'])
efficiency = Enum('efficiency',['low', 'medium', 'high'])