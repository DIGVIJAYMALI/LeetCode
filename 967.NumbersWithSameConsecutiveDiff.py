'''
Return all non-negative integers of length N such that the absolute difference between every two consecutive digits is K.

Note that every number in the answer must not have leading zeros except for the number 0 itself.
For example, 01 has one leading zero and is invalid, but 0 is valid.

You may return the answer in any order.
Example 1:
Input: N = 3, K = 7
Output: [181,292,707,818,929]
Explanation: Note that 070 is not a valid number, because it has leading zeroes.
Example 2:

Input: N = 2, K = 1
Output: [10,12,21,23,32,34,43,45,54,56,65,67,76,78,87,89,98]


N is a number and K is a difference.
'''
class Solution:
    def numsSameConsecDiff(self, N, K):

        if N == 1:
            return [0,1,2,3,4,5,6,7,8,9]
        result = []

        def dfs(prev, number):
            if len(number) == N:
                result.append(int(number))
                return
            for digit in [0,1,2,3,4,5,6,7,8,9]:
                if prev is None and digit == 0: continue
                if prev is None or abs(digit-prev) == K:
                    dfs(digit, number+str(digit))
        dfs(None, '')
        return result