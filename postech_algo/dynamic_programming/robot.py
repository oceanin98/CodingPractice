def read_ints():
  temp = input().split()
  temp = [int(t) for t in temp]
  return temp

def maximum_points(grid, N, M):
  scores = [0] * M
  scores_1 = [0] * M
  scores_2 = [0] * M

  scores[0] = grid[0][0]

  for i in range(1,M):
    scores[i] = scores[i-1] + grid[0][i]

  for r in range(1, N):
    for c in range(M):
      if c == 0:
        scores_1[c] = scores[c] + grid[r][c]
      else:
        scores_1[c] = max(scores[c], scores_1[c - 1]) + grid[r][c]

    for c in range(M):
      col = M - c - 1
      if col == M - 1:
        scores_2[col] = scores[col] + grid[r][col]
      else:
        scores_2[col] = max(scores[col], scores_2[col + 1]) + grid[r][col]

    for c in range(M):
      scores[c] = max(scores_1[c], scores_2[c])
  return scores[M-1]

tests = int(input())

for _ in range(tests):
  N,M = read_ints()

  grid = []
  for _ in range(N):
    row = read_ints()
    grid.append(row)
  result = maximum_points(grid, N, M)
  print(result)
