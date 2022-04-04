/**
 * @File    :   树状数组.cpp
 * @Time    :   2022/04/04 10:25:02
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :   https://oi-wiki.org/ds/fenwick/
 * 
 * 树状数组和线段树具有相似的功能，但他俩毕竟还有一些区别：
 * 
 * 树状数组能有的操作，线段树一定有；线段树有的操作，树状数组不一定有。
 * 但是树状数组的代码要比线段树短，思维更清晰，速度也更快，
 * 在解决一些单点修改的问题时，树状数组是不二之选。
 * 
 * 应用场景：
 * 
 * 1.一维树状数组的应用场景
 *   1.1单点修改 + 区间查询
 *   1.2区间修改 + 单点查询
 *   1.3区间修改 + 区间查询
 *   1.4树状数组其他神奇操作
 *      1.4.1求逆序对数量
 * 
 * 2.二维树状数组
 *   2.1单点修改 + 二维区间查询
 *   2.1二维区间修改 + 单点查询
 *   2.1二维区间修改 + 二维区间查询
 * 
 * 
 * https://www.bilibili.com/video/BV1Hz411v7XC?p=2
 * https://blog.csdn.net/qq_47549346/article/details/117783536
 */

#include <bits/stdc++.h>
using namespace std;

int n = 8;
vector<int> c(n + 1);
vector<int> a{0, 1, 2, 3, 4, 5, 6, 7, 8};

int lowbit(int x) {
    return x & -x;
    // return x & (~x + 1);
}

void add(int i, int v) {
    while (i <= n) {
        c[i] += v;
        i += lowbit(i);
    }
}

int getsum(int i) {
    int sum = 0;
    while (i) {
        sum += c[i];
        i -= lowbit(i);
    }
    return sum;
}

void init() {
    for (int i = 1; i <= n; i++) {
        c[i] += a[i];
        int j = i + lowbit(i);
        if (j <= n) c[j] += c[i];
    }
}

void printVectorInt(vector<int>& vct) {
    printf("[");
    int n = vct.size();
    if (n > 0) printf("%d", vct[0]);
    for (int i = 1; i < n; i++) printf(",%d", vct[i]);
    printf("]\n");
}

int main(int argc, char const* argv[]) {
    printVectorInt(c);
    init();
    printVectorInt(c);
    return 0;
}
