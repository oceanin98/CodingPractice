#https://codeforces.com/problemset/problem/158/B

n = int(input())
children = [int(t) for t in input().split()]

count = [0] * 4

for c in children:
    count[c - 1] += 1

result = count[3] + count[2]
count[0] -= count[2] # deduct by the number of 3s, may become negative here
result += count[1] // 2

if count[1] % 2 == 1:
    result += 1
    count[0] -= 2

if count[0] > 0:
    result += (count[0] + 3) // 4

print(result)
