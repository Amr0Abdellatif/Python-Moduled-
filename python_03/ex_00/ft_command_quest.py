#!/usr/bin/env python3


import sys

if __name__ == "__main__":
    habibi = sys.argv
    num_args = len(habibi) - 1
    i: int = 0
    print("=== Command Quest ===")
    print(f"Program name: {habibi[0]}")
    if num_args == 0:
        print("No arguments provided!")
    else:
        print(f"Arguments recieved: {num_args - 1}")
        while i < num_args:
            print(f"Argument {i + 1}: {habibi[i + 1]}")
            i += 1
    print(f"Total Arguments: {num_args}")
