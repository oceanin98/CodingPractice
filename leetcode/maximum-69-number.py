# Python 3
# https://leetcode.com/problems/maximum-69-number

class Solution:
    def maximum69Number (self, num: int) -> int:
        numlist = list(str(num))

        for i, n in enumerate(numlist):
            if n == '6':
                numlist[i] = '9'
                break

        return int(''.join(numlist))
