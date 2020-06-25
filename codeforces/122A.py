# https://codeforces.com/problemset/problem/122/A

def read_ints():
    temp = input().split()
    ints = [int(t) for t in temp]
    return ints

divisors = [4,7, 44, 47, 74, 77, 444,447,474,477,744,747,774,777]

n = int(input())


result = "NO"
for d in divisors:
    if n < d:
        break
    if n % d == 0:
        result="YES"
        break

print(result)
