# loop with list

#for loop with list
thislist = ["apple", "banana", "cherry",'orange','grapes']
for x in thislist:
  print(x)

#for loop using rang() and len()
thislist = ["apple", "banana", "cherry",'orange','grapes']
for i in range(len(thislist)):
  print(thislist[i])

#while loop with list
thislist = ["apple", "banana", "cherry",1,2,3,4,5,6,7]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1

#print table by while loop
thislist = [1,2,3,4,5,6,7,8,9,10]
i = 0
b=int(input("Enter your number to print table:\n"))
while i < len(thislist):
  print(thislist[i]*b)
  i = i + 1
