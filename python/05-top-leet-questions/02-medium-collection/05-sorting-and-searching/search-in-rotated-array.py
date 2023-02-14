from typing import List


# There is an integer array nums sorted in ascending order (with distinct values).

# Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length)
# such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed).
# For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

# Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums,
# or -1 if it is not in nums.

# You must write an algorithm with O(log n) runtime complexity.


class Solution:
    # Time Complexity: O(log n)
    # Space Complexity: O(1)
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            # base cases
            if nums[mid] == target:
                return mid
            elif nums[left] == target:
                return left
            elif nums[right] == target:
                return right
            elif right - left <= 2:
                return -1

            if nums[mid] > nums[left]:
                # left -> mid: ascending && mid -> right: pivoted
                if nums[left] < target < nums[mid]:
                    return self.searchBinary(nums, target, left, mid)
                else:
                    left = mid
            elif nums[mid] < nums[right]:
                # converse
                if nums[mid] < target < nums[right]:
                    return self.searchBinary(nums, target, mid, right)
                else:
                    right = mid
            else:
                return -1
        return -1

    def searchBinary(self, nums: List[int], target: int, lo: int, hi: int) -> int:
        while lo <= hi:
            mid = (lo + hi) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                lo = mid + 1
            else:
                hi = mid - 1
        return -1

    # Time Complexity: O(log n)
    # Space Complexity: O(1)
    def searchSimple(self, nums: List[int], target: int) -> int:
        pivot_idx = self.searchMinIdx(nums)

        # not actual lo, hi [will be calibrated based on pivot]
        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            mid_util = (lo + hi) // 2
            mid_actual = (mid_util + pivot_idx) % len(nums)
            if nums[mid_actual] == target:
                return mid_actual
            elif nums[mid_actual] < target:
                lo = mid_util + 1
            else:
                hi = mid_util - 1
        return -1

    def searchMinIdx(self, nums: List[int]) -> int:
        lo, hi = 0, len(nums) - 1
        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] > nums[hi]:
                lo = mid + 1
            else:
                hi = mid
        return lo


if __name__ == "__main__":
    sol = Solution()
    print(sol.search(nums=[4, 5, 6, 7, 0, 1, 2], target=0))
    print(sol.searchSimple(nums=[4, 5, 6, 7, 0, 1, 2], target=0))
    print(sol.search(nums=[4, 5, 6, 7, 0, 1, 2], target=7))
    print(sol.searchSimple(nums=[4, 5, 6, 7, 0, 1, 2], target=7))
    print(sol.search(nums=[4, 5, 6, 7, 0, 1, 2], target=3))
    print(sol.searchSimple(nums=[4, 5, 6, 7, 0, 1, 2], target=3))
    print(sol.search(nums=[1], target=0))
    print(sol.searchSimple(nums=[1], target=0))
