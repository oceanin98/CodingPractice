# Staircase problem, up to 2 steps at a time
# I know it can be solved using fibonacci at O(log n), but I got lazy so..

def staircase(n):
  dp = [0,0,1]
  for i in range(n):
    dp[0], dp[1] = dp[1], dp[2]
    dp[2] = dp[0] + dp[1]
  return dp[-1]

print staircase(4)
# 5
print staircase(5)
# 8
