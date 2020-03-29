#EASY
#Determine whether a given string of parentheses (multiple types) is properly nested.

def solution(S):
    stack = [0] * 200000
    size = 0
    
    for b in S:
        if b in  ['(', '[', '{']:
            stack[size] = b
            size += 1
        else:
            if size == 0:
                return 0
            
            last = stack[size-1]
            
            if (b == ')' and last == '(') or \
            (b == ']' and last == '[') or \
            (b == '}' and last == '{'):
                size -= 1
            else:
                return 0
                
    if size == 0:
        return 1
    return 0
