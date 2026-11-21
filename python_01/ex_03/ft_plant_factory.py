#!/usr/bin/env python3


class Plant:
    def __init__(self, name: str, height: float, age: int):
        self.name = name
        self.height = height
        self.age = age

    def show(self)-> None:
        print(f"{self.name.capitalize()}: {self.height}cm, {self.age} days old")

    def grow(self)-> None:
        self.height += 0.512456

    def age_plant(self)-> None:
        self.age += 1


rose = Plant("rose", 25, 30)
oak = Plant("oak", 200, 365)
cactus = Plant("cactus", 5, 90)
sun_flower = Plant("sunflower", 80, 45)
fern = Plant("fern", 15, 120)
print("=== Plant Factory output ===")
rose.show()
oak.show()
cactus.show()
sun_flower.show()
fern.show()
