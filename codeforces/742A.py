def read_ints():
  temp = input()
  ints = [int(t) for t in temp.split(" ")]
  return ints

N = int(input())

mod = N % 4

result = [6,8,4,2][mod]
if N == 0:
  result = 1

print(result)
