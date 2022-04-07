# Implement 10 operations on String

x="Ranjith Kumar"
print("Given String: ",x)
while(1):
        print("1. Length")
        print("2. Concatination")
        print("3. Count of a Element")
        print("4. Finding a Element")
        print("5. Replacing a String")
        print("6. Reverse")
        print("7. Lowwer Case")
        print("8. Upper Case")
        print("9. Startswith Operation")
        print("10. Endswith Operation")
        print("11. Exit")
        ch=int(input("Enter Your Choice: "))

        if ch==1:
                print("Length of the  given String: ",len(x))
        elif ch==2:
                y=input("Enter a String to Concatinate: ")
                print("Concation of two strings: ",x+y)
        elif ch==3:
                y=input("Enter a element present in the string: ")
                print("Count of "+y+" is: ",x.count(y))
        elif ch==4:
                y=input("Enter a element to find: ")
                print("The element "+y+" is present in: ",x.find(y))
        elif ch==5:
                y=input("Enter a element present in the string to be get replaced: ")
                z=input("Enter a element to Replace: ")
                print("After Replacing: ", x.replace(y,z))
        elif ch==6:
                print("Reverse of given String: ", x[::-1])
        elif ch==7:
                print("Lowercase of given string: ",x.lower())
        elif ch==8:
                print("Uppercase of given string: ",x.upper())
        elif ch==9:
                y=input("Enter a element to check whether given string starts with that element or not: ")
                if x.startswith(y):
                        print("Given String is starts with "+y)
                else:
                        print("Given String is not starts with "+y)
        elif ch==10:
                y=input("Enter a element to check whether given string ends with that element or not: ")
                if x.endswith(y):
                        print("Given String is ends with "+y)
                else:
                        print("Given String is not ends with "+y)

        elif ch==11:
                break
        else:
                print("Invalid Input")


