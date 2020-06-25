# https://codeforces.com/problemset/problem/58/A

string = input()
target = "hello"
idx = 0

result = "NO"
for s in string:
    if s == target[idx]:
        idx += 1
        if idx == len(target):
            result="YES"
            break

print(result)
