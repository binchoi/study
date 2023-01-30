from typing import List

# Given an integer array nums, find the subarray with the largest sum, and return its sum.

# Follow up: If you have figured out the O(n) solution, try coding another solution using the divide and
# conquer approach, which is more subtle.


class Solution:
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def maxSubArray(self, nums: List[int]) -> int:
        # base case
        if len(nums) < 2:
            return sum(nums)

        window, res = 0, -(10 ** 20) - 1
        for i in range(len(nums)):
            window += nums[i]
            res = max(res, window)
            if window < 0:
                window = 0
        return res

    def maxSubArrayShort(self, nums: List[int]) -> int:
        res = max_including_this = nums[0]
        for i in range(1, len(nums)):
            max_including_this = max(max_including_this + nums[i], nums[i])
            res = max(res, max_including_this)
        return res

    # Divide and Conquer
    # Time Complexity: O(n log n)
    # Space Complexity: O(1)
    def maxSubArrayDnC(self, nums: List[int]) -> int:
        return self.maxSubArrayHelper(nums, 0, len(nums)-1)[2]

    def maxSubArrayHelper(self, nums: List[int], start: int, end: int) -> (int, int, int):
        if start == end:
            return start, end, nums[start]
        mid = (start + end) // 2
        l_start, l_end, l_max = self.maxSubArrayHelper(nums, start, mid)
        r_start, r_end, r_max = self.maxSubArrayHelper(nums, mid+1, end)
        c_start, c_end, c_max = self.maxSubArrayHelperAcross(nums, start, mid, end)
        if l_max >= r_max and l_max >= c_max:
            return l_start, l_end, l_max
        elif r_max > l_max and r_max >= c_max:
            return r_start, r_end, r_max
        else:
            return c_start, c_end, c_max

    def maxSubArrayHelperAcross(self, nums: List[int], start: int, mid: int, end: int) -> (int, int, int):
        l_max = - (10**4) - 1
        l_cumulative, c_start = 0, mid
        for i in range(mid, start-1, -1):
            l_cumulative += nums[i]
            if l_cumulative>l_max:
                l_max = l_cumulative
                c_start = i

        r_max = - (10**4) - 1
        r_cumulative, c_end = 0, mid+1
        for i in range(mid+1, end+1):
            r_cumulative += nums[i]
            if r_cumulative>r_max:
                r_max = r_cumulative
                c_end = i
        return c_start, c_end, l_max + r_max

    # If empty array is a valid output (misinterpreted)
    # Time Complexity: O(n)
    # Space Complexity: O(1)
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



if __name__ == "__main__":
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    sol = Solution()
    print(sol.maxSubArray(nums))
    print(sol.maxSubArrayShort(nums))
