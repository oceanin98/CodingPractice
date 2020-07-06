# https://codeforces.com/problemset/problem/451/B
# Took much longer than it should have
# 1300

n = int(input())
integers = [int(t) for t in input().split()]

start = -1
end = -1
largerthan = 0

result = "yes"
for i, integer in enumerate(integers):
    if i == 0:
        continue
    if start == -1: # first part of array
        if integers[i - 1] < integer:
            continue
        else:
            if i - 2 >= 0:
                largerthan = integers[i - 2]
            start = i - 1
    elif end == -1: # second part of array
        if integers[i - 1] > integer:
            continue#
        else:
            if integer < integers[start]:
                result = "no"
                break
            if integers[i - 1] < largerthan:
                result = "no"
                break
            end = i - 1
    else: #last part of array
        if integers[i - 1] > integer:
            result = "no"
            break

if start == -1:
    start = end = 0
elif end == -1:
    if integers[-1] < largerthan:
        result = "no"
    else:
        end = n - 1

print(result)
if result == "yes":
    print(start + 1, end + 1)
