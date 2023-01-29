from typing import Optional
from collections import deque
from util import TreeNode, build_tree, print_tree


# Given the root of a binary tree, return its maximum depth.

# A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the
# farthest leaf node.


class Solution:
    # Recursive
    # Time Complexity: O(n)
    # Space Complexity: O(1) [recursive call stack: O(n)]
    def maxDepthRecursive(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return 1+max(self.maxDepthRecursive(root.left), self.maxDepthRecursive(root.right))

    # Iterative
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def maxDepthIterative(self, root: Optional[TreeNode]) -> int:
        res = 0
        if not root:
            return res
        # bfs
        level_nodes = deque([root])
        while len(level_nodes) > 0:
            res += 1
            for i in range(len(level_nodes)):
                node = level_nodes.popleft()
                if node.left:
                    level_nodes.append(node.left)
                if node.right:
                    level_nodes.append(node.right)
        return res


if __name__ == "__main__":
    # Unbalanced Tree
    test_bst = build_tree(10, False)
    print_tree(test_bst)

    sol = Solution()
    print(sol.maxDepthRecursive(test_bst))
    print(sol.maxDepthIterative(test_bst))

    # Balanced Tree
    test_bst_2 = build_tree(10, True)
    print_tree(test_bst_2)

    sol = Solution()
    print(sol.maxDepthRecursive(test_bst_2))
    print(sol.maxDepthIterative(test_bst_2))

