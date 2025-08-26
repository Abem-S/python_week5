#activity one
class Superhero:
    def __init__(self, name, superpower):
        self.name = name
        self.superpower = superpower

    def use_power(self):
        return f"{self.name} uses {self.superpower}!"

class Villain(Superhero):
    def __init__(self, name, superpower, villain_name):
        super().__init__(name, superpower)
        self.villain_name = villain_name

    def fought(self):
        return f"{self.name} fought {self.villain_name}!"

hero1 = Superhero("The Flash", "super speed")
print(hero1.use_power())

villain1 = Villain("The Flash", "super speed", "Reverse Flash")
print(villain1.fought())


#activity two 
class Vehicle:
    def move(self):
        pass  # base method

class Car(Vehicle):
    def move(self):
        return "Driving"

class Plane(Vehicle):
    def move(self):
        return "Flying"

class Boat(Vehicle):
    def move(self):
        return "Sailing"

vehicles = [Car(), Plane(), Boat()]
for v in vehicles:
    print(v.move())

