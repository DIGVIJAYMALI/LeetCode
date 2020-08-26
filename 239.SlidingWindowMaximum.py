'''
Given an array nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position. Return the max sliding window.

Follow up:
Could you solve it in linear time?

Example:

Input: nums = [1,3,-1,-3,5,3,6,7], and k = 3
Output: [3,3,5,5,6,7]
Explanation:

Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7


SMART USE OF DEQUE
'''

import collections as cl

class Solution:

    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        dq = cl.deque()
        res= []
        for i, num in enumerate(nums):
            # while current num is greater than recently pushed in deque
            while dq and num > nums[dq[-1]]:
                dq.pop()
            #push index i of current
            dq.append(i)
            # if window size exceeds popleft
            # you will know your windows size by 'i-dq[0]'
            if i - dq[0] >= k:
                dq.popleft()

            # if window size reached, append dq[0] to result
            # we are using 'k-1' as we are starting from index '0'
            if i >= k-1:
                res.append(nums[dq[0]])
        return res


