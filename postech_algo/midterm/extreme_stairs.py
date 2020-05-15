def mat_square(mat, m):
  a = (mat[0][0]*mat[0][0] + mat[0][1]*mat[1][0] + mat[0][2]*mat[2][0]) % m
  b = (mat[0][0]*mat[0][1] + mat[0][1]*mat[1][1] + mat[0][2]*mat[2][1]) % m
  c = (mat[0][0]*mat[0][2] + mat[0][1]*mat[1][2] + mat[0][2]*mat[2][2]) % m

  d = (mat[1][0]*mat[0][0] + mat[1][1]*mat[1][0] + mat[1][2]*mat[2][0]) % m
  e = (mat[1][0]*mat[0][1] + mat[1][1]*mat[1][1] + mat[1][2]*mat[2][1]) % m
  f = (mat[1][0]*mat[0][2] + mat[1][1]*mat[1][2] + mat[1][2]*mat[2][2]) % m

  g = (mat[2][0]*mat[0][0] + mat[2][1]*mat[1][0] + mat[2][2]*mat[2][0]) % m
  h = (mat[2][0]*mat[0][1] + mat[2][1]*mat[1][1] + mat[2][2]*mat[2][1]) % m
  i = (mat[2][0]*mat[0][2] + mat[2][1]*mat[1][2] + mat[2][2]*mat[2][2]) % m

  return [[a,b,c],[d,e,f],[g,h,i]]

def nth_fibonacci(n,m):
  if n == 0:
    return [[1,0,0],[0,0,0],[0,0,0]]
  elif n == 1:
    return [[1,1,1],[1,0,0],[0,1,0]]
  else:
    result = mat_square(nth_fibonacci(n//2, m), m)

    if n % 2 == 1:
      a = (result[0][0] + result[0][1]) % m
      b = (result[0][0] + result[0][2]) % m
      c = result[0][0]
      
      d = (result[1][0] + result[1][1]) % m
      e = (result[1][0] + result[1][2]) % m
      f = result[1][0]

      g = (result[2][0] + result[2][1]) % m
      h = (result[2][0] + result[2][2]) % m
      i = result[2][0]

      result = [[a,b,c],[d,e,f],[g,h,i]]

    return result

def read_ints():
  temp = input().split()
  temp = [int(t) for t in temp]
  return temp

tests = int(input())

for _ in range(tests):
  n, m = read_ints()

  print(nth_fibonacci(n,m)[0][0])
