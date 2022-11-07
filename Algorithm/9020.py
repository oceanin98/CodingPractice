#고륻바흐의 추측
#2보다 큰 짝수 n이 주어졌을때 n의 골드바흐 파티션..?
#짝수는 두 소수의 합으로 이루어져 있다ㅣ

#에리스토테네스 체를 사용하여 구현 ?

prime_list = [False, False] + [True]*10002 #??

for i in range(2, 10002):
    if prime_list[i]:
        for j in range(2*i, 10002, i):
            prime_list[j] = False

T = int(input())

for i in range(T):
    n = int(input())
    a = n//2
    b = a
    while a>0:
        if prime_list[a] and prime_list[b]:
            print(a, b)
            break
        else:
            a-=1
            b+=1