# Given a murder scene happened at the far right side
# Return the number of witnesses
# Must be taller than everyone in front of them

def witnesses(heights):
  curmax = -1
  result = 0
  for h in heights[::-1]:
    if h > curmax:
      result += 1
      curmax = h

  return result
print witnesses([3, 6, 3, 4, 1])
# 3
