class Employee:
    def __init__(self, name):
        self.name = name
        self.salary = 0

    def update_salary(self, hours):
        self.salary = hours * 200

    def __add__(self, other):
        total_salary = self.salary + other.salary
        return total_salary
    
    def __radd__(self,other) :
        return self.salary+other


class Parttimeemp(Employee):

    def update_salary(self, hours):
        self.salary = hours * 150

e1 = Employee(name="John")
e1.update_salary(hours=6)
e2 = Employee(name="Robin")
e2.update_salary(hours=8)
e3 = Parttimeemp(name="Jake")
e3.update_salary(hours=8)

total = e1 + e2 + e3

print("Total Expence :", total)


