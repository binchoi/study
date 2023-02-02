from typing import List, Any, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def create_linked_list_by_list(lst: List[int]) -> Optional[ListNode]:
    if not lst:
        return None
    head = ListNode(lst[0])
    prev = head
    for i in range(1, len(lst)):
        prev.next = ListNode(lst[i])
        prev = prev.next
    return head


def get_linked_list_and_tail_by_list(lst: List[int]) -> (Optional[ListNode], Optional[ListNode]):
    if not lst:
        return None, None
    head = ListNode(lst[0])
    prev = head
    for i in range(1, len(lst)):
        prev.next = ListNode(lst[i])
        prev = prev.next
    return head, prev


# intersectVal - The value of the node where the intersection occurs. This is 0 if there is no intersected node.
# listA - The first linked list.
# listB - The second linked list.
# skipA - The number of nodes to skip ahead in listA (starting from the head) to get to the intersected node.
# skipB - The number of nodes to skip ahead in listB (starting from the head) to get to the intersected node.
def create_intersecting_linked_lists(intersectVal: int, listA: List[int], listB: List[int], skipA: int, skipB: int) -> (ListNode, ListNode):
    if intersectVal == 0:
        return create_linked_list_by_list(listA), create_linked_list_by_list(listB)
    # create linked list A
    list_a = create_linked_list_by_list(listA)
    # find intersect node
    intersect_node = skip_n_steps(list_a, skipA)
    list_b, tail_b = get_linked_list_and_tail_by_list(listB[:skipB])
    if not list_b:
        list_b = intersect_node
    else:
        # link list_b with list_a
        tail_b.next = intersect_node
    return list_a, list_b


def skip_n_steps(head: ListNode, n: int) -> ListNode:
    while n > 0:
        head = head.next
        n -= 1
    return head


def print_linked_list(head: Optional[ListNode]):
    while head:
        print(f"{head.val} -> ", end="")
        head = head.next
    print("nil")
