### This program allows you to generate synthetic data and 
### feed it directly into the model, loop this process, allowing
### brand new datapoints for each training session.

import subprocess

totalTrainingCycles = int(input("How many training cycles would you like to complete?"))
dataPerCycle = input("How many examples should be generated for each cycle?")

for i in range(totalTrainingCycles):
    subprocess.run(["python", "./datagen/main.py", dataPerCycle, "jobs.json"])
    subprocess.run(["python", "./neuralnet/estimator.py"])
    print("training cycle " + str(i) + " out of " + str(totalTrainingCycles))