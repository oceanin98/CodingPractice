#Medium
#Find the minimal average of any slice containing at least two elements.

def solution(A):
    
    if len(A) == 2:
        return 0

    minimum = 10000
    current = 0
    
    for i in range(len(A) - 1):
        if (A[i] + A[i + 1])/2 < minimum:
            current = i
            minimum = (A[i] + A[i + 1])/2
            
        if i + 2 < len(A):
            if (A[i] + A[i + 1] + A[i + 2] )/3 < minimum:
                current = i
                minimum = (A[i] + A[i + 1] + A[i + 2] )/3

            
    return current
