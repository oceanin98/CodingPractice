# Find the only element in the list that does not have an equal entry 

def singleNumber(nums):
  xor = nums[0]
  for num in nums[1:]:
    xor ^= num

  return xor

print singleNumber([4, 3, 2, 4, 1, 3, 2])
# 1
