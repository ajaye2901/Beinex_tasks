"""7) Extend the above solution again and add another instance method called 'as_dict'. 
The method should return a dictionary with the data of the student. 
It should contain 'name', 'score', 'grade', keys and their respective values."""


class Student :
    def __init__(self,name,score) -> None:
        self.name = name
        self.score  = score
        self.grade = self.Grade()
        self.d =self.as_dict()

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
        
    def as_dict(self) :
        d = {}

        d["Name"] = self.name
        d["Score"] = self.score
        d["Grade"] = self.grade

        return d
    
    
    def display(self) :
        print("Name : ",self.name)
        print("Mark : ",self.score)
        print("Grade : ",self.grade)
        print("dictionary = ",self.d)

stud_1 = Student("Leo",90)
stud_2 = Student("Messi",86)

stud_1.display()
stud_2.display()