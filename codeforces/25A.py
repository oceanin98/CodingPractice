# http://codeforces.com/problemset/problem/25/A
# 1300

n = int(input())

numbers = [int(t) for t in input().split()]
assa = 0
result = 0
for num in numbers[:3]:
    if num % 2:
        result += 1

if result < 2:
    for i, num in enumerate(numbers):
        if num % 2:
            assa = i + 1
            break
else:
    for i,num in enumerate(numbers):
        if num % 2 == 0:
            assa = i + 1
            break

print(assa)
    
