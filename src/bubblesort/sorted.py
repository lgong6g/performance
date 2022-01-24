#!/usr/bin/env python3
# -*- coding: utf-8 -*-

try:
    import src.bubblesort.random_number_list as random_number_list
except ModuleNotFoundError:
    import random_number_list as random_number_list


def python_internal_sorted(numbers: list) -> list:
    return sorted(numbers)


if __name__ == "__main__":
    python_internal_sorted(numbers=random_number_list.read())
