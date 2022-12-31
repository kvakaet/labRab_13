#!usr/bin/env python3
# -*- coding: utf-8 -*-
from functools import reduce


def srd_gar(*args):
    if args:
        znm = list(map(lambda a: 1 / a, args))
        summa = reduce(lambda a, b: a + b, znm)
        gar = len(args) / summa
        return gar
    else:
        return None


if __name__ == '__main__':
    print(srd_gar(1, 2, 3, 4, 5, -10))
