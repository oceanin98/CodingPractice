import sys

def read_ints():
  temp = input().split()
  temp = [int(t) for t in temp]
  return temp

def shortest_k_path(graph, V, k):

  result = sys.maxsize
  distances = [sys.maxsize] * V
  distances[0] = 0

  if V-1 == 0: # if only 1 vertex
    result = 0

  while k:
    temp_dist = [sys.maxsize] * V
    for u in graph:
      for v in graph[u]:
        if distances[u] != sys.maxsize:
          temp_dist[v] = min(temp_dist[v], distances[u] + graph[u][v])
    distances = temp_dist
    result = min(result, distances[V-1])
    
    k -= 1
  
  if result == sys.maxsize:
    return 'NO'
  return result


tests = int(input())

for _ in range(tests):
  V,E,k = read_ints() 

  graph = {}
  for _ in range(E):
    u, v, w = read_ints()

    if u not in graph:
      graph[u] = {}
    
    if v in graph[u]:
      graph[u][v] = min(graph[u][v], w)
    else:
      graph[u][v] = w

  result = shortest_k_path(graph, V, k)
  print(result)
