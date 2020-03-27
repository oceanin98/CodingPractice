#Easy
#Compute number of distinct values in an array.

def solution(A):
    
    if len(A) == 0:
        return 0
    
    A.sort()
    
    current = A[0]
    unique = 1
    
    for i in A:
        if i > current:
            unique += 1
            current = i
            
    return unique
