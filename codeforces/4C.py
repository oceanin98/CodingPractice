# http://codeforces.com/problemset/problem/4/C
# 1300

n = int(input())

namedict = {}
for _ in range(n):
    name = input()
    if name not in namedict:
        namedict[name] = 0
        print("OK")
    else:
        namedict[name] += 1
        print(name + str(namedict[name]))
