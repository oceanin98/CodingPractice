def hansu(num):
    hansu_cnt=0
    for i in range(1,num+1):
        num_list= list(map(int, str(i)))
        if i<100:
            hansu_cnt +=1
        elif num_list[0]-num_list[1]==num_list[1]-num_list[2]:
            hansu_cnt +=1
    return hansu_cnt

num= int(input())
print(hansu(num))

#과연 내가 다음에 이걸 안보고 풀수 있을까...
#한수를 구하는 방법:
#숫자를 1부터 n번까지 넣어주고 카운트 해줄건데 num_list 를 만들어줄건데 여기에 