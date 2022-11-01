#문자열s를 입력받은 후 r번 반복해 새문자열 p 

s= int(input())
for i in range(s):
    count, word = input().split()
    for x in word:
        print(x*int(count), end = "")
    print()
    
    