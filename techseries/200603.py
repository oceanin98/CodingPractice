# Create a maxstack class, which supports the regular functions of a stack (push, pop)
# As well as an additional function max() which returns the maximum element in the stack (None if empty)
# Each method should run in constant time

class MaxStack:
  def __init__(self):
    self.size = 0
    self.stack = []
    self.maximum = 0
  def push(self, val):
    self.stack.append((val, self.maximum))
    self.maximum = max(self.maximum, val)

  def pop(self):
    temp = self.stack.pop()
    self.maximum = temp[1]

  def max(self):
    if self.stack:
      return self.maximum
    else:
      return None

s = MaxStack()
s.push(1)
s.push(2)
s.push(3)
s.push(2)
print s.max()
# 3
s.pop()
s.pop()
print s.max()
# 2
