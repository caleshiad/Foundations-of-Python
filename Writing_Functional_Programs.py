# Functions, Parameters and Arguments 

# A function is a reusable block of code that performs a specific task. Defined once and can be called multiple times. 
# A parameter is an input value that can be put into a function to return a result

# The function greet() prints Hello! when it is called.
def greet():               # tells Python you are defining a function () parameters are optional values a function can receive
    print("Hello!")        # the indented block contains the code that runs when the function is called
greet()

# user-defined function is a function created by programmer to perform a specific task instead of relying on Python's built-in functions
# can contain any code needed for the program and can be reused whenever they are called 
def add_two_numbers(x, y):
    result = x + y
    print(result)

add_two_numbers(3, 5)
add_two_numbers(145, 645)
add_two_numbers(21313, 332432)

# built-in functions already exist in Python for immediate use without importing anything or writing your own definition
# len() returns the number of items in a collection
# input() collects text typed by the user and returns it as a string
# range() generates a sequence of numbers for looping or iteration, usually increasing by 1
# type() returns the data type of a value, variable, or object in Python

# left off @ parameters and arguments section 8.2 