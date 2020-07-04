# http://codeforces.com/problemset/problem/189/A
# 1300
# Brute force over all possibilities...lol
# Fails in python, accepted in Pypy.

n, a, b, c = [int(t) for t in input().split()]

lengths = set((a,b,c))
lengths = [length for length in lengths if length <= n]
lengths.sort(reverse=True)
result = 0
if len(lengths) == 1:
    result = n // lengths[0]
elif len(lengths) == 2:
    for i in range(n // lengths[0] + 1):
        if (n - i * lengths[0]) % lengths[1] == 0:
            result = max(result, i + (n - i * lengths[0]) // lengths[1])
else: # 3 all left
    for i in range(n // lengths[0] + 1):
        for j in range((n - i * lengths[0]) // lengths[1] + 1):
            if (n - i * lengths[0] - j * lengths[1]) % lengths[2] == 0:
                result = max(result, i + j + (n - i * lengths[0] - j * lengths[1]) // lengths[2])

print(result)
