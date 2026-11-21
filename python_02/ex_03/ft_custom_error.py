#!/usr/bin/env python3


class GardenError(Exception):
    def __init__(self, message):
        super().__init__(message)



class PlantError(GardenError):
    pass



class WaterError(GardenError):
    pass



def test_garden_errors():
    in_water_level: str = input("Enter water level: ")
    water_level: int = int(in_water_level)

    in_age: str = input("Enter plant age: ")
    age: int = int(in_age)

    water_error: int = 0
    age_error: int = 0
    try:
        print("testing Water error.....")
        if water_level < 100:
            water_error = -1
            raise WaterError("Not enough water in the tank\n")
        else:
            print("water levels are fine!")
    except WaterError as e:
        print(f"Caught Water error: {e}")


    try:
        print("testing plant error.....")
        if age > 30:
            age_error = -1
            raise PlantError("The tomato is wilting!\n")
        else:
            print("tomato is healthy")
    except PlantError as e:
        print(f"Caught Plant error {e}")


    except GardenError as e:
        print("Caught garden error: {e}")


    print("Testing catching all garden errors...")
    try:
        if age_error == -1:
            raise GardenError("The tomato is wilting!")
    except GardenError as e:
        print(f"Caught gardern error: {e}")

    try:
        if water_error == -1:
            raise GardenError("The tomato is wilting!")
    except GardenError as e:
        print(f"Caught gardern error: {e}")

    finally:
        print("\nAll custom error types work correctly!")


test_garden_errors()
