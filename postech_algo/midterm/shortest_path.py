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

def dijkstra(graph, N):  
  visited = [0] * N
  distances = [sys.maxsize] * N
  parents = [-1] * N
  distances[0] = 0

  heap = []
  entry_finder = {}
  counter = itertools.count()
  
  add_task(entry_finder, counter, heap, 0, 0)

  while heap:
    try:
      temp = pop_task(heap, entry_finder)
      if visited[temp]:
        continue
      visited[temp] = 1
    except:
      break
    
    if temp not in graph:
      continue
    for n in graph[temp]:
      distance = distances[temp] + graph[temp][n]
      if distances[n] > distance:
        distances[n] = distance
        add_task(entry_finder, counter, heap, n, distance)
        parents[n] = temp

  return distances, parents

def print_path(parents, cur):
  if cur == 0:
    print(0,end="")
  else:
    print_path(parents, parents[cur])
    print(" ",cur, end="", sep="")
  

tests = int(input())

for _ in range(tests):
  N,M = read_ints()

  graph = {}
  for _ in range(M):
    u,v,c = read_ints()
    
    if u not in graph:
      graph[u] = {}
    
    graph[u][v] = c
  
  distances, parents = dijkstra(graph, N)

  if distances[-1] == sys.maxsize:
    print("NO")
  else:
    print_path(parents, N-1)
    print()
