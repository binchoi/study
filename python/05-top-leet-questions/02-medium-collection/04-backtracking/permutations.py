from typing import List, Set


# Given an array nums of distinct integers, return all the possible permutations. You can return the answer
# in any order.

# Constraints:
# * 1 <= nums.length <= 6
# * -10 <= nums[i] <= 10
# * All the integers of nums are unique.


class Solution:
    # Backtracking (= DFS) using recursion
    # Time Complexity: O(n!)
    # Space Complexity: O(1) (excluding return data)
    def permute(self, nums: List[int]) -> List[List[int]]:
        remaining = set(nums)
        res, curr = [], []
        self.permute_helper(nums, remaining, curr, res)
        return res

    def permute_helper(self, nums: List[int], remaining: Set[int], curr: List[int], res: List[List[int]]):
        if len(nums) == len(curr):
            res.append(curr[:])  # make a copy!
            return
        for n in nums:
            if n in remaining:
                remaining.remove(n)
                curr.append(n)
                self.permute_helper(nums, remaining, curr, res)
                curr.pop()
                remaining.add(n)


if __name__ == "__main__":
    sol = Solution()
    print(sol.permute([1, 2, 3]))
