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

#Formatted strings (f-strings) are an easier way to display varibles in a string
# f-strings are created by adding an 'f' before the opening quotation mark of a string and curly braces {} around the variable you want to include in the string
name = "John"
age = 30 
print(f"The user's name is {name} and they are {age} years old.")

#string concatenation is the process of combining two or more strinfs using the + operator 
first_name = "John"
last_name= "Doe"
age = "30"
username = first_name + last_name + age 
print(username)
#concatenation can only be used with strings
print (first_name + " " + last_name) #this will put a space between the first and last name

#when int is used to convert a float to an integer it does not round the number it simply removes the decimal part
number = 5.9
print(int(number)) #Output will be 5, not 6

#a type conversion ia a conversion of one data type to another data type 
print(float(1+2))
#an implicit type conversion is when python automatically converts one data type to another data type 
1 + 2.5 #Output will be 3.5, not 3 because python automatically converts the integer to a float
print(1 + 2.5)

#Lists hold multiple items in order, enclosed in square brackets [] and separated by commas
#lists are flexible, items can be added, removed, or changed after the list is created
fruits = ["apple", "banana", "cherry", "blueberry", "grape", "orange"]  
print(fruits)

##Tuples store multiple items in order, enclosed in parentheses () and separated by commas
#Tuples are immutable, meaning that once a tuple is created, its items cannot be changed, added, or removed
#Tuples are useful for storing data that should not be modified, it protects the data from accidental changes
coordinates = (10, 20)
print(coordinates)

#A range represents represents a sequuence of numbers that follows a pattern
#Range(5) describes numbers 0-4 in order 
#Ranges are used to generate a sequence of numbers to guide repeated actions, such as loops or to create predictable patterns
#Range allows you to specify a start, stop, and step value 
range(1, 10, 2) #This will generate the numbers 1, 3, 5, 7, and 9
#Python will start at 1, stop before 10, and count by 2s
#Range is immutable
print (list(range(1, 10, 2)))
numbers = range (3, 15, 3)
print (list(numbers)) #Output will be [3, 6, 9, 12]

#Booleans are True or False data type values that help us make decisions in our code
#Booleans are essential for conditions and logic 
6 > 5 #Output will be True
9 < 7 #Output will be False
print(6 > 5)
print(9 < 7)
#Booleans are case sensitive, they must be capitalized 
# true is not the same as True and false is not the same as False, writing them wrong will cause an error

#Arithmentic operators are used to perform mathematical operations on numbers 
# + Addition
# - subtraction 
# * multiplication
# / division
# // floor division (returns the whole number part of the division)
# % modulus (returns the remainder of the division)
# ** exponentiation (raises a number to the power of another number)
print (5 + 3) #Output will be 8
print (5 - 3) #Output will be 2
print (5 * 3) #Output will be 15
print (5 / 3) #Output will be 1.6666666666666667
print (5 // 3) #Output will be 1
print (5 % 3) #Output will be 2
print (5 ** 3) #Output will be 125

"Go" *4 #Output will be "GoGoGoGo", the string "Go" is repeated 4 times
print("Go" * 4)

x = 5 + 6
y = 25 -10
z = x * y
print(z) #Output will be 165, because x is 11 and y is 15, so 11 * 15 = 165

#Python follows PEMDAS when evaluating mathematical expressions

#Comparison operaters are used to compare two values and return a boolean result (True or False)
# == equal to
# != not equal to
# > greater than
# < less than
# >= greater than or equal to
# <= less than or equal to

#Assignment operators lets you store values in variables and perform operations on those variables
# = assigns a value to a variable
# += adds a value to a variable and assigns the result back to the variable
# -= subtracts a value from a variable and assigns the result back to the variable
# *= multiplies a variable by a value and assigns the result back to the variable
# /= divides a variable by a value and assigns the result back to the variable
# //= performs floor division on a variable by a value and assigns the result back to the variable
# %= performs modulus on a variable by a value and assigns the result back to the variable      

total = 8
total += 2 #This is the same as total = total + 2, so total will now be 10
total *= 3 #This is the same as total = total * 3, so total will now be 30
print(total) #Output will be 30

#Logical operators let Python combine conditions, which allows complex decision making in code 
#Logical operators return a boolean result of True or False based on the conditions being evaluated
#The main logical operators are: and, or, and not
#and returns True if both conditions are true, otherwise it returns False

#Comparison, Logic, and Precedence Lab
#TODO: Create two variables
a = 10
b = 5
#TODO: Compare the rwo variables and print the result
print(a > b)
#TODO: Update one variable using an assignment operator
a += 3
print(a)
#TODO: Use logic operators to combine comparisons
result = (a > b) and (b < 10)
#TODO: Print the final result
print(result)