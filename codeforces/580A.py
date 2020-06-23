def read_ints():
  temp = input()
  ints = [int(t) for t in temp.split(" ")]
  return ints

values = input()
values = read_ints()

curmax = 1
totalmax = 1
for i, value in enumerate(values):
  if i == 0:
    continue
  if value < values[i - 1]:
    totalmax = max(totalmax, curmax)
    curmax = 1
  else:
    curmax += 1

totalmax = max(totalmax, curmax)
print(totalmax)
