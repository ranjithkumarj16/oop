
d={}
class Employee:
	def acceptData(self):
		self.name=input("Enter Employee name: ")
		self.addr=input("Enter Employee Address: ")
		self.pan=input("Enter Pan Number: ")
		self.basic=int(input("Enter Basic Salary: "))
		self.pf=0.05*self.basic
		self.hra=0.20*self.basic
		self.tds=0.10*self.basic
		self.deduct=self.pf+self.tds
		self.da=0.15*self.basic
		self.cca=0.25*self.basic
		self.netSal=self.calcNetSal()
		self.updateDictionary()

	def calcNetSal(self):
		gross=self.basic+self.hra+self.da
		net_salary=gross-self.deduct
		return net_salary

	def updateDictionary(self):
		d.update({self.name:{
		"Name":self.name,
		"Address":self.addr,
		"Pan Number":self.pan,
		"Basic Salary":self.basic,
		"HRA":self.hra,
		"DA":self.da,
		"CCA":self.cca,
		"Deduct":self.deduct,
		"Net salary":self.netSal
}})

	def displayData(self):
		for key in d:
			print(d[key])

	def searchEmployee(self):
		count=0
		name=input("Enter Employee Name: ")
		if(name.isdigit()):
			print("Enter Valid  Name")
		else:
			for key in d:
				if(key==name):
					count=1
					print(d[key])
			if(count==0):
				print("No Record found for entered Employee")


e1=Employee()
while(1):
	ch=int(input("\n 0. Exit \n 1. To Add Data \n 2. To Display Data \n 3. To Search \n 4. Clear Dictionary\n"))
	if(ch==1):
		e1.acceptData()
	elif(ch==2):
		if (len(d)==0):
			print("There are no Records")
		else:
			e1.displayData()
	elif(ch==3):
		if(len(d)==0):
			print("There are no Records ")
		else:
			e1.searchEmployee()
	elif(ch==0):
		break

	elif ch==4:
		d.clear()
		print("Dictionary is Cleared")
	else:
                print("Invalid Choice")





