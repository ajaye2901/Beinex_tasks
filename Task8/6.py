"""6) Extend the above solution and add another instance attribute called grade (should be string).
Assign value to grade from within the constructor.

The value should not be taken from user input.

Instead use the following conditions and assign values to grade by using the value of score.

grade = A+ if score >=90

grade = A if score >=80 and <90

grade = B+ if score >=70 and <80

and so on.

if score is below 40 then grade should be FAILED"""


class Student :
    def __init__(self,name,score) -> None:
        self.name = name
        self.score  = score
        self.grade = self.Grade()

    def Grade(self) :
        if self.score >= 90:
            return "A+"
        elif self.score >=80 and self.score<90 :
            return "A"
        elif self.score >=70 and self.score<80 :
            return "B+"
        elif self.score >=60 and self.score<70 :
            return "B"
        elif self.score >=50 and self.score<60 :
            return "C"
        elif self.score >=40 and self.score<50 :
            return "C+"
        else :
            return "Failed"
    
    
    def display(self) :
        print("Name : ",self.name)
        print("Mark : ",self.score)
        print("Grade : ",self.grade)

stud_1 = Student("Leo",90)
stud_2 = Student("Messi",86)

stud_1.display()
stud_2.display()
