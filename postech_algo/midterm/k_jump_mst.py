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
      return task, priority
  raise KeyError('pop from an empty priority queue')

def MST(graph, N):
  weight_sum = 0

  included = [0] *  N
  distances = [sys.maxsize] * N
  total_included = 0

  heap = []
  entry_finder = {}
  counter = itertools.count()

  included[0] = 1
  total_included += 1
  for n in graph[0]:
    if included[n] == 0:
      add_task(entry_finder, counter, heap, n, graph[0][n])
      distances[n] = graph[0][n]

  while total_included < N:
    try:
      temp, weight = pop_task(heap, entry_finder)
      if included[temp]:
        continue
      included[temp] = 1
      total_included += 1
      weight_sum += weight
    except:
      return "NO"

    for n in graph[temp]:
      if included[n] == 0:
        priority = min(distances[n], graph[temp][n])
        add_task(entry_finder, counter, heap, n, priority)

  return weight_sum


def read_ints():
  temp = input().split()
  temp = [int(t) for t in temp]
  return temp

tests = int(input())

for _ in range(tests):
  N,M,K = read_ints() 
  
  max_c = 0
  min_c = sys.maxsize

  graph = {}
  for _ in range(M):
    u,v,c = read_ints()

    if min_c > c:
      min_c = c
    elif max_c < c:
      max_c = c

    if u not in graph:
      graph[u] = {}
    
    if v not in graph:
      graph[v] = {}

    graph[u][v] = c
    graph[v][u] = c

  if M < N - 1:
    print("NO")
    continue

  if (max_c - min_c) / K  + 1 < N - 1:
    print("NO")
    continue
  result = MST(graph, N)
  print(result)
