n = int(input())

for i in range(n):
  len = int(input())
  positions = input().split()
  positions = [int(position) for position in positions]

  bestpos = positions[len//2]

  d = 0

  for pos in positions:
    if pos < bestpos:
      d = d + (bestpos - pos)
    else:
      d = d + (pos - bestpos)

  print(d)
