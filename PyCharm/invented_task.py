#!usr/bin/env python3
# -*- coding: utf-8 -*-


def rvrs(*args):
    return list(reversed(args))


if __name__ == '__main__':
    lst = [int(i) for i in input('введите список цифр\n').split()]
    print(*rvrs(*lst))
