 #ox문제
 #o일경우 계속 숫자를 더한다
 #x이면 리셋되고 0으로 나온다
 
n= int(input())

for i in range(n):
    ox_list= list(input())
    score= 0
    sum_score=0
    for ox in ox_list:
        if ox =='O':
            score +=1
            sum_score += score
        else:
            score = 0
    print(sum_score)
    