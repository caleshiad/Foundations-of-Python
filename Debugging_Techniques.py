# Troubleshooting involves identifying the cause of a program's non functional behavior and resolving the issue. 
# by reading the error message given, checking the code step-by-step, and testing small changes, most problems can be solved

# Troubleshooting Process
# 1. Identify the problem - notice what is going wrong
# 2. Reproduce the issue - rerun the script to confirm the problem is consistent
# 3. Analyze the cause - read error messages and inspect related code
# 4. Try a solution - apply a docused change to resolve the issue
# 5. Test the fix - rerun the program to see if the issue is resolved
# 6. Reflect and document - document the issue and resolution

# NameError appears when you use a variable that has not been defined
# SyntaxError appears when Python encounters code it cannot interpret (like a missing colon) due to violating the language's rules 
# Exceptions occur when something goes wrong during the execution of the program, they interrupt normal program flow and signal that an error has occured 

# A try-except block is a structure that allows the program to handle errors w/o crashing
# Code that might cause an error is placed inside the try block and if an error occurs Python skips the rest of the try block and runs the except instead
# This allows the program to respond to the problem in a controlled way, like showing a helpful error message or using a safe default value
# try-except blocks keep programs running smoothly even when something unexpected happens 

try:
    number = int(input("Enter a number:"))
    print("You entered:", number)
except ValueError:
    print("That is not a valid number.")


# Debugging with Output Statements involves adding temporary print statements to your code to observe the program's behavior as it runs 
# the statements help you track the values of variables, confirm specific lines of code are being reached, and understand how the program flows 

total = 0
numbers = [2, 4, 6, 8]
for n in numbers:
    print("Debug: current number is ", n) # debugging output
    total = total + n
    print("Debug: total is now ", total) # debugging output
print("Final total: ", total)

# Calculation errors occur when the wrong operation, formula, or numbers are used

# Debugging Calculation Errors
# 1. Print Variable Values
# 2. Check the formula
# 3. Compare with hand caluclations
# 4. Fix the code

# Logic errors do not crash a program but they do produce incorrect or unexpected results 
# troubleshooting logic errors involves checking if the program is doing what you intended or what you accidentally told it to do
# add print statements to track the values of important variables as the program runs
# test the program with various inputs including edge cases, to identify what behavior deviates from expected results
# split complex logic up into smaller peices and verify each part works correctly before combining them
# walk through code manually step-by-step to see if any part diverges from the behavior you expected from the program 

# An Off-by-One error is a logical mistake where a loop, index, or range runs one too many or one too few times 
# typically happens with these b/c Python uses zero-based indexing 
# happens because Indexes start at 0, not 1
# because the range () function icnludes the start value but excludes the end value
# because loop conditions like < versus <= are easy to confuse

# Loop errors occur when a program runs too many times, not at all, or repeats the wrong set of instructions 
# Troubleshooting Loop Errors:
# check that the loop condition will eventually become false, or else you would have an infinite loop
# print the loop variable inside the loop to see how it changes during each iteration
# make sure the loop starts with the correct intial value so it runs the intended number of times
# make sure that updates to the loop variable are occuring in the correct location and with the proper mathematical operations 
# walk through the loop manually to see how many times it should run and what the loop variable should be

# The goal of the program is to print numbers 1 through 5.
counter = 1
while counter < 8:
    print(counter)
    counter = counter + 1 
# after this runs you will notice the number 5 is missing. below is the corrected version 

# here is one way you could go about fixing the code
counter = 1
while counter < 10:
    print (counter)
    counter = counter + 1

# here is another way you could go about fixing the code
counter = 1
while counter <= 9:
    print(counter)
    counter = counter + 1

# Here is an example of creating an infinite loop
# count = 1
# while count <= 5:
#     print(count) 
# this would go on forever because the value of count is never changed isnide the loop

# Here is how you write the loop and make sure the condition eventually becomes false
count = 1
while count <= 10:
    print(count)
    count = count + 1

# troubleshooting function errors means checking how a function is defined, how it is called, and how data moves in and out of it
# if a function is not defined before it is called it will raise a NameError
# the number of arguments passed should match the number of parameters in the function definition, mismatches cause TypeError problems
# print values inside the function to verify parameters contain what you think they do, helps you see if the right data is being sent
#  confirm that the functions return statement is correct, missing return statements lead to unexpected results in the main program 
# function name should be spelled consistently throughout
# test the function by calling it with simple values first, so you can easily trace the behavior 

# Syntax Errors 
# Troubleshooting Syntax Errors:
# Read Error Message
# Carefully check each line
# Fix the code