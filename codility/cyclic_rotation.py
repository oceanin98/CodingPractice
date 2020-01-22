# Difficulty: Painless
# Rotate an array to the right by a given number of steps.

"""
An array A consisting of N integers is given. 
Rotation of the array means that each element is shifted right by one index, 
and the last element of the array is moved to the first place.

The goal is to rotate array A K times; 
that is, each element of A will be shifted to the right K times.

Assume that:

N and K are integers within the range [0..100];
each element of array A is an integer within the range [−1,000..1,000].
"""

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A, K):
    if len(A) < 2:
        return A
        
    K = K % len(A) # in case K > len(A)
    return A[len(A) - K:] + A[:len(A) - K]
