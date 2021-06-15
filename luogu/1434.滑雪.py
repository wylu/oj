#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   1434.滑雪.py
@Time    :   2021/06/14 21:34:53
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
from functools import lru_cache


def solve():
    m, n = list(map(int, input().split()))
    mat = [None] * m
    for i in range(m):
        mat[i] = list(map(int, input().split()))

    d = (0, 1, 0, -1, 0)
    seen = [[False] * n for _ in range(m)]

    @lru_cache(None)
    def dfs(x, y):
        seen[x][y] = True
        res = 0
        for i in range(4):
            nx, ny = x + d[i], y + d[i + 1]
            if (nx < 0 or nx >= m or ny < 0 or ny >= n or seen[nx][ny]
                    or mat[x][y] <= mat[nx][ny]):
                continue
            res = max(res, dfs(nx, ny))
        seen[x][y] = False
        return res + 1

    ans = 0
    for i in range(m):
        for j in range(n):
            ans = max(ans, dfs(i, j))

    print(ans)


solve()
