#!/usr/bin/env python3

import typing


def test():
    print("A")
    yield 1
    print("B")
    yield 2
    print("C")
    yield 3

g = test()

next(g)
next(g)
next(g)

def test_two():
    print("H")
    yield 1
    print("A")
    yield 2
    print("B")
    yield 3
    print("I")
    yield 4
    print("B")
    yield 5
    print("I")
    yield 6


gen = test_two()

for i in gen:
    pass
