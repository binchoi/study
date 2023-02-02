from typing import Optional, List, Any
from util import ListNode, create_linked_list_by_list, print_linked_list, create_intersecting_linked_lists


# Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect. If the
# two linked lists have no intersection at all, return null.

# For example, the following two linked lists begin to intersect at node c1:

# The test cases are generated such that there are no cycles anywhere in the entire linked structure.

# Note that the linked lists must retain their original structure after the function returns.


class Solution:
    # Time Complexity: O(n+m)
    # Space Complexity: O(1)
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        a_len = self.get_linked_list_len(headA)
        b_len = self.get_linked_list_len(headB)
        if a_len < b_len:
            headB = self.skip_n_steps(headB, b_len - a_len)
        else:
            headA = self.skip_n_steps(headA, a_len - b_len)

        while headA and headA != headB:
            headA, headB = headA.next, headB.next
        return headA

    def get_linked_list_len(self, head: Optional[ListNode]) -> int:
        res = 0
        while head:
            res += 1
            head = head.next
        return res

    def skip_n_steps(self, head: ListNode, n: int) -> ListNode:
        while n > 0:
            head = head.next
            n -= 1
        return head

    # brute force
    # Time Complexity: O(n+m)
    # Space Complexity: O(n+m)
    def getIntersectionNodeNaive(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        stk_a = self.linked_list_to_stk(headA)
        stk_b = self.linked_list_to_stk(headB)
        res = None
        for i in range(0, min(len(stk_a), len(stk_b))):
            a, b = stk_a.pop(), stk_b.pop()
            if a == b:
                res = a
            else:
                break
        return res

    def linked_list_to_stk(self, head: Optional[ListNode]) -> List[Any]:
        stk = []
        res = head
        while head:
            stk.append(head)
            head = head.next
        return stk

    # Invalid solution (changes the structure of the linked list) - also, incorrect as reversing intersecting list
    # produces a linked list that requires a node that is able to point to two next nodes (which is impossible)
    # Time Complexity: O(n+m)
    # Space Complexity: O(1) [except, it modifies given lists]
    def getIntersectionNodeReverse(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        rev_a = self.reverse_linked_list(headA)
        rev_b = self.reverse_linked_list(headB)
        res = None
        print_linked_list(rev_a)
        print_linked_list(rev_b)
        while rev_a and rev_a == rev_b:
            res = rev_a
            rev_a, rev_b = rev_a.next, rev_b.next
        return res

    def reverse_linked_list(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        while head and head.next:
            nxt = head.next
            head.next = prev
            prev = head
            head = nxt
        head.next = prev
        print(f"check it out")
        print_linked_list(head)
        return head


if __name__ == "__main__":
    sol = Solution()
    l1, l2 = create_intersecting_linked_lists(intersectVal=8, listA=[4, 1, 8, 4, 5], listB=[5, 6, 1, 8, 4, 5], skipA=2,
                                              skipB=3)
    print_linked_list(l1)
    print_linked_list(l2)

    print(sol.getIntersectionNode(l1, l2).val)
    print(sol.getIntersectionNodeNaive(l1, l2).val)

    l1, l2 = create_intersecting_linked_lists(intersectVal=2, listA=[1, 9, 1, 2, 4], listB=[3, 2, 4], skipA=3, skipB=1)
    print_linked_list(l1)
    print_linked_list(l2)

    print(sol.getIntersectionNode(l1, l2).val)
    print(sol.getIntersectionNodeNaive(l1, l2).val)

    l1, l2 = create_intersecting_linked_lists(intersectVal=0, listA=[2, 6, 4], listB=[1, 5], skipA=3, skipB=2)
    print_linked_list(l1)
    print_linked_list(l2)

    print(sol.getIntersectionNode(l1, l2))
    print(sol.getIntersectionNodeNaive(l1, l2))
