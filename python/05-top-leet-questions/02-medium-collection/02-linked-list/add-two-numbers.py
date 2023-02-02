from typing import Optional
from util import ListNode, create_linked_list_by_list, print_linked_list


# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse
# order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Constraints:
# The number of nodes in each linked list is in the range [1, 100].
# 0 <= Node.val <= 9
# It is guaranteed that the list represents a number that does not have leading zeros.


class Solution:
    # Time Complexity: O(n) where n = max(len(l1), len(l2))
    # Space Complexity: O(1)
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        tail, is_switched = None, False
        head = l1
        carry = 0
        while l1 or l2 or carry:
            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0
            if l1:
                carry, l1.val = divmod(l1_val + l2_val + carry, 10)
                tail = l1
                l1 = l1.next
                l2 = l2 if not l2 else l2.next  # if none, stay none
            elif l2:
                if not is_switched:
                    tail.next = l2
                    is_switched = True  # to prevent redundant assignment
                carry, l2.val = divmod(l1_val + l2_val + carry, 10)
                tail = l2
                l2 = l2.next
            else:
                tail.next = ListNode(carry)
                carry = 0
        return head


if __name__ == "__main__":
    sol = Solution()
    l1, l2 = create_linked_list_by_list([2, 4, 3]), create_linked_list_by_list([5, 6, 4])
    res = sol.addTwoNumbers(l1, l2)
    print_linked_list(res)
