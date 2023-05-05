from internal._file_creator import generate_test_data

numRows: int = input("How many rows of data would you like to generate?\r\n")
nameFile: str = input("What filename would you like to create/append the data to?\r\n")
generate_test_data(int(numRows),nameFile)