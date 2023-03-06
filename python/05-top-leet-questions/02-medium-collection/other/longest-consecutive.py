from collections import defaultdict
from typing import List

# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
# You must write an algorithm that runs in O(n) time.


class Solution:
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        res = 0
        for n in nums_set:
            # only continue if it is the beginning of a streak
            if n - 1 in nums_set:
                continue

            curr = n + 1
            while curr in nums_set:
                curr += 1
            res = max(res, curr - n)
        return res


    def longestConsecutiveAlternative(self, nums: List[int]) -> int:
        res = 0
        m = defaultdict(int)
        for n in nums:
            if m[n] > 0:  # instead of n in m b/c defaultdict adds similar keys (optimization)
                continue

            left, right = m[n-1], m[n+1]
            sum = left + right + 1
            m[n] = sum  # len of seq of n

            # update res
            res = max(res, sum)

            # update the length to the boundaries of the sequence (left, right only)
            m[n-left] = sum
            m[n+right] = sum
        return res


if __name__ == "__main__":
    sol = Solution()
    nums = [100, 4, 200, 1, 3, 2]
    nums2 = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]

    print(sol.longestConsecutive(nums))
    print(sol.longestConsecutive(nums2))
    print(sol.longestConsecutiveAlternative(nums))
    print(sol.longestConsecutiveAlternative(nums2))
