# https://codeforces.com/problemset/problem/1/A

def read_ints():
    temp = input().split()
    ints = [int(t) for t in temp]
    return ints

n,m,a = read_ints()

side1 = (n + a - 1) // a
side2 = (m + a - 1) // a

print(side1 * side2)
