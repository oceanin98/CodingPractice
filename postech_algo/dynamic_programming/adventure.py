def read_ints():
  temp = input().split()
  temp = [int(t) for t in 

temp]
  return temp

def max_fish(fish):
  fish.sort(key=lambda x: 

x[0])
  cur_x = 0
  real_x = fish[0][0]

  for f in fish:
    if f[0] == real_x:
      f[0] = cur_x
    else:
      cur_x += 1
      real_x = f[0]
      f[0] = cur_x

  fish.sort(key=lambda x: 

x[1])
  cur_y = 0
  real_y = fish[0][1]

  for f in fish:
    if f[1] == real_y:
      f[1] = cur_y
    else:
      cur_y += 1
      real_y = f[1]
      f[1] = cur_y

  antarctic = [[0] * 

(cur_x+1) for _ in range

(cur_y+1)]
  for f in fish:
    antarctic[f[1]][f[0]] 

= 1

  for i in range(1, len

(antarctic[0])):
    antarctic[0][i] = 

antarctic[0][i] + 

antarctic[0][i - 1]

  for i in range(1, len

(antarctic)):
    for j in range(len

(antarctic[0])):
      if j == 0:
        antarctic[i][j] += 

antarctic[i-1][j]
      else:
        antarctic[i][j] += 

max(antarctic[i-1][j], 

antarctic[i][j-1])

  return antarctic[-1][-1]

tests = int(input())

for _ in range(tests):
  N = int(input())

  fish = []
  for _ in range(N):
    x, y = read_ints()
    fish.append([x,y])
  result = max_fish(fish)
  
  print(result)
