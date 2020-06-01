#Given binary tree and a value k,
# Return floor (value less than or equal to k) and ceiling(higher than or equal to k)
# Return None for either if nonexistent

class Node:
  def __init__(self, value):
    self.left = None
    self.right = None
    self.value = value

def findCeilingFloor(root_node, k, floor=None, ceil=None):
  if root_node is None:
    return(floor, ceil)
  if root_node.value == k:
    floor = ceil = k
  elif root_node.value < k:
    floor, ceil = findCeilingFloor(root_node.right, k, root_node.value, ceil)
  else:
    floor, ceil = findCeilingFloor(root_node.left, k, floor, root_node.value)

  return (floor, ceil)

root = Node(8) 
root.left = Node(4) 
root.right = Node(12) 
  
root.left.left = Node(2) 
root.left.right = Node(6) 
  
root.right.left = Node(10) 
root.right.right = Node(14) 

print findCeilingFloor(root, 5)
# (4, 6)
