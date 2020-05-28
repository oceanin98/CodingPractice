def sortNums(nums):
  l = i = 0
  r = len(nums) - 1
  
  while i < r:
    if nums[i] == 2:
     i += 1 
    elif nums[i] < 2:
      nums[l], nums[i] = nums[i], nums[l]
      l += 1
      i += 1
    else:
      nums[r], nums[i] = nums[i], nums[r]
      r -= 1
  return nums

print(sortNums([3, 3, 2, 1, 3, 2, 1]))
print(sortNums([1,3,2,2,1,3,2,1,2,3,2,1,3,2,1,3,2,1,2,3,2,1,2,3,2,1,2,2,2,2,3,2,1,1,1,1,1,3,2,1,3,2,3,3]))
# [1, 1, 2, 2, 3, 3, 3]
