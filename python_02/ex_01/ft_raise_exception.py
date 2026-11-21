#!/usr/bin/env python3


def input_temperature(temp_str: str) -> int:
        return int(temp_str)



def test_temperature():
    input_result: str = input("Enter number: ")
    try:
        print("=== Garden temprature ===\n")
        print(f"Input data is {input_result}")
        reading: float = input_temperature(input_result)

        if reading > 40:
             raise ValueError(f"{reading}°C is too hot for plants (max 40°C)")
        elif reading < 0:
             raise ValueError(f"{reading}°C is too cold for plants (max 40°C)")

        print(f"Temprature is now {reading}°C")
    except ValueError as e:
        print(f"Caught input_temperature error: {e}")
    finally:
        print("\nAll tests complete - program didn't crash!")


if __name__ == "__main__":
     test_temperature()
