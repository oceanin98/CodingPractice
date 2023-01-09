#소인수분해
#정수 n이 주어졌을때, 소인수분해하는 프로그램을 작성하시오.

n=int(input())

if n==1 :
    print('')
    
for i in range(2, n+1):
    while n%i==0:
        print(i)
        n=n/i
