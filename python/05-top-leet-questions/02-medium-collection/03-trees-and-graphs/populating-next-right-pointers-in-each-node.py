from typing import Optional
from util import build_tree, print_tree


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
    # Time Complexity:
    # Space Complexity:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        pass


if __name__ == "__main__":
    sol = Solution()
    t = build_tree(10)
    print_tree(t)
    # print(sol.connect(t))

