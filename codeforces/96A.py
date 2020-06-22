def read_ints():
  temp = input()
  ints = [int(t) for t in temp.split(" ")]
  return ints

players = input()
players = [int(p) for p in players]

cur = players[0]
count = 1

result = "NO"
for player in players[1:]:
  if player == cur:
    count += 1
  else:
    cur = player
    count = 1
  
  if count > 6:
    result = "YES"
    break

print(result)
  
