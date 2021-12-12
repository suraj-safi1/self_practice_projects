letter= ''' Dear <|name|>
                         This is glad to inform you are selected for the post of <|post|>
            Date: <|date|> 
            <|Name of CEO|>
            CEO-<|Company Name|>
            '''
name=input("Enter the Name of selected employee:\n")               
date=input("Enter the date:\n")
post=input("Enter the post:\n")
CEO=input("Enter CEO Name: \n")
Com_name=input("Enter Company name:\n")
letter=letter.replace("<|name|>",name)
letter=letter.replace("<|date|>",date)
letter=letter.replace("<|post|>",post)
letter=letter.replace("<|Name of CEO|>",CEO)
letter=letter.replace("<|Company Name|>",Com_name)
print(letter)

