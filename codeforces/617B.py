# https://codeforces.com/problemset/problem/617/B
# 1300

n = int(input())
pieces = [int(t) for t in input().split()]

nutcount = 0
curways = 1
ways = []
for i, piece in enumerate(pieces):
    if piece: # nut
        ways.append(curways)
        curways = 1
        nutcount += 1
    else:
        if nutcount:
            curways += 1

result = 1
for w in ways:
    result *= w
if not ways:
    result = 0
print(result)
