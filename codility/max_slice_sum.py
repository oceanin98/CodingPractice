# Easy
# Find a maximum sum of a compact subsequence of array elements.

def solution(A):
    maxend = maxslice = A[0]
    
    for i in A[1:]:
        maxend = max(maxend + i, i)
        maxslice = max(maxslice, maxend)

    return maxslice
