
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def print_linked_list(head: ListNode, max_len: int = 100):
    cnt = 0
    while head.next is not None and cnt < max_len:
        print(f"{head.val} -> ", end="")
        head = head.next
        cnt += 1
    print(head.val)


def create_linked_list(frm: int, to: int, spacing: int = 1, cycle_pos: int = -1):
    res = ListNode(frm)
    curr = res
    cycle_idx, cycle_node = frm + cycle_pos*spacing if cycle_pos >= 0 else None, None
    for i in range(frm+spacing, to, spacing):
        curr.next = ListNode(i)
        if i == cycle_idx:
            cycle_node = curr.next
        curr = curr.next
    if cycle_node:
        curr.next = cycle_node
    return res
