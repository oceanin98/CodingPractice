def read_ints():
  raw = input().split()
  return [int(r) for r in raw]

n = int(input())

for i in range(n):
  laps, cars = read_ints()
  sequence = read_ints()

  initial = [-1] * 1000001
  count = 0

  # identify initial sequence
  for s in sequence:
    if initial[s] == -1:
      initial[s] = count
      count += 1

    if count == cars:
      break

  temp = [0] * (cars + 1)
  temp[0] = laps

  statement = "NO"

  for s in sequence:
    if initial[s] == 0: # if initially first position
      temp[0] -= 1
      temp[1] += 1
    else:
      if temp[initial[s]] > 0:
        temp[initial[s]] -= 1
        temp[initial[s] + 1] += 1
      else:
        statement = "YES"
        break

  print(statement)
