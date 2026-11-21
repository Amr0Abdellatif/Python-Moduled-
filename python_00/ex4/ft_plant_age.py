#!/usr/bin/env python3


def ft_plant_age():
    age: str = input("Plant age in days: ")
    age_in_num = int(age)
    if age_in_num >= 0:
        if age_in_num > 60:
            print("Plant is ready to Harvest !")
        else:
            print("Plant needs more time to grow.")
    else:
        print("Enter a positive number !")


# ft_plant_age()
