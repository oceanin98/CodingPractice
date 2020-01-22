# Difficulty: Easy
# Count minimal number of jumps from position X to Y.

"""
A small frog wants to get to the other side of the road. 
The frog is currently located at position X,
and wants to get to a position greater than or equal to Y. 
The small frog always jumps a fixed distance, D.

Count the minimal number of jumps that the small frog must perform to reach its target.

Write an efficient algorithm for the following assumptions:

 - X, Y and D are integers within the range [1..1,000,000,000];
 - X ≤ Y.
"""

def solution(X, Y, D):
    if X == Y:
        return 0
    if (Y - X)/D > (Y - X) //D:
        return (Y - X) //D + 1
    return (Y - X) //D
