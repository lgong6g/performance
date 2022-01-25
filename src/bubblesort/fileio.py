#!/usr/bin/env python3
# -*- coding: utf-8 -*-

try:
    import src.bubblesort.random_number_list as random_number_list
except ModuleNotFoundError:
    import random_number_list as random_number_list


if __name__ == "__main__":
  for i in range(1000):
    random_number_list.create(path='data/fileio/' + str(i) + '.txt')
    random_number_list.read(path='data/fileio/' + str(i) + '.txt')
