# 1100
# http://codeforces.com/problemset/problem/1375/A

t = int(input())

for _ in range(t):
  n = int(input())
  l = [int(t) for t in input().split()]

  for i , num in enumerate(l):
    if i % 2:
      if num > 0:
        l[i] *= -1
    else:
      if num < 0:
        l[i] *= -1
  
  print(*l)
