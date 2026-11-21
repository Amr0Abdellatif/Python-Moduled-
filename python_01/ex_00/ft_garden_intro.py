#!/usr/bin/env python3


def ft_garden_intro(name: str, height: int, age: int) -> None:
	print("=== Welcome to my Garden ===")
	print(f"Plant: {name.capitalize()}")
	print(f"Heigtht: {height}cm")
	print(f"Age: {age} days")
	print("\n=== End of Program ==")


print("this is a top level line\n")


if __name__ == "__main__":
	print("habibi test")
	ft_garden_intro("rose", 15, 30)
