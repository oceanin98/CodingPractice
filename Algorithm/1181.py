#단어정렬
#1.길이가 짧은 것부터 2. 길이가 같으면 사전 순으로 
#글자의 길이는 어떻게 알겠는게 알파벳순 정렬은 뭐임?

import sys

n= int(input())
list =[]

for i in range(n):
    list.append(str(sys.stdin.readline.rstrip()))
    
list=list(set(list))
list.sort()
list.sort(key=len)
for i in list:
    print(i)