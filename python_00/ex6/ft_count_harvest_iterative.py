#!/usr/bin/env python3


def ft_count_harvest_iterative():
    days_in: str = input("Days until harvest: ")
    days: int = int(days_in)

    if days < 1:
        print("Enter a number bigger than 0!")
        return
    for i in range(1, days + 1, 1):
        print("Day ", i)
    print("Harvest time!")
    return


# ft_count_harvest_iterative()
