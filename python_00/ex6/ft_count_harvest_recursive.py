#!/usr/bin/env python3

"""
#recursion using seperate helper function

def helper(day, total):
    if day > total:
        return
    print("Day: ", day)
    helper(day + 1, total)

def	ft_count_harvest_recursive():
    num_in :str = input("Days until harvest :")
    days :int = int(num_in)
    helper(1, days)
    print("Harvest time!")

ft_count_harvest_recursive()

"""

# recursion using nested helper function


def ft_count_harvest_recursive():
    num_in: str = input("Days until harvest: ")
    days: int = int(num_in)

    def helper(day: int):
        if day > days:
            return
        print("Day: ", day)
        helper(day + 1)
    helper(1)
    print("Harvest time!")


# ft_count_harvest_recursive()
