import math

def read_ints():
  raw = input().split()
  return [int(r) for r in raw]

def merge_sort(points):
  length = len(points) 
  if length < 2:
    return
  
  midpoint = length // 2
  left, right = points[:midpoint], points[midpoint:]

  merge_sort(left)
  merge_sort(right)

  l = 0
  r = 0
  t = 0

  while l < len(left) and r < len(right):
    if left[l][2] < right[r][2]:
      points[t] = left[l]
      l += 1
      t += 1
    elif left[l][2] > right[r][2]:
      points[t] = right[r]
      r += 1
      t += 1
    else:
      if math.fabs(left[l][0]) + math.fabs(left[l][1]) < math.fabs(right[r][0]) + math.fabs(right[r][1]):
        points[t] = left[l]
        l += 1
        t += 1
      else:
        points[t] = right[r]
        r += 1
        t += 1

  if l < len(left):
    while l < len(left):
      points[t] = left[l]
      l += 1
      t += 1
  else:
    while r < len(right):
      points[t] = right[r]
      r += 1
      t += 1

n = int(input())

for i in range(n):
  num = int(input())

  points = []
  for j in range(num):
    x, y = read_ints()
    points.append([x, y, -math.atan2(x, -y)])

  merge_sort(points)
  
  for p in points:
    print(p[0], p[1])
  
  print()
