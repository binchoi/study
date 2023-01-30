
# Given an integer array nums, find the subarray with the largest sum, and return its sum.
from typing import List


class Solution:
    # Memoization
    # Time Complexity: O(n)
    # Space Complexity: O(n) [+ O(n) call stack]
    def maxSubArrayMisinterpreted(self, nums: List[int]) -> int:
        # base case
        if len(nums) < 2:
            return sum(nums)

        left = 0  # left = to subtract next, right = to add now
        window, res = 0, 0
        for right in range(len(nums)):
            window += nums[right]
            if window < 0:
                left = right + 1
                window = 0
            else:
                res = max(res, window)
        return res

    def maxSubArray(self, nums: List[int]) -> int:
        # base case
        if len(nums) < 2:
            return sum(nums)

        left = 0  # left = to subtract next, right = to add now
        window, res = 0, -(10 ** 20) - 1
        for right in range(len(nums)):
            window += nums[right]
            res = max(res, window)
            if window < 0:  # iffy
                left = right + 1
                window = 0
        return res

    # Sliding Window
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2

        a, b = 1, 2
        for i in range(2, n):
            temp_b = b
            b = a + b
            a = temp_b

        return b

    def climbStairsSWusingWhile(self, n: int) -> int:
        # base-case
        if n == 1:
            return 1
        if n == 2:
            return 2

        n -= 2
        a, b = 1, 2
        while n > 0:
            t_b = b
            b = a+b
            a = t_b
            n -= 1
        return b


if __name__ == "__main__":
    sol = Solution()
    print(sol.climbStairsMemo(5))
    print(sol.climbStairs(9))
