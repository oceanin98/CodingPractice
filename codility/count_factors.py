# Easy
# Count factors of given number n.

def solution(N):
    factors = 0
    
    i = 1
    while i * i < N:
        if N % i == 0:
            factors += 2
        
        i += 1
    if i * i == N:
        factors += 1
        
    return factors
