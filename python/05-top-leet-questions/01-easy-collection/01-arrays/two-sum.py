from collections import deque
from typing import List


# Given an array of integers nums and an integer target, return indices of the two numbers such that they
# add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.


class Solution:
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        for i, n in enumerate(nums):
            if n in map:
                return [map[n], i]
            else:
                map[target - n] = i
        return [-1, -1]


if __name__ == "__main__":
    sol = Solution()
    nums = [1, 9, 0, 8, -100]
    print(sol.twoSum(nums, -92))

