# Medium
# Compute number of integers divisible by k in range [a..b].

def solution(A, B, K):
    
    total = 0
    
    if A % K == 0:
        pass
    else:
        A = A + (K - (A % K))
    total += 1
        
    total += (B - A) // K
    
    return total
