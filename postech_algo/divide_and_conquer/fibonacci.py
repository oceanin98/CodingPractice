tests = int(input())

def mat_square(mat):
  a = (mat[0][0]*mat[0][0] + mat[0][1]*mat[1][0]) % 2147483647
  b = (mat[0][0]*mat[0][1] + mat[0][1]*mat[1][1]) % 2147483647
  c = (mat[0][0]*mat[1][0] + mat[1][1]*mat[1][0]) % 2147483647
  d = (mat[0][1]*mat[1][0] + mat[1][1]*mat[1][1]) % 2147483647
  return [[a,b],[c,d]]

def nth_fibonacci(n):
  if n == 0:
    return [[0,0],[0,0]]
  elif n == 1:
    return [[0,1],[1,1]]
  else:
    result = mat_square(nth_fibonacci(n//2))

    if n % 2 == 1:
      a = result[0][1]
      b = (result[0][0] + result[0][1]) % 2147483647
      c = result[1][1]
      d = (result[1][0] + result[1][1]) % 2147483647

      result = [[a,b],[c,d]]

    return result

for _ in range(tests):
  n = int(input())
  print(nth_fibonacci(n)[0][1])
