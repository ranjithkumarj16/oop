n=input("Enter a Number: ")
if type(n)==int:
	sum = 0
	while (n != 0):
		sum = sum+(n % 10)
		n=n//10
	print("Sum of Digit of given Number: ",sum)
elif type(n)==str:
	print("Invalid Input")
else:
	print("Invalid Input")
