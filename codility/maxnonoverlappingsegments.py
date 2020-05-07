#Easy
#Find a maximal set of non-overlapping segments.

def solution(A, B):
    if len(A) == 0:
        return 0
        
    result = 1
    end = B[0]
    
    for i in range(1, len(A)):
        if A[i] > end:
            end = B[i]
            result += 1
    
    return result
