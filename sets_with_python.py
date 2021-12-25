#sets with python
a={1,2,3,4,3}# sets is a collection of non repetive numbner
print(a)
print(type(a))
a=set() #empty set
print(type(a))
a.add(1)#add one argument one time
a.add(1)
a.add(1)
a.add(1)
a.add(1)
a.add(1)
print(a)#print only 1 because it never repeat the value
a.add(2)
a.add(3)
a.add(4)
a.add(5)
a.add(6)
print(a)#it prints all values of set
a.add((1,7,8,9,99,90))#add tuple in sets
print(a)
print(len(a))#print length of sets
a.remove((1,7,8,9,99,90))#removal of data from sets
print(a)
print(a.pop())#removes arbitary element from sets
print(a)
b={44,56,3,4,7,8,9}
print(b)

s=a.union(b)#adding two sets
print(s) 
s=a.intersection(b)#intersection of two sets
print(s)
print(a.clear())#clear set a
print(b.clear())#clear set b




