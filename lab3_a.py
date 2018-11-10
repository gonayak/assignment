#a. Write a function that accepts an integer and returns True
#  if the input is between 4 and 10, inclusive; otherwise, return False

def intergernum(n):
    if n in range(4,11):
        print True
    else:
        print False

n= int(raw_input("Enter the number : "))
intergernum(n)