# 1100
# http://codeforces.com/problemset/problem/1334/B

t = int(input())

for _ in range(t):
  n, x = [int(t) for t in input().split()]
  l = [int(t) for t in input().split()]

  l.sort(reverse=True)
  
  total = 0
  count = 0
  for i, num in enumerate(l):
    total += num  
    if total /(i + 1) >= x:
      count += 1
    else:
      break
    
  print(x, count)
