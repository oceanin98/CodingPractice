# Given a string, find the length of the longest substring without repeating characters.

class Solution:
  def lengthOfLongestSubstring(self, s):
    positions = {}
    st = 0
    maxlen = 0
    for i in range(len(s)):
      if s[i] not in positions:
        positions[s[i]] = i

      elif positions[s[i]] >= st:
        maxlen = max(maxlen, i - st)
        st = i+1
        
    return(maxlen)
print(Solution().lengthOfLongestSubstring('abrkaabcdefghijjxxx'))
# 10
