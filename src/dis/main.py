#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def sum_tender(count: int = 1_000_000) -> int:
    total = 0
    for n in range(count):
        total = total + n
    return total


def sum_terse(count: int = 1_000_000) -> int:
    return sum(range(count))


assert sum_tender() == sum_terse()
