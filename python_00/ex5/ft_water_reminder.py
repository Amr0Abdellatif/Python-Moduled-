#!/usr/bin/env python3


def ft_water_reminder():
    days_in: str = input("Days since last watering: ")
    days: int = int(days_in)

    if days >= 0:
        if days > 2:
            print("Water the plants!")
        else:
            print("Plants are fine.")
    else:
        print("Enter positive number!")


# ft_water_reminder()
