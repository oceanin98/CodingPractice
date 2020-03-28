#Easy
#Determine whether a triangle can be built from a given set of edges.

def solution(A):
    
    A.sort(reverse=True)
    
    for i in range(len(A)):
        if A[i] < 0:
            A = A[:i]
            break
        
    if len(A) < 3:
        return 0
    
    for i in range(len(A) - 2):
        if A[i] < A[i+1] + A[i+2]:
            return 1
        
    return 0
