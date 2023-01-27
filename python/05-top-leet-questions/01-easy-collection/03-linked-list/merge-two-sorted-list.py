from typing import Optional
from util import ListNode, print_linked_list, create_linked_list

# You are given the heads of two sorted linked lists list1 and list2.
# Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of
# the first two lists.

# Return the head of the merged linked list.

# NOTE: using a sentinel value as a head node can drastically simplify the code
# NOTE: replace `if x is not None` with `if x`


class Solution:
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        sentinel = ListNode(0)
        curr = sentinel
        while list1 and list2:
            if list1.val < list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next
        curr.next = list1 or list2
        return sentinel.next

    def mergeTwoListsNaive(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # base case
        if None in (list1, list2):
            return list2 if list1 is None else list1

        p1, p2 = list1, list2

        if p1.val < p2.val:
            head = p1
            p1 = p1.next
        else:
            head = p2
            p2 = p2.next

        prev = head
        while p1 is not None and p2 is not None:  # while both not none
            if p1.val < p2.val:
                prev.next = p1
                prev = p1
                p1 = p1.next
            else:
                prev.next = p2
                prev = p2
                p2 = p2.next

        prev.next = p2 if p1 is None else p1
        return head


if __name__ == "__main__":
    test_head1 = create_linked_list(1, 6, 2)
    test_head2 = create_linked_list(2, 7, 2)

    print_linked_list(test_head1)
    print_linked_list(test_head2)

    sol = Solution()
    res = sol.mergeTwoLists(test_head1, test_head2)

    print_linked_list(res)

