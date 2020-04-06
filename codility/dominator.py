# Easy
# Find an index of an array such that its value occurs at more than half of indices in the array.

def solution(A):
    size = 0
    value = 0
    
    for n in A:
        if size == 0:
            size += 1
            value = n
        else:
            if n == value:
                size +=1
            else:
                size -=1
        
    if size < 1:
        return -1
    
    sum = 0
    size = len(A)
    for n in range(size):
        if A[n] == value:
            sum += 1
            if sum > size / 2:
                return n
    
    return -1
