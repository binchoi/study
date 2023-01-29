from collections import deque

# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build_tree(size: int, balanced: bool = True):
    if size < 1:
        return None
    elif balanced:  # 3 -> 2 / 1 - 2 - 4 -8
        head = TreeNode(0)
        parent_nodes = deque([head])
        cnt = 1
        while cnt < size:
            parent_node = parent_nodes.popleft()
            parent_node.left = TreeNode(cnt)
            cnt += 1
            parent_nodes.append(parent_node.left)
            if cnt < size:
                parent_node.right = TreeNode(cnt)
                cnt += 1
                parent_nodes.append(parent_node.right)
        return head
    else:
        sentinel = prev = TreeNode()
        for i in range(size):
            prev.right = TreeNode(i)
            prev = prev.right
        return sentinel.right


def print_tree(head: Optional[TreeNode]):
    if not head:
        return

    res = [[head.val]]
    same_level_nodes = deque([head])
    while len(same_level_nodes) > 0:
        children = []
        while same_level_nodes:
            parent = same_level_nodes.popleft()
            if parent.left:
                children.append(parent.left)
            if parent.right:
                children.append(parent.right)
        same_level_nodes.extend(children)
        if children:
            res.append([c.val for c in children])
    print(f"=======TREE {str(head.__hash__())}=======", *res,
          sep="\n| ",
          end=f"\n=======TREE {str(head.__hash__())}=======\n")


if __name__ == "__main__":
    tree = build_tree(10, True)
    print_tree(tree)

    unbalanced_tree = build_tree(10, False)
    print_tree(unbalanced_tree)




