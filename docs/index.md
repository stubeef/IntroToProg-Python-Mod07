# Module07 Website
*Dev:* **slai**  
*Date:* **2021-11-28**  
[Assignment 07](https://github.com/stubeef/IntroToProg-Python-Mod07) 
---


## Error Handling and Pickling  
### Introduction 
For this assignment we were tasked with creating a short demo of error handling and pickling a file. I did a combination of the two in my code by asking the user in input some data and checking if the data was a float or not. If it passed then the data was written to the file, otherwise an error would be raised. 

### Methods 
I started by building out the individual, reusable components of the demo which were a a custom error handling class, a write_to_file() function, and a read_from_file() function. After that, I was able to start developing the presentation or main code block. I collect user input and then run it through a try except block so I can do my error handling. If the data is correct then the data can be written to the file otherwise it is passed as an error and the Exception and Customer Error class can handle it.

```
# ---------------------------------------------------------------------------- #
# Title: Assignment 07
# Description: Demo of pickle and customer error handling
# ChangeLog (Who,When,What):
# Slai,11.27.2021,Created Script
# ---------------------------------------------------------------------------- #


## Customer Error Class Code
class IsNumericError(Exception):
    """
    Checks to see if a field is numeric
    """
    def __str__(self):
        return 'Data is not numeric'

## Applying the custom error class in the Try block
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
except Exception as e:
    print("Generic Error Handling")
    print(e,e.__doc__, type(e), sep = '\n')
 ```

![Results of Figure 1](Screen%20Shot%202021-11-28%20at%2012.11.28%20PM.png "Figure 1") 
*Figure 1 - Example of code accepting a correctly formatted input*.  

![Results of Figure 2](Screen%20Shot%202021-11-28%20at%2012.13.06%20PM.png "Figure 2") 
*Figure 2 - Example of code accepting a correctly formatted input*. 

![Results of Figure 3](Screen%20Shot%202021-11-28%20at%2012.20.42%20PM.png "Figure 3")   
*Figure 3 - Example of code accepting a correctly formatted input*.  

### Summary
In summary, this assignment was a good introduction to handling errors and making errors and debugging more visible and clear. Using custom error classes are a great tool for designing custom error handling which makes it much easier to tune code and classes for my specific use cases. The try except code block also makes it much easier to integrate error handling into production code. Ultimately, this helps with creating more resilient code that won’t break over a simple error and many small errors can be made visible and quickly solved. 

