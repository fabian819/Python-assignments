# ASSIGNMENT ONE
class Superhero:
    def __init__(self, name, power, city):
        self.name = name
        self.power = power
        self.city = city

    def introduce(self):
        return f"I am {self.name}, protector of {self.city}!"

    def use_power(self):
        return f"{self.name} uses {self.power}!"

# Subclass with added functionality (Inheritance)
class FlyingSuperhero(Superhero):
    def __init__(self, name, power, city, flight_speed):
        super().__init__(name, power, city)
        self.flight_speed = flight_speed

    def fly(self):
        return f"{self.name} flies at {self.flight_speed} km/h!"

# Creating objects
hero1 = Superhero("Night Panther", "Shadow Stealth", "New York")
hero2 = FlyingSuperhero("Sky Falcon", "Wind Blast", "Los Angeles", 800)

# Using methods
print(hero1.introduce())
print(hero1.use_power())

print(hero2.introduce())
print(hero2.use_power())
print(hero2.fly())


# ASSIGNMENT TWO
class Vehicle:
    def move(self):
        raise NotImplementedError("Subclasses should implement this!")

class Car(Vehicle):
    def move(self):
        return "Driving 🚗"

class Plane(Vehicle):
    def move(self):
        return "Flying ✈️"

class Boat(Vehicle):
    def move(self):
        return "Sailing 🚤"

# List of vehicles
vehicles = [Car(), Plane(), Boat()]

# Polymorphism in action
for v in vehicles:
    print(v.move())
