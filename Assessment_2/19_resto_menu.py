# Write program for building restaurant menu using class in Python

class MenuItem :
    def __init__(self,name,price) :
        self.name = name
        self.price = price

class Menu :
    def __init__(self) :
        self.items = {}

    def Add_item(self,menu_item) :
        self.items[menu_item.name] = menu_item.price

    def Display_menu(self) :
        print("   Menu   ")
        for name,price in self.items.items() :
            print(f"{name} - {price} Rs")

obj = Menu()
item1 = MenuItem("Lasagna",400)
item2 = MenuItem("Butter Chicken",250)
item3 = MenuItem("Steak",750)
item4 = MenuItem("Chicken Tandoori",600)
item5 = MenuItem("Black Coffee",40)


obj.Add_item(item1)
obj.Add_item(item2)
obj.Add_item(item3)
obj.Add_item(item4)
obj.Add_item(item5)

obj.Display_menu()

