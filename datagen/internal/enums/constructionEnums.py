from enum import StrEnum


hvac = StrEnum('hvac_type',['forced air', 'boiler', 'heat pump','geothermal'])
building = StrEnum('building_type',['residential', 'commercial', 'industrial'])
efficiency = StrEnum('efficiency_level',['high', 'medium', 'low'])