def read_ints():
  temp = input()
  ints = [int(t) for t in temp.split(" ")]
  return ints

N = int(input())
result = 0
for _ in range(N):
  certain = read_ints()
  if sum(certain) > 1:
    result += 1

print(result)
