#숫자의 합
#n개의 숫자가 공백 없이 쓰여있다.  이 숫자를 모두 합해서 출력하는 프로그램을 작성하시오.

 #숫자 하나를 입력받고
 #입력받은 수많큼 숫자를 입력받고
 #입력받은 숫자를 모두 더해서 출력
 
n= int(input())
num=input()
sum=0

for i in range(n):
    sum+=int(num[i])
print(sum)