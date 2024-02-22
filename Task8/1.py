
""" 1) Write a program to create a class by name Students, and initialize attributes like name, age, and grade 
while creating an object."""

class Students :

    def __init__(self,name,age,grade) -> None:
        self.name=name
        self.age=age
        self.grade=grade

details = Students("Ajay",23,"A+")

print(details.name,details.age,details.grade)


