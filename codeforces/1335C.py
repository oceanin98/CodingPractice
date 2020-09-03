# 1100
# http://codeforces.com/problemset/problem/1335/C

t = int(input())

for _ in range(t):
  n = int(input())
  l = [int(t) for t in input().split()]

  l.sort()
  
  distincts = 1
  max_sames = 1
  sames = 1
  for i, num in enumerate(l):
    if i == 0:
      continue
    if num == l[i-1]:
      sames += 1
    else:
      max_sames = max(max_sames, sames)
      sames = 1
      distincts += 1
  
  max_sames = max(max_sames, sames)
  if distincts == max_sames:
    max_sames -= 1
    
  result = min(distincts, max_sames)
  print(result)      
    
