# You are given an array. Each element represents the price of a stock on that particular day. 
# Calculate and return the maximum profit you can make from buying and selling that stock only once.


def buy_and_sell(arr):
  #Fill this in.
  min_ = arr[0]
  result = 0

  for val in arr[1:]:
    if val < min_:
      min_ = val
      continue
    result = max(result, val - min_)
  return result
  
print buy_and_sell([9, 11, 8, 5, 7, 10])
# 5
