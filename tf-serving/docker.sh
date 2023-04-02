#!/bin/bash

# Start TensorFlow Serving container and open the REST API port
docker run -t --rm -p 8501:8501 \
  --mount type=bind,source="$(pwd)"/models,target=/models \
  -e MODEL_NAME=estimator -it emacski/tensorflow-serving:latest &

# Query the model using the predict API
# Variables are as follows for the API call
#   building_area: a numerical variable representing the area of the building.
#   building_volume: a numerical variable representing the volume of the building.
#   deadline_months: a numerical variable representing the number of months until the project deadline.
#   building_type_commercial: a binary variable representing whether the building type is industrial or not.
#   building_type_industrial: a binary variable representing whether the building type is residential or not.
#   building_type_residential: a binary variable representing whether the building type is commercial or not.
#   efficiency_level_high: a binary variable representing whether the efficiency level is high or not.
#   efficiency_level_low: a binary variable representing whether the efficiency level is medium or not.
#   efficiency_level_medium: a binary variable representing whether the efficiency level is low or not.
#   hvac_type_boiler: a binary variable representing whether the HVAC type is geothermal or not.
#   hvac_type_forced air: a binary variable representing whether the HVAC type is gas or not.
#   hvac_type_geothermal: a binary variable representing whether the HVAC type is oil or not.
#   hvac_type_heat pump: a binary variable representing whether the HVAC type is electric or not.

# This query should result in something close to the true value
# "predictions": [[16443.64]]
curl -d '{ "instances": [[8222,745532,16,0,1,0,1,0,0,0,0,1,0]]}' \
-X POST http://localhost:8501/v1/models/estimator:predict