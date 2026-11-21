#!/usr/bin/env python3


import sys


def parse_dictionary(habibi_input: list)-> list:
    result = []

    for token in habibi_input:
        try:
            component = token.split(':')
            if len(component) != 2:
                raise ValueError("Input formate error: '<item>:<quantity>'")
            component[1] = int(component[1])
            result = result + [component]
        except ValueError as e:
            print(f"{e}")

    return result


def delete_duplicate(dic_lst: list) -> dict:
    i: int = 0
    j: int = 0
    lenght = len(dic_lst) - 1

    while i < lenght:
        j = i
        while j < lenght:
            if dic_lst[i][0] == dic_lst[j + 1][0]:
                print(f"Redundant item '{dic_lst[i][0]}' - discarting")
                del dic_lst[j + 1]
                lenght -= 1
            j += 1
        i += 1

    return dic_lst


def sum_quantity(dict_lst: list) -> int:
    total :int = 0

    for item in dict_lst:
        total += item[1]

    return total


def inventory_sys():
    habibi_input = sys.argv[1:].copy()
    habibi_out = parse_dictionary(habibi_input)

    new_dic = delete_duplicate(habibi_out)
    print(new_dic)
    quantity = sum_quantity(new_dic)
    print(f"Total quantity of the {len(new_dic)} items: {quantity}")
    for item in new_dic:
        print(f"Item '{item[0]}' represent {round(item[1] / quantity * 100, 1)}%")


if __name__ == "__main__":
    print("=== Inventory System Analysis ===")
    inventory_sys()
