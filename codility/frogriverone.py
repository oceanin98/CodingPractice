#Frog River One
# Find the Earliest time when a frog can jump to the other side of a river
# Easy

'''
You are given an array A consisting of N integers representing the falling leaves.
A[K] represents the position where one leaf falls at time K, measured in seconds.

The goal is to find the earliest time when the frog can jump to the other side of the river. 
The frog can cross only when leaves appear at every position across the river from 1 to X 
(that is, we want to find the earliest moment when all the positions from 1 to X are covered by leaves).

Write an efficient algorithm for the following assumptions:

N and X are integers within the range [1..100,000];
each element of array A is an integer within the range [1..X].
'''

def solution(X, A):
    times = [-1] * X
    
    for i in range(len(A)):
        if times[A[i] - 1] == -1:
            times[A[i] - 1] = i
            X = X - 1
        else:
            continue
        
        if X == 0:
            return i
    
    return -1
