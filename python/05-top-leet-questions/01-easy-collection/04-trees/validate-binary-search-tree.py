from typing import Optional
from util import TreeNode, build_tree, print_tree

# Given the root of a binary tree, determine if it is a valid binary search tree (BST).

# A valid BST is defined as follows:
# * The left subtree of a node contains only nodes with keys less than the node's key.
# * The right subtree of a node contains only nodes with keys greater than the node's key.
# * Both the left and right subtrees must also be binary search trees.


class Solution:
    # In-order traversal (left-root-right) [iterative]
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        stk = []
        prev_val = - (2 ** 31)-1
        while root or len(stk) > 0:
            while root:  # nested while-loop is key
                stk.append(root)
                root = root.left
            root = stk.pop()
            if root.val <= prev_val:
                return False
            prev_val = root.val
            root = root.right
        return True

    # In-order traversal [Recursive Approach] - leetcode example
    def isValidBSTRecursiveInorder(self, root: TreeNode) -> bool:
        def inorder(root):
            # base case
            if not root:
                return True
            # left
            if not inorder(root.left):
                return False
            # root
            if root.val <= self.prev:
                return False
            self.prev = root.val
            # right
            return inorder(root.right)

        self.prev = - (2 ** 31)-1
        return inorder(root)

    # Recursive Approach (Divide-and-Conquer)
    # Time Complexity: O(n)
    # Space Complexity: O(1) [O(n) call stack]
    def isValidBSTRecursive(self, root: Optional[TreeNode]) -> bool:
        return self.isValidBSTHelper(root, -(2 ** 31) - 1, 2 ** 31)

    def isValidBSTHelper(self, root: Optional[TreeNode], low: int, high: int):
        if not root:
            return True
        if root.val <= low or high <= root.val:
            return False
        return self.isValidBSTHelper(root.left, low, root.val) and self.isValidBSTHelper(root.right, root.val, high)


if __name__ == "__main__":
    # Non-BST Tree
    test_bst = build_tree(10, True)
    print_tree(test_bst)

    sol = Solution()
    print(sol.isValidBST(test_bst))
    print(sol.isValidBSTRecursive(test_bst))

