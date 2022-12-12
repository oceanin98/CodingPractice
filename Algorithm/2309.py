#일곱난쟁이
#난쟁이가 돌아왔는데 아홉명이다.
#난쟁이 키는 합 100
#1. 오름차순 정렬로 나타냄, 어떻게 찾냐 

import sys
from itertools import combinations
n=9
num= [ int(input()) for _ in range (n)]

for i in combinations(num,7):
    if sum(i) == 100:
        answer= list(i)
        
answer.sort()
print(*answer, sep='\n')