#!/usr/bin/env python3

class GardenError(Exception):
    def __init__(self, message):
        super().__init__(message)



class PlantError(GardenError):
    pass



class WaterError(GardenError):
    pass


def water_plant(plant_name: str):
    tmp_name= plant_name
    new_name = plant_name.capitalize()

    if new_name == tmp_name:
        print(f"success plant name {tmp_name} is [OK]")
    else:
        raise PlantError(f"invalid plant name: '{tmp_name}'")


if __name__== "__main__":
    plants: str = ["Tomato", "Carrots", "Cucumber", "lettus", "Banana"]

    try:
        water_plant(plants[0])
        water_plant(plants[1])
        water_plant(plants[2])
        water_plant(plants[3])
        water_plant(plants[4])
    except PlantError as e:
        print(f"Caught PlantError: {e}")
    finally:
        print("Closing watering system\n")
        print("clean up done!")
