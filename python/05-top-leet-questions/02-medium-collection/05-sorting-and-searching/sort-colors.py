from collections import Counter
from typing import List, Set


# Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of
# the same color are adjacent, with the colors in the order red, white, and blue.

# We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.
# You must solve this problem without using the library's sort function.

# Follow up: Could you come up with a one-pass algorithm using only constant extra space?

class Solution:
    # Two-pointer Solution (actually more like 3) - [Dutch Partitioning Problem]
    # Time Complexity: O(n) [1 pass]
    # Space Complexity: O(1)
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i, j = 0, len(nums) - 1
        while i < len(nums) and nums[i] == 0:
            i += 1
        curr = i

        while j >= 0 and nums[j] == 2:
            j -= 1

        while i <= curr <= j:
            if nums[curr] == 2:
                nums[curr], nums[j] = nums[j], nums[curr]
                while curr <= j and nums[j] == 2:  # to prevent 2's being swapped back
                    j -= 1
            if nums[curr] == 0:
                nums[curr], nums[i] = nums[i], nums[curr]
                while i <= j and nums[i] == 0:  # to prevent 0's being swapped forward
                    i += 1
            curr = max(curr + 1, i)

    # Same Time/Space Complexities as above
    def sortColorsSimplified(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i, curr, j = 0, 0, len(nums) - 1
        while curr <= j:  # no need to have one pointer that increments every iteration!
            if nums[curr] == 2:
                nums[curr], nums[j] = nums[j], nums[curr]
                j -= 1
            elif nums[curr] == 0:
                nums[curr], nums[i] = nums[i], nums[curr]
                i += 1
                curr += 1
            else:
                curr += 1

    # HashMap / Brute-force
    # Time Complexity: O(n) [2 pass]
    # Space Complexity: O(n) [hashmap]
    def sortColorsNaive(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        freq_map = Counter(nums)  # O(n)
        i, curr = 0, 0
        while curr < 3:
            while freq_map.get(curr, 0) > 0:
                nums[i] = curr
                i += 1
                freq_map[curr] -= 1
            curr += 1


if __name__ == "__main__":
    sol = Solution()
    nums = [0, 2, 2, 1, 1, 1, 1, 0, 0, 1, 2, 0]
    sol.sortColors(nums)
    print(nums)

    nums = [0, 2, 2, 1, 1, 1, 1, 0, 0, 1, 2, 0]
    sol.sortColorsSimplified(nums)
    print(nums)

    nums = [0, 2, 2, 1, 1, 1, 1, 0, 0, 1, 2, 0]
    sol.sortColorsNaive(nums)
    print(nums)
