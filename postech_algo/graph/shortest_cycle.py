from collections import deque

def read_ints():
  temp = input().split()
  temp = [int(t) for t in temp]
  return temp

def shortest_path(graph, i, j, n):
  num = n
  distances = [10001] * num
  visited = [-1] * num

  distances[i] = 0
  visited[i] = 0

  queue = deque()
  queue.append(i)

  while queue:
    temp = queue.popleft() 
    
    for k in graph[temp]:
      if visited[k] == -1:
        visited[k] = 1
        distances[k] = distances[temp] + 1

        queue.append(k)

        if k == j:
          return distances[j]
  return distances[j]


def shortest_cycle(graph, vertices, n):
  result = 10001

  for v1, v2 in vertices:
    graph[v1].remove(v2)
    graph[v2].remove(v1)

    path_length = shortest_path(graph, v1, v2, n)
    result = min(path_length + 1, result)

    graph[v1].append(v2)
    graph[v2].append(v1)

  if result == 10001:
    result = -1
  return result

tests = int(input())

for _ in range(tests):
  n,m = read_ints() 

  graph = {}
  vertices = []
  for _ in range(m):
    v1, v2 = read_ints()
    vertices.append((v1,v2))
    if v1 not in graph:
      graph[v1] = []
    if v2 not in graph:
      graph[v2] = []

    graph[v1].append(v2)
    graph[v2].append(v1)

  result = shortest_cycle(graph, vertices, n)
  print(result)
