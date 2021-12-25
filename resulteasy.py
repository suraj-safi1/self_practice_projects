#result
sub1=int(input("Enter sub1 number: "))
sub2=int(input("Enter sub2 number: "))
sub3=int(input("Enter sub3 number: "))
per=(sub1+sub2+sub3)/3
total=sub1+sub2+sub3
print("Total marks=", total)
if sub1<33 or sub2<33 or sub3<33:
    print("you are fail due to having less than 33 in any subject")
elif (sub1+sub2+sub3)/3<40:
    print("you are fail due to percentage is less than 40")

if per >59 and per < 75:
    print("Result: Congratulation! you are passed with First Division")
elif per>=40 and per <= 50:
    print("Result: Congratulation! you are passed with Third division")
elif per > 50 and per <= 59:
    print("Result: Congratulation! you are passed with second division")
elif per > 75:
    print("Result:Congratulation! you are passed with Distinction")
else:
    print("you are fail")
    