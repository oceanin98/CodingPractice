def read_ints():
  temp = input()
  ints = [int(t) for t in temp.split(" ")]
  return ints

N = int(input())

for _ in range(N):
  n,m,k = read_ints()
  per_player = n//k

  if per_player >= m:
    print(m)
  else:
    m -= per_player
    minmax = m // (k - 1)
    if m % (k - 1):
      minmax += 1
    print(per_player - minmax)
