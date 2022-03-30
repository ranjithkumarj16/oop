class op:

        def __init__(self):
                self.list1=[]

        def input(self):
                n=input("Enter the size of List: ")
                if(n.isalpha()):
                        print("Enter only Integers")
                        self.input()
                else:
                        for i in range(0,int(n)):
                                ele=int(input("Enter the Element: "))
                                self.list1.append(ele)
                        print("List: ",self.list1)

        def __add__(self,other):
                newlist=[]
                for i in range(0,len(self.list1)):
                        newlist.append(self.list1[i] + other.list1[i])
                print("Addition of Lists: ",newlist)

        def __sub__(self,other):
                newlist=[]
                for i in range(0,len(self.list1)):
                        newlist.append(self.list1[i] - other.list1[i])
                print("Subtraction of Lists: ",newlist)

        def __mul__(self,other):
                newlist=[]
                for i in range(0,len(self.list1)):
                        newlist.append(self.list1[i] * other.list1[i])
                print("Multiplication of Lists: ",newlist)

        def __floordiv__(self,other):
                newlist=[]
                for i in range(0,len(self.list1)):
                        newlist.append(self.list1[i] // other.list1[i])
                print("Floor Division of Lists: ",newlist)

