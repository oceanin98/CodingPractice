# 1100
# http://codeforces.com/problemset/problem/1327/A

t = int(input())

for _ in range(t):
  n, k = [int(t) for t in input().split()]
  if n % 2 != k % 2:
    print("NO")
    continue

  if k * (2 + (k - 1) * 2) // 2 > n:
    print("NO")
  else:
    print("YES")
