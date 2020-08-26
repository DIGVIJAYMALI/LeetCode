'''

Given a positive integer num, write a function which returns True if num is a perfect square else False.

Follow up: Do not use any built-in library function such as sqrt.



Example 1:

Input: num = 16
Output: true
Example 2:

Input: num = 14
Output: false

'''

# USING BINARY SEARCH

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num == 1:
            return True
        low = 1
        high = num

        while low < high:
            mid = (low + high) // 2
            if mid * mid == num:
                return True
            elif mid * mid > num:
                high = mid
            else:
                low = mid + 1
        return False



# BY NEWTONS RAPSON
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        num =225
        if num == 1:
            return True

        # f(x) = x**2 - num

        h = lambda x: -(x*x - num) // (2*x)
        # initialize the function value for exponential decay
        x = num
        while x*x > num:
            x = x + h(x)
            print(x)

        return x*x == num
