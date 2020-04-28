def read_ints():
  temp = input().split()
  temp = [int(i) for i in temp]
  return temp

def binary_search(numbers, l, r, q):
  if r < l:
    if r < 0:
      return numbers[l]
    elif l == len(numbers):
      return numbers[r]
    else:
      if numbers[l] - q < q - numbers[r]:
        return numbers[l]
      else:
        return numbers[r]
  else:
    m = (l + r) // 2

    if numbers[m] == q:
      return numbers[m]
    elif numbers[m] > q:
      return binary_search(numbers, l, m-1, q)
    else:
      return binary_search(numbers, m+1, r, q)

tests = int(input())

for _ in range(tests):
  n,m = read_ints()
  numbers = read_ints()
  queries = read_ints()

  result = []
  for q in queries:
    result.append(binary_search(numbers, 0, n-1, q))

  print(*result, sep=" ")
