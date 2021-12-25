#comprehension to decrease line of coding
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)

#comprehension to decrease line of coding
fruits = ["apple", "banana", "cherry", "kiwi", "mango",'sun','mon','tue','wed','thru','fri']

newlist = [x for x in fruits if "i" in x]

print(newlist)
newlist = [x for x in fruits if x != "apple"]
print(newlist)
newlist = [x for x in fruits]
print(newlist)
newlist = [x for x in range(10)]
print(newlist)
newlist = [x for x in range(10) if x < 5]
print(newlist)
newlist = [x.upper() for x in fruits]
print(newlist)
newlist = ['hello' for x in fruits]
print(newlist)
newlist = [x if x != "banana" else "orange" for x in fruits]
print(newlist)
