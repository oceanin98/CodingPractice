#https://codeforces.com/problemset/problem/1345/B
#1100

import math
t = int(input())

for _ in range(t):
    cards = int(input())
    total = 0
    while cards > 1:
        height = math.floor((-1 + math.sqrt(1 + 12*2*cards)) / 6)
        cards -= height*(3*height + 1) // 2
        total += 1
    print(total)
