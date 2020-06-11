from collections import deque

def read_ints():
  temp = input().split()
  temp = [int(t) for t in temp]
  return temp

def augment_path(graph, levels):
  flow = 0
  
  return flow

def maximum_flow(graph, n):
  flow = 0
  while True:
    # Determine the levels of nodes within the graph
    levels = [0] * (n * 2)
    levels[0] = 1
    queue = deque()
    queue.append(0)

    while queue:
      temp = queue.popleft()
      for neighbour in graph[temp]:
        if (not levels[neighbour]) and (graph[temp][neighbour][0] > graph[temp][neighbour][1]):
          levels[neighbour] = levels[temp] + 1
          queue.append(neighbour)
    if not levels[-1]:
      break
    flow += augment_path(graph, levels)
  return flow
tests = int(input())

for _ in range(tests):
  n,m = read_ints() 
  nodes = read_ints()
  graph = {}

  for i in range(len(nodes)):
    graph[i] = {}
    graph[i][i + n] = [nodes[i],0]

  for _ in range(m):
    u, v, c = read_ints()

    if u + n not in graph:
      graph[u + n] = {}
    if v not in graph:
      graph[v] = {}
    graph[u + n][v] = [c,0]
    graph[v][u+n] = [0,0]

  result = maximum_flow(graph, n)
  print(result)
