#수정렬2
#공백 줄이기

n= int(input())
num=[]

for i in range(n):
    num.append(int(input()))
print(num)

num1= sorted(num)
print(num1)

for i in range(num1):
    print([i])