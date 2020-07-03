# http://codeforces.com/problemset/problem/492/B
# 1200

n,l = [int(t) for t in input().split()]
pos = [int(t) for t in input().split()]

pos.sort()

maxdistance = max(l - pos[-1], pos[0]) * 2
for i in range(1,n):
    if pos[i] - pos[i - 1] > maxdistance:
        maxdistance = pos[i] - pos[i - 1]

print((maxdistance) / 2)
