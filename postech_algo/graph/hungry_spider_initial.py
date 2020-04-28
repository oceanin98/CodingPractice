import heapq
import itertools
import sys

REMOVED = '<removed-task>'

def add_task(entry_finder, counter, heap, task, priority=0):
  if task in entry_finder:
    remove_task(task, entry_finder)
  count = next(counter)
  entry = [priority, count, task]
  entry_finder[task] = entry
  heapq.heappush(heap, entry)

def remove_task(task, entry_finder):
  entry = entry_finder.pop(task)
  entry[-1] = REMOVED

def pop_task(heap, entry_finder):
  while heap:
    priority, count, task = heapq.heappop(heap)
    if task is not REMOVED:
      del entry_finder[task]
      return task
  raise KeyError('pop from an empty priority queue')

def read_ints():
  temp = input().split()
  temp = [int(t) for t in temp]
  return temp

def dijkstra(graph, N, s):  
  visited = [0] * (N * M)
  distances = [sys.maxsize] * (N * M)
  distances[s] = 0

  heap = []
  entry_finder = {}
  counter = itertools.count()
  
  add_task(entry_finder, counter, heap, s, 0)

  while heap:
    try:
      temp = pop_task(heap, entry_finder)
      if visited[temp]:
        continue
      visited[temp] = 1
    except:
      break
    
    for n in graph[temp]:
      distance = distances[temp] + graph[temp][n]
      if distances[n] > distance:
        distances[n] = distance
        add_task(entry_finder, counter, heap, n, distance)

  return distances

def noi(dist1, dist2):
  picked = set()

  dist3 = list(range(len(dist1)))
  distances = [(d1,d2,d3) for d1,d2,d3 in zip(dist1, dist2, dist3)] 
  distances.sort()

  #
  for i in range(len(distances)):
    d1, d2, d3 = distances[i]
    if i == 0:
      picked.add(d3)
    else:
      for j in range(i):
        t1, t2, _ = distances[j]
        if t2 < d2:
          break
        else:
          if j == i-1:
            picked.add(d3)

  distances = [(d2,d1,d3) for d1,d2,d3 in distances] 
  distances.sort()
  minimum = distances[1][0]

  #
  for i in range(len(distances)):
    d1, d2, d3 = distances[i]
    if i == 0:
      picked.add(d3)
    else:
      for j in range(i):
        t1, t2, _ = distances[j]
        if t2 < d2:
          break
        else:
          if j == i-1:
            picked.add(d3)
            
  return len(picked)

tests = int(input())

for _ in range(tests):
  N,M = read_ints()
  d1, d2 = read_ints()

  graph = {}
  for _ in range(4*N*M - 3*N - 3*M + 2):
    u,v,l = read_ints()
    
    if u not in graph:
      graph[u] = {}
    if v not in graph:
      graph[v] = {}
    
    graph[u][v] = l
    graph[v][u] = l
  
  distances_1 = dijkstra(graph, N, d1)
  distances_2 = dijkstra(graph, N, d2)

  result = noi(distances_1, distances_2)

  print(result)
