class parent:
	def demo(self):
		print("In Parent Class Demo Method")
	
class child(parent):
	def demo(self):
		super().demo()
		#parent.demo(self)
		print("In Child Class Demo Method")
	
obj=child()
obj.demo()
