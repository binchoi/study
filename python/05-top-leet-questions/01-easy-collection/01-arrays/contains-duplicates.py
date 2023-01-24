from collections import deque
from typing import List


# Given an integer array nums, return true if any value appears at least twice in the array, and return false
# if every element is distinct.


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for n in nums:
            if n in seen:
                return True
            else:
                seen.add(n)
        return False


if __name__ == "__main__":
    sol = Solution()
    nums = [1, 3, 2]
    print(sol.containsDuplicate(nums))
