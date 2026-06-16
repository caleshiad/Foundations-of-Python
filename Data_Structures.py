# data structures are ways to organize and store information so programs can use it (ex: lists, tuples)

# Lists: containers that hold multipe items in order in []
# List items can be added, removed, or changed  (mutable)
# Lists items maintain the order in which they are added
# Lists are heterogenous since they can hold different data types
#Lists are dynamic since they grow/shrink automatically when items are added or removed
# Lists support indexing
students = ["Rodney", "Jessica", "Melissa", "Noah", "Roberto", "Kelly", "Isaac"]
print(students)
print(len(students))
print(students[3:5])
print(students[6])
print(len(students) -1) #will print 6 since there are 7 items in the list and 7-1=6

# the pop() method removes an item from a list and returns the value that was removed
# if pop() is given an index it removes the item at that position, the list will be updated and you'll be able to use the removed value in the program
absent_students = students.pop() #this will remove and return the last item of the list
print(absent_students)
print(students)
suspended_students = students.pop(1)
print(suspended_students)
print(students)

# index() is a list method that tells you the position of a specific element in a list
# it searches the list from left to right and returns the index of the FIRST matching value
teachers = ["Smith", "Rhodes", "Bernstein", "Caldwell"]
print(teachers)
print(teachers.index("Caldwell"))

class_pets = ["Hamster", "Turtle", "Fish", "Ferret"]
pet_four = class_pets.index("Ferret")
print(pet_four)

# The remove() method deletes the first occurence of a specific value from a list
# remove() only takes 1 argument at a time
# if the value you put with remove() does not exist, Python raises a ValueError
class_sizes = ["31", "33", "31", "33", "35", "31"]
class_sizes.remove("31")
print(class_sizes)

# the len() function is used to find the number of items in a collection
# when using len() with a list it tells us how many items the list contains
buses = ["Bus One", "Bus Two", "Bus Three", "Bus Four", "Bus Five"]
amount_of_buses = len(buses)
print(amount_of_buses) 

# Use len() to retrieve the last item in a list by using its length to calculate the final index
after_school = ["Erin", "Jessica", "Monica", "Jesse", "Luke", "Caleb", "Aaron"]
last_index = len(after_school) -1
last_student = after_school[last_index]
print(last_student)

# append() adds a new item to the end of the list
# append() changes the original list instead of creating a new one
# syntax is list_name.append(value)
new_students = ["Ravi", "Justin", "Emma"]
print(new_students)
new_students.append("Erica")
print(new_students)

# sort() arranges items in a list in a specific order
# strings are sorted alphabetically, numbers from smallest to largest
# sort() changes the original list instead of creating a new one
# cannot sort mized data types

test_scores = ["77", "82", "95", "80", "61", "92", "84"]
test_scores.sort()
print(test_scores) #this will be in ascending order

test_scores.sort(reverse=True) #this will be in ascending order
print(test_scores)

# Dictionaries store information using key-value pairs inside {} 
# Each key in a dictionary is linked to a specific value
# Dictionaries enable you to label and access data clearly 
#Dicitionaries are mutable (items can be added, changed or removed)
#Keys must be immutable types like strings, numbers, or tuples, values can be any date type
student_ids = {"Rodney: 323435", "Jessica: 741957", "Melissa: 182057", "Noah:472946", "Roberto: 293572", "Kelly:004284", "Isaac:694572"}
print(student_ids)

# get() is used retireve the value for a specified key 
# if a key is missing it returns "None" 
profile = {"name": "Jessica", "dob": "01/24/2013", "sex": "F", "student_id": "741957", "attendance" : "absent"}
profile["attendance"] = "present" #the key value for attendance is updated to present
print(profile["attendance"])
dob = profile.get("dob") 
print(dob)
print(profile.get("name")) # this is how get() is used to retrieve a value for a key

# keys() shows you all of the keys that exist in a dictionary, not their actual values
# updates automatically if the dictionary changes 
# used when you want to loop through keys or see what info a dictionary stores 
print(profile.keys()) # will print all of the keys in profile 

# values() shows all of the values in the dictionary 
print(profile.values()) # will print the values in profile

# items() will show all of the key value pairs in a dictionary 
print(profile.items()) # will print all of the items in profile

# Modifying Python Dictionaries 

# add/modify dictionary elements by assigning a value to a key using square brackets, if key already exists its value will be updated
# remember Python is case sensitive, if you are updating pay attention to lower/upper case
lion = {"firstname": "Alex", "lastname": "The Lion", "Origin": "NYC", "Location": "NYC", "Nickname": "The King of New York"}
print(lion.items())
lion["Location"] = "Madagascar"
print(lion.items())

# update() is used to add or modify dictionary elements by passing another dictionary or key-value pairs to it
# if a value already exists it's just replaced
attendance = {"Rodney": "Present", "Jessica": "Absent", "Andreas": "Present", "Roberto": "Absent", "Skyler": "Present"}
print(attendance.items())
attendance.update({"Rodney": "Absent"})
print(attendance)

# items can be removed using the "del" keyword 
info = {"name": "Alex", "age": "20", "role": "student", "favorite_color": "red"}
del info ["favorite_color"] # this is the syntax for using del to remove items from a list
print(info)

# pop() is another way to remove items 
# give pop() the key you want to remove and it will delete the key-value pair and return the value that wa removed allowing you to store it or use it immediately
asset_tag = {"device_name": "HP1234", "serial_number": "AFFE3422331", "assigned_user": "M.Scott"}
removed_value = asset_tag.pop("assigned_user")
print(removed_value)
print(asset_tag)
# if the value you are targetting does not exist pop() will return a KeyError unless a default value is given 





# Tuples are ordered collections of items stored inside ()
# Tuples cannot be changed after creation 
# Tuples can store different data types in the same structure
student_one = ("Rodney", 323435,"6th Grader" ) #this tuple shows the student name, student ID, and their grade level
print(student_one)

# A set is a collection of unique items stored inside {}, no duplicate items are allowed
honor_roll = {"Melissa", "Noah", "Roberto", "Isaac"}
print(honor_roll)

# Python knows what kind of data structure is being used because of the syntax used when creating them and the type it already is in memory 
# List [] is always a list
# Tuple () is always a tuple unless empty
# Set {} values only with no :
# Dictionary {} uses : between key/value


