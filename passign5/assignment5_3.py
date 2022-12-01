class Arithmatic:
	def __init__(self):
		self.Value1=0
		self.Value2=0

	def Accept(self):
		print("Enter the first number...")
		self.Value1=int(input())
		print("Enter second number...")
		self.Value2=int(input())
		print("__________________________")
				
	def Addition(self):
		return (self.Value1+self.Value2)

	def Subtraction(self):
		return self.Value1-self.Value2

	def Multiplication(self):
		return self.Value1*self.Value2

	def Division(self):
		return self.Value1/self.Value2

def main():

	obj1=Arithmatic()

	obj1.Accept()
	print("Addition is :",obj1.Addition())
	print("Subtraction is:",obj1.Subtraction())
	print("Multiplication is:",obj1.Multiplication())
	print("Division is:",obj1.Division())

	print("___________________________")

	obj2=Arithmatic()

	obj2.Accept()
	print("Addition is :",obj2.Addition())
	print("Subtraction is:",obj2.Subtraction())
	print("Multiplication is:",obj2.Multiplication())
	print("Division is:",obj2.Division())

if(__name__=="__main__"):
	main()	