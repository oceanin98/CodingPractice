'''
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:
- Open brackets are closed by the same type of brackets.
- Open brackets are closed in the correct order.
- Note that an empty string is also considered valid.
'''

class Solution:
  def isValid(self, s):
    stack = [0] * 10
    # Use try-catch and append do be made dynamic. Just used static for simplicity.
    size = 0

    for p in s:
      if p in ['{', '[', '(']:
        stack[size] = p
        size += 1
      else:
        if (p == '}' and stack[size - 1] == '{') or (p == ']' and stack[size - 1] == '[') or (p == ')' and stack[size - 1] == '('):
          size -= 1
        else:
          return "False"

    if size == 0:
      return "True"
    return "False"

# Test Program
s = "()(){(())" 
# should return False
print(Solution().isValid(s))

s = ""
# should return True
print(Solution().isValid(s))

s = "([{}])()"
# should return True
print(Solution().isValid(s))
