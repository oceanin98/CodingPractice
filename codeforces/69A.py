# https://codeforces.com/problemset/problem/69/A

def read_ints():
    temp = input().split()
    ints = [int(t) for t in temp]
    return ints

n = int(input())

forces = []
for _ in range(n):
    forces.append(read_ints())

result = "YES"
for direction in zip(*forces):
    if sum(direction) != 0:
        result = "NO"
        break

print(result)
