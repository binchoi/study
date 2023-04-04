from typing import Optional
from util import ListNode, create_linked_list, print_linked_list


# Remove duplicates from an unsorted linked list


class Solution:
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def removeDups(self, head: Optional[ListNode]) -> Optional[ListNode]:
        seen = set()
        prev = None
        while head is not None:
            if head.val in seen:
                head = head.next
            else:
                prev = head
                head = head.next

if __name__ == "__main__":
    sol = Solution()

    test_head = create_linked_list(1, 6)
    print_linked_list(test_head)

    # sol.removeDups()
