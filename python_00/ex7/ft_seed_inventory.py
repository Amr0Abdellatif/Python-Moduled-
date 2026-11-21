#!/usr/bin/env python3


def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    if unit == "packets":
        print(seed_type.capitalize(), "seeds:",
              quantity, unit, "availble", sep=' ')
    elif unit == "grams":
        print(seed_type.capitalize(), "seeds:",
              quantity, unit, "total", sep=' ')
    elif unit == "area":
        print(seed_type.capitalize(), "seeds:", "covers",
              quantity, "square meters", sep=' ')
    else:
        print("Unknown unit type")


""" ft_seed_inventory("tomato", 15, "packets")
ft_seed_inventory("carrot", 8, "grams")
ft_seed_inventory("lettus", 12, "area") """
