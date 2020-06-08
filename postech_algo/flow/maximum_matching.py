def read_ints():
  temp = input().split()
  temp = [int(t) for t in temp]
  return temp

def check_match(graph, u, visited, pred):
  for v in graph[u]:
    if visited[v] == 0:
      visited[v] = 1
      
      if pred[v] == -1:
        pred[v] = u
        return 1
      elif check_match(graph, pred[v], visited, pred) == 1:
        pred[v] = u
        return 1
  return 0

def maximum_matching(graph, n, m):
  matches = 0
  pred = [-1] * m
  for i in graph:
    visited = [0] * m
    matches += check_match(graph, i, visited, pred)
  return matches

tests = int(input())

for _ in range(tests):
  n,m,l = read_ints() 

  graph = {}
  for _ in range(l):
    u, v= read_ints()

    if u not in graph:
      graph[u] = []
    graph[u].append(v)

  result = maximum_matching(graph, n, m)
  print(result)
