#!/usr/bin/env python3


class Plant:
    def __init__(self, name: str, height: float, age: int):
        self.name = name
        self._height = 0 #"_" means protected
        self._age = 0       #protected

        self.set_age(age)
        self.set_height(height)

    def show(self)-> None:
         if self._age > 0 and self._height > 0:
            print(f"{self.name.capitalize()}: {self._height}cm, {self._age} days old")

    def grow(self)-> None:
        self._height += 0.512456

    def age_plant(self)-> None:
        self._age += 1


    def set_height(self, value: float):
        if value < 0:
            print("Plant height can not be NEGATIVE")
        self._height = value


    def get_height(self) -> float:
        return self._height


    def set_age(self, value: int):
        if value < 0:
            print("Age must be a positive value")
        self._age = value

    def get_age(self)-> int:
        return self._age



habibi = Plant("rose", -15, 30)
habibi.show()
