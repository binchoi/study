from typing import List, Tuple
from enum import Enum

# The alternating sum of a 0-indexed array is defined as the sum of the elements at even indices minus the sum of
# the elements at odd indices.

# For example, the alternating sum of [4,2,5,3] is (4 + 5) - (2 + 3) = 4.
# Given an array nums, return the maximum alternating sum of any subsequence of nums (after reindexing the elements
# of the subsequence).

# A subsequence of an array is a new array generated from the original array by deleting some elements (possibly none)
# without changing the remaining elements' relative order. For example, [2,7,4] is a subsequence of [4,2,3,7,2,1,4]
# (the underlined elements), while [2,4,2] is not.


# class State(Enum):
#     LOCAL_MAXIMA_SEARCHING = 1
#     LOCAL_MINIMA_SEARCHING = 2


class Solution:
    # enum
    LOCAL_MAXIMA_SEARCH_STATE = 0
    LOCAL_MINIMA_SEARCH_STATE = 1

    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def maxAlternatingSum(self, nums: List[int]) -> int:
        state = self.LOCAL_MAXIMA_SEARCH_STATE
        i = 0
        res = 0
        while i < len(nums):
            if state == self.LOCAL_MAXIMA_SEARCH_STATE:
                if i == len(nums) - 1:
                    res += nums[i]
                elif nums[i + 1] < nums[i]:
                    res += nums[i]
                    state = self.LOCAL_MINIMA_SEARCH_STATE
            else:
                if i < len(nums) - 1 and nums[i + 1] > nums[i]:
                    res -= nums[i]
                    state = self.LOCAL_MAXIMA_SEARCH_STATE
            i += 1
        return res


if __name__ == "__main__":
    sol = Solution()
    nums = [6, 2, 1, 2, 4, 5]
    print(sol.maxAlternatingSum(nums))
