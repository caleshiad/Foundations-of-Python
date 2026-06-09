# String Comparison and String Case 

#string comparisons let Python determine whether two pieces of text are identical or distinct 
"cat" == "cat" #Output will be True, because both strings are identical
"cat" == "Cat" #Output will be False, because the first letter is different (lowercase vs uppercase)
"apple" < "banana" #Output will be True, because "a" comes before "b" in the alphabet

# String Index is a number that points to a specific character inside of a string
# Python stores strings as a sequence, so each character has a position starting from 0 
# The purpose of indexing is to allow access to individual characters so you can examine them or use them in your program 
# word = pizza : the letter p is at index 0 and i is at index 1 and the last a is at index 4

word = "Supercalifragilisticexpealidocious" 
print(word[10])
print(word[-5])
print(word[15])

#Logical operators can be used with strings to help the program make decisions based on text
# specific positions can be checked using indexes and those checks can be combined with and, or, not 
name = "Liam"
if name [0] == "L": 
    print (True)

print(name [0] == "L" and name [-1] == "m")
print(name [3] == "o" and name [1] == "i") 

#String case refers to whether letters are uppercase or lowercase
#Python sees uppercase letters as smaller than lowercase ones 
print("Apple" < "banana")

#The functions lower() and upper() let you change the case of a strinf
# lower() function turns every letter in a sting into lowercase 
# upper() function turns every letter into uppercase 
word = "Hello"
print(word.lower()) #hello
print(word.upper()) #HELLO 

phrase = "I like PyThOn"
print(phrase.lower())
print(phrase.upper())

#symbols, special chararacters, and spaces have an index 
"Hello Python" # H is at index 0, e is at index 1, l is at index 2, o is at index 4, space is at index 5, P is at index 6, y is at index 7, t is at index 8, h is at index 9, o is at index 10, n is at index 11

#string slicing involves cutting out a piece of the string 
#In python slicing is done by using the square brackets with a start and end position seperated by a colon
# string[start:stop] this is the python syntax for slicing 
print("Hello from Python!"[2:8])

#Positive indexes start from the left 
text = "Python Programming"
first_four = text[:4]
print(first_four)
#Negative Indexs start from the right 
last_four = text[-4]
print(last_four) 
#Negative indexes are for when you want to know the position but don't need to focus on the length of the string 
last_half = text[-8:]
print(last_half) #this will print the last 8 characters of the string, which is "Programming"

filename = "assignment.pdf"
extension = filename[-3:]
print (extension) #this will print "pdf" which is the file extension of the filename string 
#this works for any filename with a 3 letter extension 

#Reversing a string can be done by using slicing with a step of -1 
text = "Hello World"
reversed_text = text[::-1]
print(reversed_text)

#String searching allows you to check if speicifc text appears within a larger string 
sentence = "The cunning cat outsmarted the animal control officer"
#the syntax for string searching uses the "in" operator to check if a a substring is present in a larger string 
print("cat" in sentence) #this will return True because "cat" is present in the sentence
print("the" in sentence) 
#string searching is case sensitive and will return a true or false value 

#the find string method is used to search for a specific substring within a string and returns its index position 
text = "The quick brown fox jumps over the lazy dog" 
index = text.find("fox")
print(index) #it will print 16 because "fox" starts at index 16 in the text string 
# if the text you are searching for is not found, the find method wil return -1 

#Splittinga string is the process of breaking it into smaller parts based on a seperator, like a space
# the syntax for that is string.split()
text = "The red firetruck was racing down the street"
parts = text.split(" ")
print(parts) 

list = "Red Fish, Blue Fish, Green Fish, Purple Fish"
parts = list.split(", ")
print(parts)

#String joining involves combining a list of seperate strings into a single string with a speicified seperator
# the syntax for that is string.join()
words = ["The", "quick", "brown", "fox"]
sentence = " ".join(words)
print(sentence)

# the strip() method is used to remove unwanted whitespace from the beginning and end of a string
# strip() removes leading left side and trailing white side whitespace
# whitespace includes spaces, tab(\t) and newline characters(\n)
# strip() creates a new string while the original string remains unchanged
text = "  Hello, world!"
cleaned = text.strip()
print(cleaned)

#strip() can be used to remove specific characters 
message = "***Welcome***"
print(message.strip("*"))
