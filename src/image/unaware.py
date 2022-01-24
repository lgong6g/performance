#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg


def overwrite_partially_flagged_pixel_with_zeros_slow(array: np.array, high_bit: int) -> np.array:
    """ Replace all values smaller than high bit with 0"""
    for i, x in enumerate(array):
        for j, y in enumerate(x):
            for k, z in enumerate(y):
                if z < high_bit:
                    array[i, j, k] = 0
    return array


if __name__ == "__main__":
    img = mpimg.imread('data/example.jpg')
    arr = np.array(img)
    imgplot = plt.imshow(arr)
    plt.show()

    overwrite = overwrite_partially_flagged_pixel_with_zeros_slow(array=arr.copy(), high_bit=200)

    imgplot2 = plt.imshow(overwrite)
    plt.show()




