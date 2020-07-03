# http://codeforces.com/problemset/problem/466/A
# 1200

n,m,a,b = [int(t) for t in input().split()]

result = 0

if b / m > a:
    result = a * n
else:
    result = n//m * b + min((n % m) * a, b)

print(result)
