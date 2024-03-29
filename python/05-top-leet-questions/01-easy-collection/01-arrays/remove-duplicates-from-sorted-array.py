from typing import List

# Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique
# element appears only once. The relative order of the elements should be kept the same.

# Since it is impossible to change the length of the array in some languages, you must instead have the result be
# placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates,
# then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first
# k elements.

# Return k after placing the final result in the first k slots of nums.

# Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1)
# extra memory.


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        remove_idx_lst = []
        for i in range(1, len(nums)):
            if nums[i - 1] == nums[i]:
                remove_idx_lst.append(i - 1)

        for i in remove_idx_lst[::-1]:
            nums.pop(i)

        return len(nums)

    def removeDuplicatesWithoutDeletes(self, nums: List[int]) -> int:
        count = 0  # number of duplicates found
        for i in range(1, len(nums)):
            if nums[i - 1] == nums[i]:
                count += 1
            else:
                nums[i-count] = nums[i-1]

        return len(nums)-count


if __name__ == "__main__":
    sol = Solution()
    print(sol.removeDuplicates([1, 1, 2]))
    print(sol.removeDuplicatesWithoutDeletes([1, 1, 2]))
