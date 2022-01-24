import random


def create(path: str = 'data/random_numbers.txt',
           min_value: int = -1_000,
           max_value: int = 1_000,
           quantity: int = 10_000) -> None:

    # Create random number list
    random_numbers = [random.uniform(min_value, max_value) for _ in range(quantity)]

    with open(path, 'w', encoding="utf-8") as filehandle:
        filehandle.writelines("%s\n" % number for number in random_numbers)


def read(path: str = 'data/random_numbers.txt') -> list:
    # open file and read the content in a list
    with open(path, 'r', encoding="utf-8") as filehandle:
        random_numbers = [current_number.rstrip() for current_number in filehandle.readlines()]

    return random_numbers
