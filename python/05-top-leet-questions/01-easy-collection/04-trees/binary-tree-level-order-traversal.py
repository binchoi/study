from typing import Optional, List
from collections import deque
from util import TreeNode, build_tree, print_tree

# Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left
# to right, level by level).


class Solution:
    # Iterative
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        # queue
        res = [[root.val]]
        parents = deque([root])
        while len(parents) > 0:
            level_nodes_val = []
            for i in range(len(parents)):  # pop only existing parent nodes (of prev level) using len
                p = parents.popleft()
                if p.left:
                    level_nodes_val.append(p.left.val)
                    parents.append(p.left)
                if p.right:
                    level_nodes_val.append(p.right.val)
                    parents.append(p.right)
            if len(level_nodes_val) > 0:
                res.append(level_nodes_val)
        return res

    # can remove boiler plate code
    def levelOrderSimilar(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        # queue
        res = []  # init as empty
        parents = deque([root])
        while len(parents) > 0:
            level_nodes_val = []
            for i in range(len(parents)):  # pop only existing parent nodes (of prev level) using len
                p = parents.popleft()
                level_nodes_val.append(p.val)
                if p.left:
                    parents.append(p.left)
                if p.right:
                    parents.append(p.right)
            res.append(level_nodes_val)
        return res

    # Recursive (just for exploration)
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def levelOrderRecursive(self, root: Optional[TreeNode]) -> List[List[int]]:
        res: List[List[int]] = []
        self.levelOrderRecursiveHelper(root, res, 0)
        return res

    def levelOrderRecursiveHelper(self, root: Optional[TreeNode], res: List[List[int]], height: int):
        # python passes arguments by assignment (similar to pass-by-reference with mutable data e.g. lists)
        # note: if new list is created and assigned to res, the outer scope will still be pointing to the original res.
        if not root:
            return
        if len(res) <= height:  # len(res) < height will never occur (i.e. only len(res)=height occurs)
            res.append([])
            if len(res) <= height:
                raise Exception("Something is off")
        res[height].append(root.val)
        self.levelOrderRecursiveHelper(root.left, res, height+1)
        self.levelOrderRecursiveHelper(root.right, res, height+1)


if __name__ == "__main__":
    # Unbalanced Tree
    test_bst = build_tree(10, False)
    print_tree(test_bst)

    sol = Solution()
    print(sol.levelOrder(test_bst))
    print(sol.levelOrderSimilar(test_bst))
    print(sol.levelOrderRecursive(test_bst))

    # Balanced Tree
    test_bst_2 = build_tree(10, True)
    print_tree(test_bst_2)

    sol = Solution()
    print(sol.levelOrder(test_bst_2))
    print(sol.levelOrderSimilar(test_bst_2))
    print(sol.levelOrderRecursive(test_bst_2))

