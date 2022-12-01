class Circle:
	PI=3.14

	def __init__(self):
		self.Radius=0.0
		self.Area=0.0
		self.Circumference=0.0

	def Accept(self):
		print("Enter the Radius value ")
		self.Radius=float(input())

	def CalculateArea(self):
		self.Area=Circle.PI*self.Radius*self.Radius

	def CalculateCircumference(self):
		
		self.Circumference=(2*Circle.PI*self.Radius)

	def Display(self):
		print("Radius is :",self.Radius)
		print("Area is :",self.Area)
		print("Circumference is :",self.Circumference)

def main():

	obj1=Circle()

	obj1.Accept()
	obj1.CalculateArea()
	obj1.CalculateCircumference()
	obj1.Display()

	print("____________________")

	obj2=Circle()

	obj2.Accept()
	obj2.CalculateArea()
	obj2.CalculateCircumference()
	obj2.Display()
if(__name__=="__main__"):
	main()


