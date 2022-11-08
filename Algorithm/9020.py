#고륻바흐의 추측
#2보다 큰 짝수 n이 주어졌을때 n의 골드바흐 파티션..?
#짝수는 두 소수의 합으로 이루어져 있다ㅣ

#에리스토테네스 체를 사용하여 구현 ?

def Goldbach():
    check = [False, False] + [True] * 10000
    
    for i in range(2, 101):
        if check[i] == True:
            for j in range(i + i, 10001, i):
                check[j] = False

    T = int(input())
    for _ in range(T):
        n = int(input())

        A = n // 2
        B = A
        for _ in range(10000):
            if check[A] and check[B]:
                print(A, B)
                break
            A -= 1
            B += 1

Goldbach()