import sys

def read_ints():
  temp = input().split()
  temp = [int(t) for t in temp]
  return temp

def topological_sort(visited, graph, v, stack, count):
  visited[v] = 1

  if v in graph:
    for k in graph[v]:
      if visited[k] == 0:
        topological_sort(visited, graph, k, stack, count)
    
  stack[count[0]] = v
  count[0] += 1

def longest_path(graph, n, sinks):
  result = 0

  for i in sinks:
    if i not in graph:
      continue
    stack = [-1] * n
    count = [0]
    visited = [0] * n

    topological_sort(visited, graph, i, stack, count)

    #for j in range(n):
    #  if visited[j] == 0:
    #    topological_sort(visited, graph, j, stack, count)
    
    count = count[0]
    distances = [-sys.maxsize] * n
    distances[i] = 0

    while count:
      count -= 1
      u = stack[count]
      if distances[u] != -sys.maxsize:
        if u in graph:
          for k in graph[u]:
            distances[k] = max(distances[k], distances[u] + graph[u][k])
            result = max(result, distances[k])
  return result

tests = int(input())

for _ in range(tests):
  n,m = read_ints() 

  sources = {}

  graph = {}
  for _ in range(m):
    u, v, w = read_ints()

    sources[u] = 1

    if v not in graph:
      graph[v] = {}
    
    if u in graph[v]:
      graph[v][u] = max(graph[v][u], w)
    else:
      graph[v][u] = w

  sinks = []
  for i in range(n):
    if i not in sources:
      sinks.append(i)
  result = longest_path(graph, n, sinks)
  print(result)
