from typing import Optional, List
from collections import deque
from util import TreeNode, build_tree, print_tree

# Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left
# to right, level by level).


class Solution:
    # Recursive
    # Time Complexity: O(n)
    # Space Complexity: O(1) except for returned tree [call stack: O(log n) at one time]
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        return self.sortedArrayToBSTHelper(nums, 0, len(nums))

    def sortedArrayToBSTHelper(self, nums: List[int], start: int, end: int) -> Optional[TreeNode]:
        if end <= start:
            return None
        mid = (start + end) // 2
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBSTHelper(nums, start, mid)
        root.right = self.sortedArrayToBSTHelper(nums, mid+1, end)
        return root

    def sortedArrayToBSTHelperVariation(self, nums: List[int], start: int, end: int) -> Optional[TreeNode]:
        if end - start <= 0:
            return None
        if end - start == 1:
            return TreeNode(nums[start])
        mid = (start + end) // 2
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBSTHelper(nums, start, mid)
        root.right = self.sortedArrayToBSTHelper(nums, mid + 1, end)
        return root

    # Higher Space Complexity (as new lists are created at each recursive call)
    def sortedArrayToBSTNaive(self, nums: List[int]) -> Optional[TreeNode]:
        return self.sortedArrayToBSTHelperNaive(nums)

    def sortedArrayToBSTHelperNaive(self, nums: List[int]) -> Optional[TreeNode]:
        if len(nums) == 0:
            return None
        if len(nums) == 1:
            return TreeNode(nums[0])
        mid = len(nums) // 2
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBSTHelperNaive(nums[:mid])
        root.right = self.sortedArrayToBSTHelperNaive(nums[mid + 1:])
        return root


if __name__ == "__main__":
    test = [i for i in range(10)]
    print(f"input: {test}\noutput:")
    sol = Solution()
    print_tree(sol.sortedArrayToBST(test))
    print_tree(sol.sortedArrayToBSTNaive(test))

