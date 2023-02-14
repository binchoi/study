from typing import List


# Given an integer array nums of unique elements, return all possible subsets (the power set).

# The solution set must not contain duplicate subsets. Return the solution in any order.


class Solution:
    # Backtracking
    # Time Complexity: O(2^n) where n = len(nums)
    # Space Complexity: O(n) excluding call stack
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res, curr = [], []
        self.subsets_helper(nums, 0, [], res)
        return res

    def subsets_helper(self, nums: List[int], i: int, curr: List[int], res: List[List[int]]):
        if i == len(nums):
            res.append(curr[:])  # copy
            return

        self.subsets_helper(nums, i + 1, curr, res)
        curr.append(nums[i])
        self.subsets_helper(nums, i + 1, curr, res)
        curr.pop()

    # Time Complexity: O(2^n) where n = len(nums)
    # Space Complexity: O(1) excluding output array
    def subsets_iterative(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for n in nums:
            res += [r + [n] for r in res]
        return res


if __name__ == "__main__":
    sol = Solution()
    print(sol.subsets([1]))
    print(sol.subsets([1, 2, 3]))
    print(sol.subsets([1, 2, 3, 4, 5]))
    print(sol.subsets_iterative([1]))
    print(sol.subsets_iterative([1, 2, 3]))
    print(sol.subsets_iterative([1, 2, 3, 4, 5]))

