def read_ints():
  temp = input()
  ints = [int(t) for t in temp.split(" ")]
  return ints

coins = input()
coins = read_ints()
total = sum(coins)
coins.sort(reverse=True)
mine = 0
sum_mine = 0

for coin in coins:
  if sum_mine > total:
    break
  else:
    mine += 1
    sum_mine += coin
    total -= coin

print(mine)
