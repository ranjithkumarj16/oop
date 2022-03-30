from op import *

obj1=op()
obj2=op()

while(1):
	print("\n 0. Exit \n 1. Continue")
	ch=int(input("Enter Your Choice: "))
	if ch==0:
		break
	elif ch==1:
		obj1.list1.clear()
		obj2.list1.clear()
		obj1.input()
		obj2.input()
		if(len(obj1.list1)==len(obj2.list1)):
			while(1):
				print("\n 0.Exit \n 1.Addition \n 2.Subtraction \n 3.Multiplication \n 4.Floor Division")


				ch=int(input("Enter Your Choice: "))

				if ch==0:
					break

				elif ch==1:
					obj1 + obj2

				elif ch==2:
					obj1 - obj2

				elif ch==3:
					obj1 * obj2

				elif ch==4:
					obj1 // obj2

				else:
					print("Invalid Input")
		else:
			print("Length of the 2 Lists are not Equal")
	else:
		print("Invalid Input")
		









