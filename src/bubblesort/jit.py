#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
from numba import njit


@njit()
def bubble_sort(numbers: np.array) -> list:
    """ Optimized bubble sort algorithm - check if items at the end were already swapped"""
    swapped = True
    iterations = 0

    while swapped:

        swapped = False

        for i in range(len(numbers) - iterations - 1):
            if numbers[i] > numbers[i + 1]:
                numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
                swapped = True

        iterations += 1

        # print("Number of iterations: ", iterations)

    return numbers


if __name__ == "__main__":
    # Deprecation of reflection for List and Set types
    # https://numba.pydata.org/numba-doc/latest/reference/deprecation.html#deprecation-of-reflection-for-list-and-set-types
    random_numbers = np.loadtxt('data/random_numbers.txt')
    bubble_sort(numbers=random_numbers)
