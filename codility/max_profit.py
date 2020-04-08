# Easy
# Given a log of stock prices compute the maximum possible earning.

def solution(A):
    
    if len(A) < 2:
        return 0
        
    max_profit = A[1] - A[0]
    cur_min = min(A[0], A[1])
    for i in A[2:]:
        max_cand = i - cur_min
        max_profit = max(max_profit, max_cand)
        cur_min = min(i, cur_min)
        
    max_profit = max(0, max_profit)
    return max_profit
        
        
