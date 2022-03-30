x=(2,3,6,2,8,1,5,3,10,11,10)
print("Tuple: ",x)
while(1):
	print("1. Length")
	print("2. Count a element in the Tuple ")
	print("3. Return Highest Value(max())")
	print("4. Return Lowest Value(min())")
	print("5. Slicing")
	print("6. Exit")
	ch=int(input("Enter your Choice: "))

	if ch==1:
		print("Length of Tuple is: ",len(x))
	elif ch==2:
		y=input("Enter a number present in the tuple: ")
		print("Count of "+y+" is: ",x.count(y))
	elif ch==3:
		print("Highest Value in the Tuple is: ",max(x))
	elif ch==4:
                print("Lowest Value in the Tuple is: ",min(x))

	elif ch==5:
		a=int(input("Enter Starting Range: "))
		b=int(input("Enter Ending Range: "))
		print("Sliced String",x[a:b]) 
	elif ch==6:
		break
	else:
		print("Invaid Input")
