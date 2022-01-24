#!/usr/bin/env python3
# -*- coding: utf-8 -*-

try:
    import src.bubblesort.random_number_list as random_number_list
except ModuleNotFoundError:
    import random_number_list as random_number_list


@profile
def bubble_sort(numbers: list) -> list:
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
    bubble_sort(numbers=random_number_list.read())
