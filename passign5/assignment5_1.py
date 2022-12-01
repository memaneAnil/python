class Demo:
	Value=11
	def __init__(self,a,b):
		self.No1=a
		self.No2=b

	def fun(self):
		print("inside fun")
		print(self.No1)
		print(self.No2)
		print(self.Value)

	def gun(self):
		print("inside gun")
		print(self.No1)
		print(self.No2)
		print(Demo.Value)


def main():
	print("Enter first number")
	iNo1=int(input())
	print("Enter second number")
	iNo2=int(input())

	obj1=Demo(11,21)
	obj2=Demo(51,101)
	obj3=Demo(iNo1,iNo2)

	obj1.fun()
	obj2.fun()

	Demo.Value=999

	obj1.gun()
	obj2.gun()

	obj3.Value=888

	obj3.fun()


if(__name__=="__main__"):
	main()