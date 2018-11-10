#Write a function to test if a list contains any items.
# Return 'EMPTY' if it does not contain any items and 'NOT EMPTY' if it does.
list1= []
list2=[1,2]

def checklist(listlen):

    if not listlen:
        print ("Empty")
    else:
        print("NOT EMPTY")

checklist(list1)
checklist(list2)