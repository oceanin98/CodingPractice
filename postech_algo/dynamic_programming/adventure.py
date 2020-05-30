def read_ints():
  temp = input().split()
  temp = [int(t) for t in temp]
  return temp

def max_fish(fish, N):
  fish.sort(key=lambda x: x[0])
  cur_x = 0
  real_x = fish[0][0]

  for f in fish:
    if f[0] == real_x:
      f[0] = cur_x
    else:
      cur_x += 1
      real_x = f[0]
      f[0] = cur_x

  fish.sort(key=lambda x: x[1])
  cur_y = 0
  real_y = fish[0][1]

  for f in fish:
    if f[1] == real_y:
      f[1] = cur_y
    else:
      cur_y += 1
      real_y = f[1]
      f[1] = cur_y

  antarctic = [0] * (cur_x+2)
  fidx = 0
  
  for i in range(cur_y + 1):
    for j in range(1,cur_x + 2):
      antarctic[j] = max(antarctic[j], antarctic[j-1])
      if fidx < N:
        if fish[fidx][1] == i and fish[fidx][0] == j-1:
          antarctic[j] += 1
          fidx += 1

  return antarctic[-1]

tests = int(input())

for _ in range(tests):
  N = int(input())

  fish = []
  for _ in range(N):
    x, y = read_ints()
    fish.append([x,y])
  result = max_fish(fish, N)
  
  print(result)
