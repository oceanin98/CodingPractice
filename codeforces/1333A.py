# https://codeforces.com/problemset/problem/1333/A

def read_ints():
  temp = input()
  ints = [int(t) for t in temp.split(" ")]
  return ints

N = int(input())
for _ in range(N):
  n, m = read_ints()

  base = ['B','W'] * 51
  to_black = (0,0)
  if m % 2 == 0:
    to_black = (0, m-1)
  elif n % 2 == 0:
    to_black = (n-1, 0)
  
  for i in range(n):
    s = i % 2
    to_print = base[s:s+m]
    if i == to_black[0]:
      to_print[to_black[1]] = 'B'
    print("".join(to_print))
