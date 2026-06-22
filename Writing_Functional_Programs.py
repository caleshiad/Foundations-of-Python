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

# Parameters are the variable names listed in a function definition, they are placeholders for the values a function will receive and are seperated by commas 
# def multiply (x, y): x and y are the parameters 
# Arguments are the actual values you pass into the function when you call it
# multiply(3, 5): 3 and 5 are the arguments 



name = input("What's your name?")

def welcome(name): # name is the parameter
    print("Welcome,", name) 
welcome(name)

name = "Chris"
welcome(name)

name = "Todd"
welcome(name)

name = "Christie"
welcome(name)

# the return statement is a command inside the function that sends a value back to the part of the program that called the function
# when Python gets to the return statement the function stops running and hands back the specified result, allowing the value to be stored, printed or used in other calculations

def add_numbers(): # () shows that the function takes no parameters
    result = 3 + 5 # this line performs a calculation inside the function
    return result # this line ends the function and sends the value of result back to wherever the function was called. The return value is 8.
value = add_numbers() # the returned value from add_numbers() is assigned to the variable value
print(value) # this prints the value stored in value which is 8

bill = float(input("What is the total on your bill?"))
total_cost = bill + add_numbers()
print(f"The total cost of your service today is ${total_cost}.")

def birthplace():
    origin = print(input("Where are you from?"))
    print("That sounds like an interesting place.")

name = "Josh"
welcome(name)
birthplace()

# print() function provides information to the person running the program
# return statement gives data back to the program

# the pass statement is a placeholder that does nothing, it's used when you want to define a function syntactically but are not ready to write its code
# pass is used so that Python does not generate an error message due to a function with an empty body (which is not allowed)

def future_function():
    pass
# this allows the program to run while you plan or develop the function's logic later

def login_user():
    print("Logging in user")
def create_report():
    pass # Will be completed later
def send_email():
    pass # Placeholder until the email feature is added
login_user()
# in this example create_report and send_email are part of the program's design but not yet implemented
# using pass keeps the code valid and allows the rest of the program to run without errors while you continue development

# IT Support technician needs a simple way to calculate total weekly uptime for a server, each day's uptime in hours is recorded and the technician wants a reusable function that calculates the total uptime for the week and displays the result
# User-defined function to calculate total uptime

def calculate_total_uptime(hours_day1, hours_day2, hours_day3, hours_day4, hours_day5):
    total_uptime = hours_day1 + hours_day2 + hours_day3 + hours_day4 + hours_day5
    return total_uptime

# Call the function with recorded daily uptime values
weekly_uptime = calculate_total_uptime(24, 24, 23, 24, 22)

# Display the returned result
print("Total weekly server uptime (hours:)", weekly_uptime)

# this defines a function that doubles any number inputted 
def double_number(x):
    result = x * 2
    print(result)

double_number(5)

