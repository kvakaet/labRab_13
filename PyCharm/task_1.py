#!usr/bin/env python3
# -*- coding: utf-8 -*-
from functools import reduce


def arif(*args):
    if args:
        prod = reduce(lambda a, b: a * b, args)
        return pow(prod, 0.5)
    else:
        return None


if __name__ == '__main__':
    print(arif(2, 5, 10))
