import heapq

def read_ints():
  temp = input().split()
  temp = [int(t) for t in temp]
  return temp

def max_revenue(bids, last_deadline):
  current_bids = []

  max_revenue = 0

  while last_deadline:
    if last_deadline in bids:
      for p in bids[last_deadline]:
        heapq.heappush(current_bids, -p)    
    
    try:
      price = heapq.heappop(current_bids)
    except:
      price = 0
    max_revenue += (-price)
    last_deadline -= 1
  
  return max_revenue


tests = int(input())

for _ in range(tests):
  B = int(input())

  bids = {}
  last_deadline = 0
  for _ in range(B):
    price, d = read_ints()
    last_deadline = max(d, last_deadline)

    if d not in bids:
      bids[d] = []

    bids[d].append(price)

  result = max_revenue(bids, last_deadline)
  print(result)
