from typing import Optional
import unittest

# https://leetcode.com/problems/intersection-of-two-linked-lists/

# Given the heads of two singly linked-lists headA and headB, return the node at which the two lists
# intersect. If the two linked lists have no intersection at all, return null.

# For example, the following two linked lists begin to intersect at node c1:
# The test cases are generated such that there are no cycles anywhere in the entire linked structure.

# Note that the linked lists must retain their original structure after the function returns.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # Time Complexity:  O(n)
    # Space Complexity: O(n)
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        pass


# Test
# class TestSolution(unittest.TestCase):
#     def test_solution(self):
#         @dataclass
#         class Args:
#             nums: List[int]  # TODO: change this
#             k: int
#
#         @dataclass
#         class TestCase:
#             name: str
#             input: Args
#             expect: bool  # TODO: change this
#
#         cases = [
#             TestCase(
#                 name="test 1",
#                 input=Args(nums=[1, 2, 3, 1], k=3),  # TODO: write your test cases
#                 expect=True
#             ),
#             TestCase(
#                 name="test 2",
#                 input=Args(nums=[1, 0, 1, 1], k=1),
#                 expect=True
#             ),
#             TestCase(
#                 name="test 3",
#                 input=Args(nums=[1, 2, 3, 1, 2, 3], k=2),
#                 expect=False
#             )
#         ]
#
#         for c in cases:
#             solution = Solution()
#
#             actual = solution.someQuestion(nums=c.input.nums, k=c.input.k)  # TODO: change this
#
#             self.assertEqual(
#                 c.expect,
#                 actual,
#                 f"failed {c.name} expected {c.expect}, actual {actual}"
#             )


if __name__ == '__main__':
    unittest.main()
