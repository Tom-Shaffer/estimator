import os
import sys
from internal._file_creator import generate_test_data

numRows: int = sys.argv[1] if len(sys.argv) == 3 else input("How many rows of data would you like to generate?\r\n")
nameFile: str = sys.argv[2] if len(sys.argv) == 3 else input("What filename would you like to create/append the data to?\r\n")

if os.path.exists(nameFile):
    os.remove(nameFile)

generate_test_data(int(sys.argv[1]),sys.argv[2])