from typing import List


# Given an array of integers nums sorted in non-decreasing order, find the starting and ending
# position of a given target value.

# If target is not found in the array, return [-1, -1].

# You must write an algorithm with O(log n) runtime complexity.


class Solution:
    # Binary Search (with a twist)
    # Time Complexity: O(log n) [b/c O(2 log n) = O(log n)]
    # Space Complexity: O(1)
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start = self.searchFstOccurance(nums, target)
        if start == -1:
            return [-1, -1]

        end = self.searchLstOccurance(nums, target)
        return [start, end]

    def searchFstOccurance(self, nums: List[int], target: int) -> int:
        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if nums[mid] < target:
                lo = mid + 1  # if not + 1, infinite loop
            elif nums[mid] > target:
                hi = mid - 1  # if not - 1, infinite loop
            else:
                if mid - 1 < 0 or nums[mid - 1] < nums[mid]:
                    return mid
                else:
                    hi = mid - 1
        return -1

    def searchLstOccurance(self, nums: List[int], target: int) -> int:
        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if nums[mid] < target:
                lo = mid + 1
            elif nums[mid] > target:
                hi = mid - 1
            else:
                if mid + 1 >= len(nums) or nums[mid + 1] > nums[mid]:
                    return mid
                else:
                    lo = mid + 1
        return -1

    # same as above
    def searchRangeRefactored(self, nums: List[int], target: int) -> List[int]:
        start = self.searchEdgeOccurance(nums, target, True)
        if start == -1:
            return [-1, -1]

        end = self.searchEdgeOccurance(nums, target, False)
        return [start, end]

    def searchEdgeOccurance(self, nums: List[int], target: int, is_fst: bool) -> int:
        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if nums[mid] < target:
                lo = mid + 1
            elif nums[mid] > target:
                hi = mid - 1
            else:
                if is_fst:
                    if mid - 1 < 0 or nums[mid - 1] < nums[mid]:
                        return mid
                    else:
                        hi = mid - 1
                else:
                    if mid + 1 >= len(nums) or nums[mid + 1] > nums[mid]:
                        return mid
                    else:
                        lo = mid + 1
        return -1

    # TODO: Can simplify if we don't insist on returning during binary search but assessing vals after
    #  exiting from while-loop
    #  (https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/solutions/14734/easy-java-o-logn-solution/)


if __name__ == "__main__":
    sol = Solution()
    print(sol.searchRange(nums=[5, 7, 7, 8, 8, 10], target=8))
    print(sol.searchRangeRefactored(nums=[5, 7, 7, 8, 8, 10], target=8))
    print(sol.searchRange(nums=[5, 7, 7, 8, 8, 10], target=6))
    print(sol.searchRangeRefactored(nums=[5, 7, 7, 8, 8, 10], target=6))
    print(sol.searchRange(nums=[], target=0))
    print(sol.searchRangeRefactored(nums=[], target=0))
