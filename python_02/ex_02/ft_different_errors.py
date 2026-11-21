#!/usr/bin/env python3


def garden_operations(operation_number: int):
    if operation_number == 0:
        print("Testing operation 0...")
        val = int("abc")
    elif operation_number == 1:
        print("Testing operation 1...")
        x :float = 5 / 0
    elif operation_number == 2:
        print("Testing operation 2...")
        open("habibi.txt")
    elif operation_number == 3:
        print("Testing operation 3...")
        wrong_typ: str = "12a"
        y :int = int(wrong_typ)
    else:
        print("Testing operation 4...")
        print("Operation completed successfully\n")


def test_error_type():
    for i in range(0, 5):
        try:
            garden_operations(i)
        except ValueError as e:
            print(f"Caught ValueError: {e}\n")
        except ZeroDivisionError as e:
            print(f"Caught ValueError: {e}\n")
        except FileNotFoundError as e:
            print(f"Caught ValueError: {e}\n")
        except TypeError as e:
            print(f"Caught ValueError: {e}\n")

    print("All error types tested successfully!")


if __name__ == "__main__":
    test_error_type()
