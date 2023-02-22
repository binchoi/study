from typing import List


# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and
# j != k, and nums[i] + nums[j] + nums[k] == 0..


class Solution:
    # Two pointer application
    # Time Complexity: O(n^2)
    # Space Complexity: O(1)
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # sort
        nums.sort()
        res = []
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            target = 0 - nums[i]
            lo, hi = i + 1, len(nums) - 1
            while lo < hi:
                curr = nums[lo] + nums[hi]
                if curr == target:
                    res.append([nums[i], nums[lo], nums[hi]])
                    lo += 1
                    # skip all duplicates
                    while lo < hi and nums[lo] == nums[lo - 1]:
                        lo += 1
                    while lo < hi and nums[hi] == nums[hi - 1]:
                        hi -= 1
                elif curr < target:
                    lo += 1
                else:
                    hi -= 1
        return res


if __name__ == "__main__":
    sol = Solution()
    nums = [-1, 0, 1, 2, -1, -4]

    print(sol.threeSum(nums))
