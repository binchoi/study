from collections import deque
from typing import Optional
from util import build_tree, print_tree, Node


# You are given a perfect binary tree where all leaves are on the same level, and every parent has two children.
# The binary tree has the following definition:

# struct Node {
#   int val;
#   Node *left;
#   Node *right;
#   Node *next;
# }

# Populate each next pointer to point to its next right node. If there is no next right node, the next pointer
# should be set to NULL.
# Initially, all next pointers are set to NULL.

# Constraints:
# * The number of nodes in the tree is in the range [0, 212 - 1].
# * -1000 <= Node.val <= 1000

# Follow-up:
# * You may only use constant extra space.
# * The recursive approach is fine. You may assume implicit stack space does not count as extra space for this problem


class Solution:
    # Time Complexity: O(n)
    # Space Complexity: O(n)  # number of nodes in the leaf level
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return root

        dq = deque([root])
        while len(dq) > 0:
            prev = None
            for i in range(len(dq)):
                node = dq.popleft()
                if prev:
                    prev.next = node
                prev = node

                if node.left:
                    dq.append(node.left)
                if node.right:
                    dq.append(node.right)
        return root

    # Time Complexity: O(n)
    # Space Complexity: O(1)  [excluding implicit call stack]
    def connectDFSRecursion(self, root: 'Optional[Node]') -> 'Optional[Node]':
        curr, nxt = root, None
        self.dfs(root, None)
        return root

    def dfs(self, curr: 'Optional[Node]', nxt: 'Optional[Node]'):
        if not curr:
            return
        curr.next = nxt
        self.dfs(curr.left, curr.right)
        self.dfs(curr.right, nxt.left if nxt else None)

    # Time Complexity: > O(n)
    # Space Complexity: O(1)  [excluding implicit call stack]
    def connectRecursive(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return root

        left_child, right_child = self.connect(root.left), self.connect(root.right)
        if left_child and right_child:
            left_child.next = right_child
            while left_child.right and right_child.left:
                left_child.right.next = right_child.left
                left_child, right_child = left_child.right, right_child.left
        return root


if __name__ == "__main__":
    sol = Solution()
