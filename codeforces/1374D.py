# https://codeforces.com/problemset/problem/1374/D
# 1400
# There may always be an easier and faster way

t = int(input())

for _ in range(t):
    n, k = [int(t) for t in input().split()]
    numbers = [int(t) for t in input().split()]

    remainders = {}

    for num in numbers:
        if num % k == 0:
            continue
        if k - (num % k) not in remainders:
            remainders[k - (num % k)] = 0
        remainders[k - (num % k)] += 1
    
    maxvalue = 0
    maxkey = 0
    for key in remainders:
        if remainders[key] == maxvalue:
            maxkey = max(key, maxkey)
        elif remainders[key] > maxvalue:
            maxkey = key
            maxvalue = remainders[key]

    result = (maxvalue - 1) * k + maxkey + 1
    if maxvalue == 0:
        result = 0
    print(result)
