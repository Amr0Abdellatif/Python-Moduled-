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
        self._height += 2.1

    def age_plant(self)-> None:
        self._age += 1


    def set_height(self, value: float):
        if value < 0:
            print("Plant height can not be NEGATIVE")
            return
        self._height = value


    def get_height(self) -> float:
        return self._height


    def set_age(self, value: int):
        if value < 0:
            print("Age must be a positive value")
            return
        self._age = value

    def get_age(self)-> int:
        return self._age


class Flower(Plant):
    def __init__(self, name: str, height: float, age: int, color: str):
        super().__init__(name, height, age)
        self.color = color

    def show(self):
        print("=== Flower")
        super().show()
        print(f"Color: {self.color}")


    def bloom(self):
        print("[asking the rose to bloom]")
        self.show()
        print("Rose is blooming beautifully!")


class Tree(Plant):
    def __init__(self, name: str, height: float, age: int, trunk_diameter: float):
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter


    def show(self):
        print("=== Tree")
        super().show()
        print(f"Trunk diameter: {self.trunk_diameter}")


    def produce_shade(self):
        print("[asking the oak to produce shade]")
        print(f"Tree Oak now produces a shade of {self._height}cm "
              f"long and {self.trunk_diameter}cm wide.")


class Vegetable(Plant):
    def __init__(self, name: str, height: float, age: int, harvest_season: str, nutrational_value: int):
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutrational_value = nutrational_value


    def show(self):
        print("== Vegetables")
        super().show()
        print(f"Harvest season: {self.harvest_season}")
        print(f"Nutrational value: {self.nutrational_value}")


    def grow(self, days: int):
        print("[make tomato grow and age for 20 days]")
        for day in range(days + 1):
            super().grow()
            super().age_plant()
        print(f"Harvest season: {self.harvest_season}")
        print(f"Nutrational value: {self.nutrational_value + day}")



if __name__ == "__main__":
    print("=== Garden Plant Types ===")
    rosa = Flower("rose", 15, 10, "red")
    rosa.show()
    rosa.bloom()

    print("\n\n")
    oak = Tree("oak", 200, 365, 5)
    oak.show()
    oak.produce_shade()

    print("\n\n")
    tomato = Vegetable("tomato", 5, 10, "April", 0)
    tomato.show()
    tomato.grow(20)
