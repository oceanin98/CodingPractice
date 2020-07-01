#https://codeforces.com/problemset/problem/82/A
# A-level mathematics should be revised
# At least C1~C6, M1~2, S1~3

import math

n = int(input())

names = ["Sheldon","Leonard","Penny","Rajesh","Howard"]
turn = math.ceil(math.log2(n/5 + 1))
n -= 5 * (2 ** (turn - 1) - 1)
each = 2 ** (turn - 1)

print(names[math.ceil(n/each) - 1])
