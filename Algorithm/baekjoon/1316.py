#ccazzzzbb 는 c,a,z,b의 연속


n= int(input())
cnt=n
for _ in range(n):
    word = input()
    for idx in range(len(word)-1):
        #idx를 기준으로 앞뒤 단어가 다를 경우
        if word[idx] != word[idx+1]:
#idx 뒤쪽 인덱스의 문자열에서 word[idx+1]문자가 포함되어 있는지 확인
            if word[idx+1] in word[:idx]:
#포함되어 있다면 연속해서 알파벳이 나타난게 아니므로 cnt를 하나 감소 (그룹 단어아님)
                cnt -= 1
#그리구 break로 for문 탈출 (다음 단어로 넘어감)
                break
print(cnt)
                         
