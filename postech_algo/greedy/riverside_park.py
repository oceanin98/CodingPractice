def read_ints():
  temp = input().split()
  temp = [int(t) for t in temp]
  return temp

def largest_rectangle(hulls):

  stack = []
  size = 0

  maximum = hulls[0]
  curheight = hulls[0]

  stack.append((hulls[0], 0))
  size += 1

  for i in range(1, len(hulls)):
    if hulls[i] == curheight:
      continue
    elif hulls[i] > curheight:
      if len(stack) > size:
        stack[size] = (hulls[i], i)
      else:
        stack.append((hulls[i], i))
      size += 1
      curheight = hulls[i]
    else: # hulls[i] < curheight
      farleft = i
      while (size != 0) and (stack[size - 1][0] > hulls[i]):
        maximum = max(maximum, stack[size - 1][0] * (i - stack[size - 1][1]))
        farleft = stack[size - 1][1]
        size -= 1
      if size != 0 and stack[size - 1][0] == hulls[i]:
        continue
      else:
        if len(stack) > size:
          stack[size] = (hulls[i], farleft)
        else:
          stack.append((hulls[i], i))
        size += 1
      curheight = hulls[i]
  
  while size:
    size -= 1
    h, i = stack[size]
    maximum = max(maximum, h * (len(hulls) - i))
      
  return maximum

tests = int(input())

for _ in range(tests):
  n,w = read_ints()

  hulls = [0]*w

  for _ in range(n):
    l, r, y = read_ints()
    
    for i in range(l,r):
      hulls[i] = y

  result = largest_rectangle(hulls)
  print(result)
