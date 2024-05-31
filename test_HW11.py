#HW Part1







#HW Part2










#HW Part3
    #What is a Python module and how does it differ from a Python package?
        #Modules contain ready-to-use codes. There are built-in modules in Python Standard Library (e.g. math) but one can make custom modules as well by creating e.g. functions. These modules can be imported. 
        #Packages are modules which contain sub-modules. These non built-in modules and sub-modules can be imported as well (e.g. os, random)
    #What are side effects and give some examples.
        #Side effect if when one imports a custom module (e.g. function) and the module prints/asks/writes something in the file. We dont want that, it is better to avoid these side effects. E.g. when we import turtle, nothing opens until we wire e.g. turtle.forward().
    #What are Exceptions and what to do if third-party code that we use throws them?
        #Exceptions are errors which are detected during execution. Try to understand the error message and correct your input in a way that you dont get the error message anymore. 
    #Using which keywords can you create, throw and catch your new custom Exception?
        #Try block: lets you test a block of code for error, except block: catches the error, else block: executes code when there is no error, finally block: executes the code regandress if there is or isnt an error.
    #Give examples of some benefits of testing?
        #Benefits: verification of the code without time consuming and error prone manual testing