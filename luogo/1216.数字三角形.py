#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   1216.数字三角形.py
@Time    :   2021/06/14 11:30:13
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""


def solve():
    r = int(input())
    triangle = [None] * r
    for i in range(r):
        triangle[i] = list(map(int, input().split()))

    for row in range(r - 1, 0, -1):
        for col in range(row):
            triangle[row - 1][col] += max(triangle[row][col],
                                          triangle[row][col + 1])
    print(triangle[0][0])


solve()
