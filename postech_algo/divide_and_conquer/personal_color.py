tests = int(input())

def check_achromatic(codes):
  flag = 0
  if codes[0][0] == codes[0][1] and codes[0][0] == codes[0][2]:
    flag += 1

  if codes[1][0] == codes[1][1] and codes[1][0] == codes[1][2]:
    flag += 2

  if codes[2][0] == codes[2][1] and codes[2][0] == codes[2][2]:
    flag += 4

  return flag

def code_to_int(code):
  result = []
  for c in code:
    if c in ['0','1','2','3','4','5','6','7','8','9']:
      result.append(int(c))
    else:
      if c == 'A':
        result.append(10)
      elif c == 'B':
        result.append(11)
      elif c == 'C':
        result.append(12)
      elif c == 'D':
        result.append(13)
      elif c == 'E':
        result.append(14)
      else:
        result.append(15)
  return result  

def int_to_code(number):
  a = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']

  return a[number]

def colours_to_code(colours, number):
  if number > 3:
    R = colours_to_code(colours[:number//3], number//3)
    G = colours_to_code(colours[number//3 : 2*number//3], number//3)
    B = colours_to_code(colours[2*number//3:], number//3)

    return colours_to_code([R,G,B], 3)

  elif number == 3:
    flag = check_achromatic(colours)
    R = G = B = 0
    # calculate R
    if flag % 2 == 1:
      R = colours[0][0]
    else:
      R = (colours[0][0] + colours[0][1] + colours[0][2]) % 16
    # calculate G
    if flag in [2,3,6]:
      G = colours[1][0]
    elif flag == 7:
      G = 15
    else:
      G = (colours[1][0] + colours[1][1] + colours[1][2]) % 16
    # calculate B
    if flag in [4,5,6,7]:
      B = colours[2][0]
    else:
      B = (colours[2][0] + colours[2][1] + colours[2][2]) % 16
    
    return [R,G,B]


for _ in range(tests):
  number = int(input())
  colours = input().split(" ")
  if number == 1:
    print(colours[0])
    continue
  colours = [code_to_int(code) for code in colours]

  result = colours_to_code(colours, number)
  result = ''.join([int_to_code(c) for c in result])

  print(result)
