#spam detection from string
text=input("Enter the text: \n")

if ("make a lot of money" in text):
    spam= True
elif("by now" in text):
    spam = True
elif("subscribe now" in text ):
    spam = True
else:
    spam=False

if(spam):
    print("the text having spam words")
else:
    print("their is no spam")


