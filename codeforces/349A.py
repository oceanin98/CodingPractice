# https://codeforces.com/problemset/problem/349/A
# 1100

n =int(input())
bills = [int(t) for t in input().split()]

result = "YES"
changes = {25:0, 50:0, 100:0}
for bill in bills:
    changes[bill] += 1
    change = bill - 25
    # can either be 25 or 75
    if not change:
        continue
    elif change == 25:
        if changes[25]:
            changes[25] -= 1
            continue
        else:
            result = "NO"
            break
    elif change == 75:
        if changes[25] and changes[50]:
            changes[25] -= 1
            changes[50] -= 1
            continue
        elif changes[25] >= 3:
            changes[25] -= 3
            continue
        else:
            result = "NO"
            break
print(result)
