test-data-generator

# Classes
- Settings(lines = 15)
    - Initialises environment and data fields to work on
    - Optional data amount specifier (linesOfData)
- Generator
    - Takes in a Settings object
    - Generates the data
    
# Generator: Functions
To extend functionality, the following functions must be examined:
- parseRow(row)
    - Takes in a row as a list.
    - At every line of data generated this function is called.
    - This function calls randomiseFields() and calculateField().
    - Observe how it calls the other functions
- calculateField(row, *fields, upperRange)
    - This does a calculation.
    - This can be rewritten to do different things.
