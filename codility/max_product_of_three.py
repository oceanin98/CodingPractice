#Easy
#Maximize A[P] * A[Q] * A[R] for any triplet (P, Q, R).

def solution(A):

    A.sort()
    
    last_three = A[-1] * A[-2] * A[-3]

    if last_three > 0:
        if A[-2] > 0: #(ends with PPP)
            return max(last_three, A[0] * A[1] * A[-1])
        else: #(ends with NNP)
            return A[-1] * A[0] * A[1]
    else:
        if A[-1] > 0: #(ends with NPP)
            return A[-1] * A[0] * A[1]
        else: #(ends with NNN)
            return last_three
