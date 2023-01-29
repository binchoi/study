from collections import deque

from typing import Optional, List
from util import TreeNode, build_tree, print_tree


# IN-ORDER: LEFT - ROOT - RIGHT
# USE-CASES
# * Non-decreasing traversal of Binary Search Tree (or strictly increasing, depending on definition of BST)

def in_order_traversal(head: Optional[TreeNode]) -> List[int]:
    res = []
    stk = []
    while head or len(stk) > 0:
        while head:
            stk.append(head)
            head = head.left  # LEFT
        head = stk.pop()
        res.append(head.val)  # ROOT
        head = head.right     # RIGHT
    return res


# PRE-ORDER: ROOT - LEFT - RIGHT
# USE-CASES
# * Copying a Tree
# * Finding prefix expression of Expression Tree

def pre_order_traversal(head: Optional[TreeNode]) -> List[int]:
    res = []
    stk = []
    while head or len(stk) > 0:
        while head:
            res.append(head.val)  # ROOT
            stk.append(head)
            head = head.left      # LEFT
        head = stk.pop()
        head = head.right         # RIGHT
    return res


# POST-ORDER: LEFT - RIGHT - ROOT
# USE-CASES
# * Deleting a Tree
# * Finding postfix expression of Expression Tree

def post_order_traversal(head: Optional[TreeNode]) -> List[int]:
    res = []
    stk = []
    while head or len(stk) > 0:
        while head:
            if head.right:
                stk.append(head.right)  # 2.1a
            stk.append(head)            # 2.1a
            head = head.left            # LEFT

        head = stk.pop()
        if head.right and (len(stk) > 0 and head.right == stk[-1]):
            stk.pop()
            stk.append(head)
            head = head.right           # RIGHT
        else:
            res.append(head.val)        # ROOT
            head = None

    return res

# notes of above implementation
# 1.1 Create an empty stack
# 2.1 Do following while root is not NULL
#     a) Push root's right child and then root to stack.
#     b) Set root as root's left child.
# 2.2 Pop an item from stack and set it as root.
#     a) If the popped item has a right child and the right child
#        is at top of stack, then remove the right child from stack,
#        push the root back and set root as root's right child.
#     b) Else print root's data and set root as NULL.
# 2.3 Repeat steps 2.1 and 2.2 while stack is not empty.


# LEVEL-ORDER: TOP -> DOWN by LEVEL (bfs)
def level_order_traversal(head: Optional[TreeNode]) -> List[int]:
    if not head:
        return []
    res = []
    q = deque([head])
    while len(q) > 0:
        for i in range(len(q)):
            node = q.popleft()
            res.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
    return res


if __name__ == "__main__":
    tree = build_tree(10)
    print_tree(tree)
    # ||            0          ||
    # ||      1/        \2     ||
    # ||    3/   \4   5/  \6   ||
    # ||  7/ \8 9/             ||

    print(in_order_traversal(tree))
    print(pre_order_traversal(tree))
    print(post_order_traversal(tree))
    print(level_order_traversal(tree))
