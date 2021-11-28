import pickle
class IsNumericError(Exception):
    """
    Checks to see if a field is numeric
    """
    def __str__(self):
        return 'Data is not numeric'
# Data -------------------------------------------- #
strFileName = 'CostData.dat'
lstData = []

# Processing -------------------------------------- #
def save_data_to_file(file_name, list_of_data):
    objFile = open(file_name,"ab")
    pickle.dump(list_of_data, objFile)
    objFile.close()
    print("Data Saved")

def read_data_from_file(file_name):
    objFile = open(file_name,"rb")
    list_of_data = pickle.load(objFile)
    objFile.close()
    return list_of_data

# Presentation -------------------------------------- #
try:
    strInputDate = input("Please enter the date - e.g (2021-12-02): ")
    strInputCost = input("Please enter the cost for the day - e.g (3.99): ")
    if type(float(strInputCost)) == float:
        lstData = [strInputDate, strInputCost]
        print(lstData)
        save_data_to_file(strFileName, lstData)
        print(read_data_from_file(strFileName))

except Exception as e:
    print("Custom Error Class")
    raise IsNumericError()
    print(e,e.__doc__, type(e), sep = '\n')
except ValueError as e:
    print("ValueError Handler")
    print(e,e.__doc__, type(e), sep = '\n')
except Exception as e:
    print("Generic Error Handling")
    print(e,e.__doc__, type(e), sep = '\n')