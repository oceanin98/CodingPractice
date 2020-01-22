# Difficulty: Easy
# Find value that occurs in odd number of elements.

"""
A non-empty array A consisting of N integers is given. 
The array contains an odd number of elements, 
and each element of the array can be paired with another element that has the same value, 
except for one element that is left unpaired.

Write an efficient algorithm for the following assumptions:

 - N is an odd integer within the range [1..1,000,000];
 - each element of array A is an integer within the range [1..1,000,000,000];
 - all but one of the values in A occur an even number of times.
"""

def solution(A):
    result = 0
    
    for i in range(len(A)):
        result = result ^ A[i] # XOR characteristic
        
    return result
