import heapq

def read_ints():
  temp = input().split()
  temp = [int(t) for t in temp]
  return temp

tests = int(input())

for _ in range(tests):
  n = int(input())

  levent = []

  for _ in range(n):
    l, r, y = read_ints()
    levent.append([l,1,y])
    levent.append([r,0,y])

  levent.sort()
  curx = levent[0][0]
  xevent = []
  perx = []
  for e in levent:
    if e[0] == curx:
      perx.append(e)
    else:
      xevent.append(perx)
      perx = [e]
      curx = e[0]
  
  xevent.append(perx)

  top_hull = []
  positions = []
  for x in xevent:
    for e in x:
      if e[1] == 1:
        heapq.heappush(top_hull, -e[2])
      else:
        top_hull.remove(-e[2])
        heapq.heapify(top_hull)
    if len(top_hull) == 0:
      positions.append([e[0], 0])
    else:
      positions.append([e[0], -top_hull[0]])


  top_hull = []
  curx, cury = positions[0]

  for p in positions[1:]:
    if cury == -1:
      curx, cury = p

    if p[1] == cury:
      continue
    elif p[1] == 0:
      top_hull.append([curx, p[0], cury])
      cury = -1
    else:
      top_hull.append([curx, p[0], cury])
      curx, cury = p

  for segment in top_hull:
    print(*segment, sep=" ")

