from typing import Optional
from util import ListNode, print_linked_list, create_linked_list


# Given the head of a singly linked list, reverse the list, and return the reversed list.

# Constraints:
# * The number of nodes in the list is the range [0, 5000].
# * -5000 <= Node.val <= 5000

# Follow up: A linked list can be reversed either iteratively or recursively. Could you implement both?


class Solution:
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None

        prev = None
        while head.next is not None:
            tmp = head.next  # save what is next in original list
            head.next = prev  # set the current node's next to the previous one (reverse!)
            prev = head  # set prev to current node
            head = tmp  # set head to the next node in sequence of original list
        head.next = prev  # last connection

        return head

    def reverseListSimplified(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        while head is not None:
            tmp = head.next  # save what is next in original list
            head.next = prev  # set the current node's next to the previous one (reverse!)
            prev = head  # set prev to current node
            head = tmp  # set head to the next node in sequence of original list

        return prev

    def reverseListRecursive(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.reverseListRecursiveHelper(None, head)

    def reverseListRecursiveHelper(self, prev: Optional[ListNode], head: Optional[ListNode]) -> Optional[ListNode]:
        if head is not None:
            tmp = head.next  # save what is next in original list
            head.next = prev  # set the current node's next to the previous one (reverse!)
            return self.reverseListRecursiveHelper(head, tmp)
        return prev

    def reverseListNaive(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None

        stk = []
        while head.next is not None:
            stk.append(head)
            head = head.next
        res = head

        while len(stk) > 0:
            head.next = stk.pop()
            head = head.next
        head.next = None

        return res


if __name__ == "__main__":
    test_head = create_linked_list(1, 6, 1, -1)

    print_linked_list(test_head)

    sol = Solution()
    res = sol.reverseListRecursive(test_head)

    print_linked_list(res)
