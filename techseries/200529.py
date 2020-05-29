def two_sum(l, k):
  search = {}
  for v in l:
    if v in search:
      return "True"
    else:
      search[k-v] = 1

  return "False"


print two_sum([4,7,1,-3,2], 5)
# True
