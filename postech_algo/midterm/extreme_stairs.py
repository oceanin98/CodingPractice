def extreme_stairs(n,m):
  stairs = [1,1,2]
  if n < 3:
    return stairs[n]

  for i in range(3, n+1):
    count = (stairs[0] + stairs[1] + stairs[2]) % m
    stairs[0] = stairs[1]
    stairs[1] = stairs[2]
    stairs[2] = count

  return stairs[-1]

def read_ints():
  temp = input().split()
  temp = [int(t) for t in temp]
  return temp

tests = int(input())

for _ in range(tests):
  n, m = read_ints()

  result = extreme_stairs(n,m)
  print(result)
