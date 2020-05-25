# Given a string, s, find the longest palindromic substring in s.

class Solution: 
    def longestPalindrome(self, s):
      maxlength = 1
      start = 0
      for i in range(1,len(s)):
        # No longer palindrome can be found now
        if len(s) - i < maxlength//2:
          break
        # odd length
        curlen = 1
        left = right = 1
        while i - left >= 0 and i + right < len(s):
          if s[i - left] == s[i + right]:
            left += 1
            right += 1
            curlen += 2
          else:
            break
        if curlen > maxlength:
          maxlength = curlen
          start = i - left + 1
        # even length
        curlen = 2
        left = right = 1
        if s[i] != s[i - 1]:
          continue
        while i - left - 1 > 0 and i + right < len(s):
          if s[i - left - 1] == s[i + right]:
            left += 1
            right += 1
            curlen += 2
          else:
            break
        if curlen > maxlength:
          maxlength = curlen
          start = i - left
      return s[start:start+maxlength]
       
        
# Test program
ss = ["tracecars", "banana", "million", "aaaaaaaaaaaaaaa"]
for s in ss:
  print(str(Solution().longestPalindrome(s)))
  # racecar
