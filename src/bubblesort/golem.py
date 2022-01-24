#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    Random number generator from golem.de

    File:
    https://video.golem.de/download/26251

    Article:
    https://www.golem.de/news/programmiersprache-julia-wie-python-nur-schneller-2110-159760-2.html
"""

try:
    import src.bubblesort.random_number_list as random_number_list
except ModuleNotFoundError:
    import random_number_list as random_number_list

@profile
def bubble_sort(numbers: list) -> list:
    """ Default algorithm from Golem """
    size = len(numbers)
    for _ in range(size):
        for j in range(size - 1):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
    return numbers


if __name__ == "__main__":
    bubble_sort(numbers=random_number_list.read())
