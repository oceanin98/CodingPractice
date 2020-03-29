#Easy
#N voracious fish are moving along a river. Calculate how many fish are alive.

def solution(A, B):
    N = len(A)
    
    stack = [0] * N
    size = 0
    remaining = 0
    
    for i in range(N):
        if size == 0:
            if B[i] == 0:
                remaining += 1
            else:
                stack[size] = (A[i], B[i]) #first 1
                size += 1
        else:
            if B[i] == 1:
                stack[size] = (A[i], B[i]) #other 1s
                size += 1
            else: #a 0 after 1s
                while A[i] > stack[size-1][0]:
                    size -= 1
                    if size == 0:
                        remaining += 1
                        break
                    
    return remaining + size
