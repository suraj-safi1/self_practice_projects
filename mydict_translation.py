# user look up to dictionary to search hindi words meaning
mydict={"pankah":"fan",
        "chini":"sugar",
        "namak":"salt",
        "haldi":"turmeric",
        "daal":"pulses",
        "chawal":"rice"
        }
print("Options are :",mydict.keys())
a=input("Enter the word you need to translate:\n")
print("The meaning of your words is:",mydict.get(a))#if words not in dict they return none



