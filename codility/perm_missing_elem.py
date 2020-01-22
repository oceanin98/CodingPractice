# Difficulty: Easy
# Find the missing element in a given permutation.

"""
An array A consisting of N different integers is given. 
The array contains integers in the range [1..(N + 1)], 
which means that exactly one element is missing.

Your goal is to find that missing element.

Write an efficient algorithm for the following assumptions:

 - N is an integer within the range [0..100,000];
 - the elements of A are all distinct;
 - each element of array A is an integer within the range [1..(N + 1)].
"""

def solution(A):
    n = len(A) + 1
    total = n * (n + 1) // 2 # The total if all the elements were present
    
    for i in range(n - 1):
        total = total - A[i]
        
    return total
