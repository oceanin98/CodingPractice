# Easy (but wasn't SO easy for me)
# Find the index S such that the leaders of the sequences A[0], A[1], ..., A[S] and A[S + 1], A[S + 2], ..., A[N - 1] are the same.
# Actually, find the NUMBER of such indexes.

def find_leader(L):
    size = 0
    candidate = 0
    
    for l in L:
        if size == 0:
            candidate = l
            size += 1
        else:
            if l == candidate:
                size += 1
            else:
                size -= 1

    if size < 1:
        return -1
        
    count = 0
    for i in range(len(L)):
        if L[i] == candidate:
            count += 1
            if count > (len(L) // 2):
                return i
    return -1
    
def leader_indexes(L, leader):
    indexes = []
    
    for i in range(len(L)):
        if L[i] == leader:
            indexes.append(i)
            
    return indexes

def solution(A):
    size = len(A)
    
    index = find_leader(A)
    if index == -1:
        return 0
    leader = A[index]
    
    indexes = leader_indexes(A, leader)
    
    total = len(indexes)
    left = 0
    right = total
    
    equileader = 0
    for i in range(len(A) - 1):
        if A[i] == leader:
            left += 1
            right -= 1
            
        if (left > (i + 1) // 2) and (right > (size - i - 1) // 2):
            equileader += 1
                
    return equileader
