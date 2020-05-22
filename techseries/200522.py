# You are given two linked-lists representing two non-negative integers.
# The digits are stored in reverse order and each of their nodes contain a single digit. 
# Add the two numbers and return it as a linked list.

# Definition for singly-linked list.
class ListNode(object):
  def __init__(self, x):
    self.val = x
    self.next = None

class Solution:
  def addTwoNumbers(self, l1, l2, c = 0):
    if l1 and l2:
      addition = l1.val + l2.val + c
      if addition > 9:
        c = 1
        addition -= 10
    elif l1:
      addition = l1.val
    elif l2:
      addition = l2.val
    else:
      return None
    result = ListNode(addition)
    result.next = self.addTwoNumbers(l1.next, l2.next, c)
    return result
        

l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

result = Solution().addTwoNumbers(l1, l2)
while result:
  print result.val,
  result = result.next
# 7 0 8
