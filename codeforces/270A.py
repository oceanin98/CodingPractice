# https://codeforces.com/problemset/problem/270/A

n = int(input())

for _ in range(n):
    angle = int(input())
    if 360 % (180 - angle) == 0:
        print("YES")
    else:
        print("NO")
