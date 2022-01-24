#!/usr/bin/env python3
# -*- coding: utf-8 -*-

try:
    import src.bubblesort.random_number_list as random_number_list
except ModuleNotFoundError:
    import random_number_list as random_number_list


def bubble_sort(numbers: list) -> list:
    [[numbers.insert(j + 1, numbers.pop(j)) for j in range(i) if numbers[j] > numbers[j + 1]] for i in
     range(len(numbers) - 1, 0, -1)]
    return numbers


if __name__ == "__main__":
    bubble_sort(numbers=random_number_list.read())
