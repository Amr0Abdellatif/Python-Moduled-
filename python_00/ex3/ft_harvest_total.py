#!/usr/bin/env python3


def ft_harvest_total():
    first_input: str = input("Day one Harvest: ")
    second_input: str = input("Day two Harvest: ")
    third_input: str = input("Day three Harvest: ")

    day_one: int = int(first_input)
    day_two: int = int(second_input)
    day_three: int = int(third_input)

    result: int = day_one + day_two + day_three
    print("Total harvest: ", result)


# ft_harvest_total()
