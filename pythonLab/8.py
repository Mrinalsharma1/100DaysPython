# 8. Object Oriented Programming 
# Program to create Employee class and instantiating an object upon it

class Employee:

	empCount = 0 
	
	def __init__(self, name, salary): 
		self.name = name 
		self.salary = salary 
		Employee.empCount += 1 
	
	def displayCount(self): 
		print (f"Total Employee {Employee.empCount}")
	
	def displayEmployee(self): 
		print (f"Name : {self.name}  Salary: {self.salary}")
		
emp1 = Employee("Zara", "2000")
emp1 = Employee("Manni", "5000")
emp1 = Employee("Kumar", "8000")

# emp1.displayEmployee()
emp1.displayCount()
# print ("Total Employee ", Employee.empCount)