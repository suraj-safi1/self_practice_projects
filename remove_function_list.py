#remove function of list

#remove function 
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

#pop-its removes the itme from the end of the list
thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)

#pop index remove particular index value
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

#del keyword with index
thislist = ["apple", "banana", "cherry",'orange']
del thislist[2]
print(thislist)

#del to delete all details of list
thislist = ["apple", "banana", "cherry",'orange']
del thislist
print(thislist)
