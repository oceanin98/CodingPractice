# 1100
# http://codeforces.com/problemset/problem/313/B

# Flipping the order of t = int(input()) and the calc part incurs time limit

s = input()
t = int(input())

calc = [0] * len(s)
for i, _ in enumerate(s):
    if i == 0:
        continue
    if s[i] == s[i - 1]:
        calc[i] = 1 + calc[i - 1]
    else:
        calc[i] = calc[i - 1]

for _ in range(t):
    l, r = [int(t) for t in input().split()]
    print(calc[r-1] - calc[l-1])
