# Calculate the values of counters after applying all alternating operations:
# Increase counter by 1; set value of all counters to current maximum
# Medium

'''
You are given N counters, initially set to 0, and you have two possible operations on them:

increase(X) − counter X is increased by 1,
max counter − all counters are set to the maximum value of any counter.
A non-empty array A of M integers is given. This array represents consecutive operations:

if A[K] = X, such that 1 ≤ X ≤ N, then operation K is increase(X),
if A[K] = N + 1 then operation K is max counter.

The goal is to calculate the value of every counter after all operations.

Write a function:

def solution(N, A)

that, given an integer N and a non-empty array A consisting of M integers,
returns a sequence of integers representing the values of the counters.

Result array should be returned as an array of integers.

Write an efficient algorithm for the following assumptions:

N and M are integers within the range [1..100,000];
each element of array A is an integer within the range [1..N + 1].
'''

def solution(N, A):
    result = [0] * N
    maximum = 0
    flag = 0 # not using flag returns time limit, a group of max_counter should only carry out max_counter ONCE
    
    for i in range(len(A)):
        if A[i] == N + 1:
            flag = 1
        
        else:
            if flag == 1:
                result = [maximum] * N
            result[A[i] - 1] += 1
            maximum = max(maximum, result[A[i] - 1]) # using "max(result)" returns time limit
            flag = 0
    
    if flag == 1:
        result = [maximum] * N
    return result
