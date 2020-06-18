# Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.
# In-place with minimum number of operations

class Solution:
  def moveZeros(self, nums):
    i = 0
    top = len(nums)
    zeros = 0
    while i < len(nums):
      if nums[i] == 0:
        zeros += 1
      else:
        nums[i - zeros] = nums[i]
        nums[i] = 0
      i += 1
      
nums = [0, 0, 0, 2, 0, 1, 3, 4, 0, 0]
Solution().moveZeros(nums)
print(nums)
# [2, 1, 3, 4, 0, 0, 0, 0, 0, 0]
