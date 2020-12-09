class Employee:
	def __init__(self, firstname, lastname):
		self.firstname = firstname
		self.lastname = lastname
		# Complete the code!
		self.fullname = self.firstname + " " + self.lastname
		self.email = self.firstname.lower() + "." + self.lastname.lower() + "@company.com"
		
# Examples
# emp_1 = Employee("John", "Smith")
# emp_2 = Employee("Mary",  "Sue")
# emp_3 = Employee("Antony", "Walker")
# emp_1.fullname ➞ "John Smith"

# emp_2.email ➞ "mary.sue@company.com"

# emp_3.firstname ➞ "Antony"