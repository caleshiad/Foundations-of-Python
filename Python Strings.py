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

# left off @ 5.3 Essential Practice