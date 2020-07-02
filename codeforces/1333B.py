# https://codeforces.com/problemset/problem/1333/B
# 1100


t = int(input())

for _ in range(t):
    n = int(input())
    a = [int(t) for t in input().split()]
    b = [int(t) for t in input().split()]

    plus = False
    minus = False
    result = "YES"
    for i in range(n):
        if plus and minus:
            break
        if a[i] == b[i]:
            if a[i] == 1:
                plus = True
                continue
            elif a[i] == -1:
                minus = True
                continue
        elif a[i] > b[i]:
            if not minus:
                result = "NO"
                break
            if a[i] == 1:
                plus = True 
        else:
            if not plus:
                result = "NO"
                break
            if a[i] == -1:
                minus = True
    print(result)
