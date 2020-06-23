def read_ints():
  temp = input()
  ints = [int(t) for t in temp.split(" ")]
  return ints

n, k = read_ints()
odds = (n + 1) // 2

if odds < k: # k is even
  print(2 * (k - odds))
else:
  print(1 + 2 * (k - 1))
