# Implement 10 operations on Tuple

x=("1","2","R","K","RVCE",2,6,8)
y=("RANJITH","16","08")
print("Given Tuple: ")
print(x)
print(y)
while(1):
        print("1. Length")
        print("2. Concatination")
        print("3. Count of a Element")
        print("4. Max")
        print("5. Min")
        print("6. Indexing")
        print("7. Range Slicing")
        print("8. Membership")
        print("9. Repetition")
        print("10. Exit")
        ch=int(input("Enter Your Choice: "))

        if ch==1:
                print("Length of the  given Tuple: ",len(x))
        elif ch==2:
                print("Concation of two Tuyples: ",x+y)
        elif ch==3:
                y=input("Enter a element present in the Tuple: ")
                print("Count is: ",x.count(y))
        elif ch==4:
                y=input("Enter a new tuple with elements of same data type to find maximum value: ")
                print("Maximum is :",max(y))
        elif ch==5:
                y=input("Enter a new tuple with elements of same data type to find minimum value: ")
                print("Minimum is :",min(y))


        elif ch==6:
                y=int(input("Enter a Index Value to   print the element in it :"))
                print("The element present in  index is: ",x[y])
        elif ch==7:
                y=int(input("Enter  Starting Range: "))
                z=int(input("Enter Ending Range: "))
                print("The elements: ",x[y:z])

        elif ch==8:
                y=input("Enter a element in the tuple to find membership")
                if y in x:
                        print(y+" present in the tuple")
                else:
                        print(y+" is not present in the tuple")
        elif ch==9:
                y=int(input("Enter a number to repeat"))
                print(x*2)
        elif ch==10:
                break
        else:
                print("Invalid Input")



