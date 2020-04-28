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

def get_neighbours(task, N, M):
  neighbours = []
  if task - M > 0:
    neighbours.append(task - M) # up
  
  if task + M < M*N:
    neighbours.append(task + M)
     # down
  
  if task // M == (task + 1) // M:
    neighbours.append(task + 1)

  if task // M == (task - 1) // M:
    neighbours.append(task - 1)

  return neighbours

def fastest_speed(raw_paths, N, M):
  result = -1
  
  visited = [0] * (N * M)
  speeds = [-1] * (N * M)
  speeds[0] = raw_paths[0]

  heap = []
  entry_finder = {}
  counter = itertools.count()
  
  add_task(entry_finder, counter, heap, 0, -sys.maxsize)

  while heap:
    try:
      temp = pop_task(heap, entry_finder)
      if visited[temp]:
        continue
      visited[temp] = 1
    except:
      break
   
    neighbours = get_neighbours(temp, N, M)
    
    for n in neighbours:
      speed = max(speeds[n], min(speeds[temp], raw_paths[n]))
      if speed > speeds[n]:
        speeds[n] = speed
        add_task(entry_finder, counter, heap, n, -speed)

  return speeds[-1]

tests = int(input())

for _ in range(tests):
  N,M = read_ints() 

  graph = {}
  raw_paths = []
  for _ in range(N):
    row = read_ints()
    raw_paths.append(row)
  
  raw_paths = [item for sublist in raw_paths for item in sublist]

  result = fastest_speed(raw_paths, N, M)
  print(result)
