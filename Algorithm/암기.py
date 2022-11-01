c= int(input())

for i in range(c):
    n= list(map(int, input().split()))
    c=0
    for j in n[1:]:
        avg= sum(n[1:])/n[0]
        if j>avg: