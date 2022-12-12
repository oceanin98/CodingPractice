#black jack

from itertools import combinations
n,m= map(int,input().split())
num= list(map(int,input().split()))
result=0

for cards in combinations(num,3):
    temp=sum(cards)
    if result<temp<=m:
        result=temp
print(result)
