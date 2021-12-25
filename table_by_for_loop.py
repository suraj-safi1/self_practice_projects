#table printing by for loop
b=int(input("Enter your number to print table:\n"))
i=1
for i in range(1,11):
    print(str(b)+ "X"+str(i)+ "=" +str(i*b))