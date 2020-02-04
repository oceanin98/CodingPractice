# Count the number of passing cars on the road
# Easy

'''
A non-empty array A consisting of N integers is given. 
The consecutive elements of array A represent consecutive cars on a road.

Array A contains only 0s and/or 1s:

0 represents a car traveling east,
1 represents a car traveling west.

The goal is to count passing cars. 
We say that a pair of cars (P, Q), where 0 ≤ P < Q < N, is passing when P is traveling to the east and Q is traveling to the west.

Write a function:

def solution(A)

that, given a non-empty array A of N integers, returns the number of pairs of passing cars.

The function should return −1 if the number of pairs of passing cars exceeds 1,000,000,000.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..100,000];
each element of array A is an integer that can have one of the following values: 0, 1.
'''

def solution(A):
    east = 0
    passing = 0
    for i in range(len(A)):
        if A[i] == 1:
            passing += east
            if passing > 1000000000:
                return -1
        else:
            east += 1
            
    return passing
