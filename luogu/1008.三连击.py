#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   1008.三连击.py
@Time    :   2021/06/14 11:04:00
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""


def solve():
    NUMBERS = [str(num) for num in range(1, 10)]

    for i in range(1, 10):
        seen = {i}

        for j in range(1, 10):
            if j in seen:
                continue
            seen.add(j)

            for k in range(1, 10):
                if k in seen:
                    continue
                seen.add(k)
                num1 = (i * 10 + j) * 10 + k
                num2 = num1 * 2
                num3 = num1 * 3
                ans = list(str(num1)) + list(str(num2)) + list(str(num3))
                ans.sort()
                if ans == NUMBERS:
                    print(num1, num2, num3)

                seen.discard(k)

            seen.discard(j)

        seen.discard(i)


solve()
