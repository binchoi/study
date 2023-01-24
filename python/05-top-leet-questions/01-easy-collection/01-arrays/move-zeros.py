from collections import deque
from typing import List


# Given an integer array nums, move all 0's to the end of it while maintaining the relative
# order of the non-zero elements.

# Note that you must do this in-place without making a copy of the array.


class Solution:
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        pointer = 0
        for i, n in enumerate(nums):
            if n != 0:
                nums[pointer] = n
                pointer += 1
        nums[pointer:] = [0] * (len(nums) - pointer)


if __name__ == "__main__":
    sol = Solution()
    nums = [1, 9, 0, 8, 0, 9, 9, 0, 0, 0]
    print(nums)
    sol.moveZeroes(nums)
    print(nums)
