#!/usr/bin/env python3


class Plant:
    def __init__(self, name: str, height: float, age: int):
        self.name = name
        self.height = height
        self.age = age

    def show(self) -> None:
        print(f"{self.name.capitalize()}: {self.height}cm, {self.age} days old")


if __name__ == "__main__" :
    flower = Plant("rose", 12.5, 53)
    flower.show()
