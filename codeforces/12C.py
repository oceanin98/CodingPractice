#https://codeforces.com/problemset/problem/12/C
#1100

n,m = [int(t) for t in input().split()]
tags = [int(t) for t in input().split()]

tags.sort() #ascending

fruits = {}
for _ in range(m):
    fruit = input()
    if fruit not in fruits:
        fruits[fruit] = 1
    else:
        fruits[fruit] += 1
    
counts = []
for k in fruits:
    counts.append(fruits[k])
counts.sort(reverse=True)

minimum = 0
for i in range(len(counts)):
    minimum += counts[i] * tags[i]
    
maximum = 0
for i in range(len(counts)):
    maximum += counts[i] * tags[len(tags) - i - 1]

print(minimum, maximum)
