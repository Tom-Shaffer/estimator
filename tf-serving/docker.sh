#!/bin/bash

# Start TensorFlow Serving container and open the REST API port
docker run -t --rm -p 8500:8501 \
    -v "/Users/tomshaffer/estimator/tf-serving/models/estimator_model" \
    -e MODEL_NAME=estimator_model \
    emacski/tensorflow-serving &