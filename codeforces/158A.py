def read_ints():
  temp = input()
  ints = [int(t) for t in temp.split(" ")]
  return ints

n, k = read_ints()
scores = read_ints()
result = 0

for i in range(n):
  if i < k:
    if scores[i] > 0:
      result += 1
    else:
      break
  else:
    if scores[i] == scores[k - 1]:
      result += 1
    else:
      break
print(result)
