def read_ints():
  temp = input().split()
  temp = [int(t) for t in temp]
  return temp

def convolution(feature, N, M, d):
  for r in range(N):
    for c in range(1,M):
      feature[r][c] += feature[r][c - 1]
  
  for c in range(M):
    for r in range(1,N):
      feature[r][c] += feature[r -1][c]
  #print(feature)
  result = []
  for r in range(N - d + 1):
    row = []
    for c in range(M - d + 1):
      a = feature[r + d - 1][c + d - 1]
      u = feature[r - 1][c + d - 1] if r > 0 else 0
      l = feature[r + d - 1][c - 1] if c > 0 else 0
      b = feature[r - 1][c - 1] if r > 0 and c > 0 else 0 
      row.append(a + b - u - l)
    result.append(row)  
  #print(result)
  return result


tests = int(input())

for _ in range(tests):
  N,M,d = read_ints()

  feature = []
  for _ in range(N):
    row = read_ints()
    feature.append(row)
  result = convolution(feature, N, M, d)
  
  for row in result:
    print(*row)
