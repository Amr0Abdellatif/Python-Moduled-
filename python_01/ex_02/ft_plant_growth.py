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


print ("=== Garden Plant Growth ===")

flower = Plant("rose", 10.0, 5)
first_day = flower.height
for day in range(1, 8):
    print(f"=== Day {day} ===")
    flower.show()
    flower.grow()
    flower.age_plant()
print(f"Growth this week: {round(flower.height - first_day, 2)}cm")
