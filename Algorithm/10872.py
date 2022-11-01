#n! 구하는 공식 
#재귀를 사용해서 

# def factorial(n):
#     result=1
#     if n>0:
#         result= n*factorial(n-1)
#     return result
    
# n= int(input())
# print(factorial(n))


def factorial(n):
    result=1
    if n>0:
        result= n*factorial(n-1)
    return result
        
n= int(input())
print(factorial(n))