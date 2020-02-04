# check whether array A is a permutation
# Easy

'''
A non-empty array A consisting of N integers is given.

A permutation is a sequence containing each element from 1 to N once, and only once.

Write a function:

def solution(A)

that, given an array A, returns 1 if array A is a permutation and 0 if it is not.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..100,000];
each element of array A is an integer within the range [1..1,000,000,000].
```

# Using a list (l = [-1] * max(A)) failed due to overflow when an element/range is too large.

def solution(A):
    A.sort()

    for i in range(len(A)):
        if A[i] != i + 1:
            return 0
            
    return 1
