# https://codeforces.com/problemset/problem/1324/B
# 1100

t = int(input())

for _ in range(t):
    _ = int(input())
    numbers = [int(t) for t in input().split()]

    positions = {}
    result = "NO"
    for i, num in enumerate(numbers):
        if numbers[i] not in positions:
            positions[numbers[i]] = i
        else:
            if abs(positions[numbers[i]] - i) > 1:
                result = "YES"
                break
    print(result)
