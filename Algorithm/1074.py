#z
#왼쪽 위, 오른쪽 위, 왼쪽 아래, 오르쪽 아래 
#n>1 인경우 , 배열의 크기를 2 *n-1 X 2 *n-1로 4등분 후 재귀적 방문
#모르겠다 답봐야지 
#입력받은 r과 c로 사분면을 찾기만 하면 되는 문제
# 예를 들어 좌표가 3사분면에 있다면 1,2 사분면은 거쳤으니 그 숫자만큼 더해준다 
n,r,c= map(int,input().split())
num=0
while n>0:
    temp=(2**n)//2
    if n>1:
        if temp >r and temp <= c:
            num += temp**2
            c-=temp
        elif temp <=r and temp >c:
            num += (temp **2)*2
            r -= temp
        elif temp <=r and temp <= c:
            num += (temp **2)*3
            r-= temp
            c -=temp
    elif n ==1:
        if r ==0 and c ==1:
            num +=1
        elif r==1 and c ==0:
            num+= 2
        elif r==1 and c==1:
            num += 3
    n-=1
print(num)





