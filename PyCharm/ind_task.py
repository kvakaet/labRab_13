#!usr/bin/env python3
# -*- coding: utf-8 -*-


def summa(*args):
    fnl = 0
    for i, item in enumerate(args[::-1]):
        if item > 0:
            fnl = i
            break
    return sum(args[:fnl])


if __name__ == '__main__':
    print(summa(1, 2, 3, -4, -5, -10))
