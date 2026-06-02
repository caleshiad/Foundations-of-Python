#Variables are used to store different types of data 
#Variable names can only use letters, numbers, and underscores
#Variables cannot contain special characters
#Variable names cannot start with a number
#Variable names cannot contain Python keywords aka reserved words 

name = "John"
age= 30
weight = 200
print(name)
print(age)
print(weight) 

#Output is the way a program displays information to the user
#The print() function is used to display output to the user
print("Hello, world!")

#Input is the way a program gets information from the user
name = input ("What's your name?\n")
print("Nice to meet you " + name +"!")
age = input("How old are you, " + name + "? \n")

#A function is a block of code that performs a specific task
print("The weather report is updated daily.")
#A function can return data as a result
forecast_rain = input("Will there be rain today? (yes/no)\n ")
#A function helps avoid repeating the same code

#User-defined functions are functions that you create yourself
#You name the set of instructions and are able to reuse them throughout your program
#def is the keyword used to define a function
def greet_user():
    print("Hello, welcome to the program!")
    name = input("What is your name? \n")
    print("Nice to meet you " + name + "!\nToday we have so much to learn about Python!\n")
greet_user()

#Data types are the different types of data that can be stored in a variable
#Common date types include:
#int (Integer) - whole numbers
print (5)
#float (Float) - decimal numbers
print (5.5)
#str (String) - text
print ("Hello, world!")
#bool (Boolean) - True or False
print (True)
print (False)
#list (List) - a collection of items
print ([1, 2, 3])
#set (Set) - a collection of unique items
print ({1, 2, 3})
#tuple (Tuple) - a collection of items that cannot be changed
print ((1, 2, 3))
#dict (Dictionary) - a collection of key-value pairs
print ({"name": "John", "age": 30})