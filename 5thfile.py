def main():

	mylist = []
	
	n = int(input("Enter how many chimps are in the zoo: "))
	
	for i in range(n):
		name = input("Enter a name here ")
		mylist.append("name: " + name)
		Age = input("How old are they ")
		mylist.append("age: " + Age)
		x = 27 + 32
		y = '{0:0.0f}'.format(x)
		mylist.append(y)
		
	print(mylist)
		
main()
