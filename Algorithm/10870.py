#피보나치수


# def fibonacci(n):
#     if n<= 1:
#         return n
#     return fibonacci(n-1) + fibonacci(n-2)

# n= int(input())
# print(fibonacci(n))


n= int(input())

fibonacci = [0,1]
for i in range(2, n+1):
    num = fibonacci[i-1]+fibonacci[i-2]
    fibonacci.append(num)

print(fibonacci[n])
