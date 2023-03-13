# estimator
Construction estimation neural network tool that allows users to enter data about a project, and recieve an accurate bid based off of empirical data

How to use:

dataGen:
  This folder contains a python program that allows you to generate n json objects that contain the input/output data necessary
  to train the neural network. You then need to transfer this json over to neuralnet to train it

neuralnet:
  This folder contains a python program which can train a neural network based on the data generated in the json. It does quite a trivial calculation
  of the estimated project cost based on the values of the various inputs (Right now there are a few enums, and a few scalar values)

tf-serving:
  This folder contains a docker file that should open up a tensorflow serving server with a local model. This should allow you to serve the model to
  HTTP requests. this will eventually be used to serve estimates to the main application
