# Linear Programming
# https://codeforces.com/problemset/problem/1366/A

def read_ints():
    temp = input().split()
    ints = [int(t) for t in temp]
    return ints

t = int(input())

for _ in range(t):
    result = 0
    a, b = read_ints()

    if not a or not b:
        result = 0
    elif a >= 2*b or b >= 2*a:
        result = min(a,b)
    else:
        result = (a + b) // 3
    
    print(result)
