# 100,20,10,5,1

cash = int(input())
units = [100,20,10,5,1]
bills = 0

for unit in units:
  if cash < 5:
    bills += cash
    break
  if cash < unit:
    continue
  bills += cash // unit  
  cash %= unit
  
print(bills)
