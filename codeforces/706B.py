# https://codeforces.com/problemset/problem/706/B
# WAS NOT AWARE THAT equal coke prices could exist
# BISECT turned out to be an excellent library for implementing upper/lower bounds. STUDY

import bisect

n = int(input())
prices = [int(t) for t in input().split()]
q = int(input())

prices.sort()

for _ in range(q):
    m = int(input())
    if m >= prices[-1]:
        print(n)
        continue
    if m < prices[0]:
        print(0)
        continue
    result = bisect.bisect_right(prices, m)
    print(result)
