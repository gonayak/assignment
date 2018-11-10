# Write a function that accepts a list and doubles each value in the list.
# When no input parameter is provided, return an empty list

list1= [3,4,5,6]
list2=[]
def doublelist(n):
    new_list= []
    #if the list is empty
    if not n: pass
    #if list is not empty
    for i in n:
        new_list.append(i*2)
    print(new_list)

doublelist(list1)
doublelist(list2)