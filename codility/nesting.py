# easy
# Determine whether a given string of parentheses (single type) is properly nested.

def solution(S):
    if len(S) == 0:
        return 1
    
    size = 0
    
    for p in S:
        if p == "(":
            size += 1
        else:
            size -=1
            if size < 0:
                return 0
    
    if size > 0:
        return 0
    return 1
