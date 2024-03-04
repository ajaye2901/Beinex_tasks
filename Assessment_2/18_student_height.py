# Python program to for student height record for a school using Class and Objects.

class School :
    def __init__(self) :
        self.details = {}

    def add_details(self,name,height) :
        self.details[name] = height

    def display_details(self) :
        print(self.details)

obj = School()
obj.add_details("Messi",168)
obj.add_details("Ajay",176)
obj.add_details("Leo",174)
obj.add_details("Micheal",180)
obj.add_details("Aegon",178)
obj.display_details()