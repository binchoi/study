from typing import List, Dict
from collections import Counter


# Given a collection of numbers, nums, that might contain duplicates, return all possible unique
# permutations in any order.

# Constraints:
# * 1 <= nums.length <= 8
# * -10 <= nums[i] <= 10


class Solution:
    # Backtracking (= DFS) using recursion
    # Time Complexity: O(n!) [worst case: all unique elements]
    # Space Complexity: O(1)
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res, curr = [], []
        remaining = Counter(nums)  # dict containing frequency
        self.permuteUniqueHelper(nums, remaining, curr, res)
        return res

    def permuteUniqueHelper(self, nums: List[int], remaining: Dict[int, int], curr: List[int], res: List[List[int]]):
        if len(nums) == len(curr):
            res.append(curr[:])
            return
        for n in set(nums):
            if remaining.get(n, 0) > 0:
                remaining[n] -= 1
                curr.append(n)
                self.permuteUniqueHelper(nums, remaining, curr, res)
                curr.pop()
                remaining[n] += 1


if __name__ == "__main__":
    sol = Solution()
    print(sol.permuteUnique([1, 2, 3]))
    print(sol.permuteUnique([1, 1, 3]))
