#!/usr/bin/env python3


def input_temperature(temp_str: str) -> int:
        return int(temp_str)



def test_temperature():
    input_result: str = input("Enter number: ")
    try:
        reading = input_temperature(input_result)
        print("=== Garden temprature ===\n")
        print(f"Input data is {input_result}")
        print(f"Temprature is now {reading}°C")
    except:
        print(f"Input data is '{input_result}'")
        print(f"Caught input_temperature error:"
              f" invalid literal for int() with base 10: '{input_result}'")
    finally:
        print("\nAll tests complete - program didn't crash!")


test_temperature()
