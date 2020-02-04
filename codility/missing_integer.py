# Find the smallest positive integer that does not occur in a given sequence
# Medium

'''
Write a function:

def solution(A)

that, given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..100,000];
each element of array A is an integer within the range [−1,000,000..1,000,000].
'''

def solution(A):
    A = list(set(A))
    A = [i for i in A if i > 0]
    A.sort()
    
    for i in range(len(A)):
        
        if A[i] != i + 1:
            return i + 1
            
        
    return len(A) + 1
