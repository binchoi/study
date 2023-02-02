from typing import Optional, List
from util import TreeNode, build_tree, print_tree


# Given the root of a binary tree, return the inorder traversal of its nodes' values.


class Solution:
    # Time Complexity: O(n)
    # Space Complexity: O(log n) - height of the tree
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        stk = []
        while root or stk:
            while root:
                stk.append(root)
                root = root.left
            root = stk.pop()
            res.append(root.val)
            root = root.right
        return res


if __name__ == "__main__":
    sol = Solution()
    t = build_tree(10)
    print_tree(t)
    print(sol.inorderTraversal(t))

