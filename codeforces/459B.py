# http://codeforces.com/problemset/problem/459/B
# 1300

n = int(input())
b = [int(t) for t in input().split()]

minb = b[0]
mincount = 1
maxb = b[0]
maxcount = 1
for i in b[1:]:
    if i < minb:
        minb = i
        mincount = 1
    elif i > maxb:
        maxb = i
        maxcount = 1
    else:
        if i == minb:
            mincount += 1
        if i == maxb:
            maxcount += 1
    
possibilities = mincount * maxcount
if maxb == minb:
    possibilities = maxcount * (maxcount - 1) // 2
print(maxb - minb, possibilities)
