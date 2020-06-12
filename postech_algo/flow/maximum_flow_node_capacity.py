from collections import deque

def read_ints():
  temp = input().split()
  temp = [int(t) for t in temp]
  return temp

def get_flow(graph, levels, u, flow):
  if u == len(levels) - 1:
    return flow
  for neighbour in graph[u]:
    if levels[neighbour] == levels[u] + 1:
      if graph[u][neighbour][0] - graph[u][neighbour][1] > 0:
        current = min(flow, graph[u][neighbour][0] - graph[u][neighbour][1])
        resultant_flow = get_flow(graph, levels, neighbour, current)

        if resultant_flow:
          graph[u][neighbour][1] += resultant_flow
          graph[neighbour][u][1] -= resultant_flow

          return resultant_flow

  return 0

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
        if not levels[neighbour]:
          if graph[temp][neighbour][0] > graph[temp][neighbour][1]:
            levels[neighbour] = levels[temp] + 1
            queue.append(neighbour)
    if not levels[-1]: #target not reachable
      break
    flow += get_flow(graph, levels, 0, 10000)
  return flow

tests = int(input())

for _ in range(tests):
  n,m = read_ints() 
  nodes = read_ints()
  graph = {}

  for i in range(n):
    graph[i] = {}
    graph[i][i + n] = [nodes[i],0] #C, flow
    graph[i + n] = {}
    graph[i + n][i] = [0,0]

  for _ in range(m):
    u, v, c = read_ints()

    graph[u + n][v] = [c,0]
    graph[v][u+n] = [0,0]

  result = maximum_flow(graph, n)
  print(result)
