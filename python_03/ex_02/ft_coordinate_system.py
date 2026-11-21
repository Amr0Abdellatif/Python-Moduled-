#!/usr/bin/env python3

import math

def parse_input(in_usr: str)-> list[float]:
    in_coordinates = in_usr.split(',')
    lst_len = len(in_coordinates)
    i :int = 0
    valid_input: int = 0
    while i < lst_len:
        float(in_coordinates[i])
        valid_input += 1
        i += 1
    if valid_input != 3:
        raise ValueError("invalid syntax: coordinates as float formate 'x,y,z' formate")
    coordinates: list[float] = 3 * [None]
    for x in range(3):
        coordinates[x] = float(in_coordinates[x])
    return coordinates

def calculate_distance(first_coordinate: list[float], second_coordinate: list[float]) ->float:
    x1 = first_coordinate[0]
    y1 = first_coordinate[1]
    z1 = first_coordinate[2]

    x2 = second_coordinate[0]
    y2 = second_coordinate[1]
    z2 = second_coordinate[2]

    return math.sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2)


def get_player_position()-> list[float]:
    try_again: int = 0
    world_center: list[float] = [0, 0, 0]

    while try_again == 0:
        try:
            in_usr: str = input("Enter new coordinates as floats in format 'x,y,z': ")
            coordinates: list = parse_input(in_usr)
            print(f"Got a first tuple: {coordinates}")
            print(f"It includes: X={coordinates[0]}" \
                  f", Y={coordinates[1]}, Z={coordinates[2]}")
            print(f"Distance to center:{round(calculate_distance(world_center, coordinates),4)}")
            try_again = 1
        except ValueError as e:
            print(f"{e}\n")
    return coordinates

if __name__ == "__main__":
    print("Get a first set of coordinates:")
    player_1_coordinates = get_player_position()
    print("\nGet a second set of coordinates:")
    player_2_coordinates = get_player_position()

    ditance_between: float = calculate_distance(player_2_coordinates, player_1_coordinates)
    print(f"\nDistance between the two coordinates= {round(ditance_between, 4)}")
