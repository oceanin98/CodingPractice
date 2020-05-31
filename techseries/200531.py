# Check if there is a way to make list non-decreasing by changing AT MOST ONE element

def check(lst):
  chance = 1
  for i in range(1, len(lst)):
    if lst[i] < lst[i -1]:
      if chance:
        chance -= 1
      else:
        return "False"
  return True
    

print check([13, 4, 7])
# True
print check([5,1,3,2,5])
# False
