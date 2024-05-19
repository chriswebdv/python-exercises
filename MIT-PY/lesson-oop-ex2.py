#Create an employee class

class Employee:
    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@gmail.com"

emp1 = Employee("Tank","Waldo",50000)
print(emp1.email)
print(emp1.first)
print(emp1.last)
print(emp1.pay)



