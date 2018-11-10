#Write a function that accepts two arbitrary strings and returns a
# new string containing only the unique characters present in both inputs.

def newstring(string1,string2):
    new_str=""
    for char in string1:
        if char not in string2 and char not in new_str:
            new_str+=char
    for char1 in string2:
        if char1 not in string1 and char1 not in new_str:
            new_str+=char1
    print new_str

string1= "hello"
string2="welcome"
newstring(string1,string2)


