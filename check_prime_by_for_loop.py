# check inserted number is prime or not
num1=int(input("enter the number :\n"))
prime = False
for i in range(2, num1):
    if(num1%i == 0 and num1!=2):
        prime= True
        break
if prime:
    print("This number is not prime")
else:
    print("given number is prime")
    

