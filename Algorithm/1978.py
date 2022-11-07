#소수찾기
#주어진 n개중 소수가 몇개인지 찾아서 출력
n= int(input())
m= map(int,input().split())
sosu=0

for num in m:
    error=0
    if num>1:
        for i in range(2,num):
            if num % i == 0:
                error += 1
        if error == 0:
            sosu += 1
print(sosu)

