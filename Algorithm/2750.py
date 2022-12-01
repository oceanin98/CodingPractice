#수정렬하기
#n개의 수가 주어졌을떄, 이를 오름차순으로 정렬


n= int(input())
num=[]
for i in range(n):
    num.append(int(input()))
num1=sorted(num)
for i in range(len(num)):
    print(num1[i])
