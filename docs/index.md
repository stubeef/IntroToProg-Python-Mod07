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
![Results of Figure 1](Screen Shot 2021-11-28 at 12.20.42 PM "Figure 1")https://github.com/stubeef/IntroToProg-Python-Mod07/blob/main/docs/Screen%20Shot%202021-11-28%20at%2012.11.28%20PM.png

### Summary
In summary, this assignment was a good introduction to handling errors and making errors and debugging more visible and clear. Using custom error classes are a great tool for designing custom error handling which makes it much easier to tune code and classes for my specific use cases. The try except code block also makes it much easier to integrate error handling into production code. Ultimately, this helps with creating more resilient code that won’t break over a simple error and many small errors can be made visible and quickly solved. 

