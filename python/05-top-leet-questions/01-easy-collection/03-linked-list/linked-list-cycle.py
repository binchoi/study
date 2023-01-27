import time
from typing import Optional
from util import ListNode, print_linked_list, create_linked_list

# Given head, the head of a linked list, determine if the linked list has a cycle in it.

# There is a cycle in a linked list if there is some node in the list that can be reached again by
# continuously following the next pointer. Internally, pos is used to denote the index of the node
# that tail's next pointer is connected to. Note that pos is not passed as a parameter.

# Return true if there is a cycle in the linked list. Otherwise, return false.


class Solution:
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def hasCycle(self, head: Optional[ListNode]) -> bool:  # rabit and hare algorithm
        fast = slow = head
        while slow and fast and fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
        return False


if __name__ == "__main__":
    test_head = create_linked_list(1, 6, 1, 2)

    print_linked_list(test_head)

    sol = Solution()
    print(sol.hasCycle(test_head))

