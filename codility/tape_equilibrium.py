#Difficulty: Easy
# Minimize the value |(A[0] + ... + A[P-1]) - (A[P] + ... + A[N-1])|.

"""
A non-empty array A consisting of N integers is given. 
Array A represents numbers on a tape.

Any integer P, such that 0 < P < N, splits this tape into two non-empty parts: 
A[0], A[1], ..., A[P − 1] and A[P], A[P + 1], ..., A[N − 1].

The difference between the two parts is the value of: 
|(A[0] + A[1] + ... + A[P − 1]) − (A[P] + A[P + 1] + ... + A[N − 1])|

In other words, it is the absolute difference between the sum of the first part and the sum of the second part.

Write a function:

def solution(A)

that, given a non-empty array A of N integers, returns the minimal difference that can be achieved.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [2..100,000];
each element of array A is an integer within the range [−1,000..1,000].
"""

def solution(A):
    lsum = 0
    rsum = sum(A)
    diff = -1 # sum(A)로 두면 [-2000,2000]같을 때 오류
    
    for i in range(len(A) - 1): # 그냥 range(len(A))이면 마찬가지로 [-2000,2000]같을 때 오류
        lsum += A[i]
        rsum -= A[i]
        if diff < 0:
            diff = abs(rsum - lsum)
        else:
            diff = min(abs(rsum - lsum), diff)
            
    return diff
