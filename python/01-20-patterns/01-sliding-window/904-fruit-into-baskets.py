from dataclasses import dataclass
from typing import List, Optional, Tuple
import unittest


# https://leetcode.com/problems/contains-duplicate-ii/

# You are visiting a farm that has a single row of fruit trees arranged from left to right. The trees are represented
# by an integer array fruits where fruits[i] is the type of fruit the ith tree produces.

# You want to collect as much fruit as possible. However, the owner has some strict rules that you must follow:
#   You only have two baskets, and each basket can only hold a single type of fruit. There is no limit on the amount
#   of fruit each basket can hold.
#   Starting from any tree of your choice, you must pick exactly one fruit from every tree (including the start tree)
#   while moving to the right. The picked fruits must fit in one of your baskets.
#   Once you reach a tree with fruit that cannot fit in your baskets, you must stop.

# Given the integer array fruits, return the maximum number of fruits you can pick.

# Constraints:
# 1 <= fruits.length <= 105
# 0 <= fruits[i] < fruits.length

# SUMMARY: maximize number of pickable fruits (i.e. find the longest subsection of consecutive trees of only two types)


class Solution:
    # Time Complexity:  O(n)
    # Space Complexity: O(1)
    def totalFruit(self, fruits: List[int]) -> int:
        # base case
        if len(fruits) <= 2:
            return len(fruits)

        res = 2
        # 0,1 -> (fruit_type, idx)
        fruit_map = {
            0: (fruits[0], 0)  # init first fruit
        }

        for i in range(1, len(fruits)):
            fruit_type = fruits[i]
            if fruit_type not in set(tp for (tp, idx) in fruit_map.values()):
                if len(fruit_map) > 1:
                    res = max(i - fruit_map[0][1], res)  # compute sequence length
                    fruit_map[0] = fruit_map[1]  # shift window
                fruit_map[1] = (fruits[i], i)
        # compute and compare last sequence
        res = max(len(fruits) - fruit_map[0][1], res)

        return res


# Test
class TestSolution(unittest.TestCase):
    def test_solution(self):
        @dataclass
        class Args:
            fruits: List[int]

        @dataclass
        class TestCase:
            name: str
            input: Args
            expect: int

        cases = [
            TestCase(
                name="test 1",
                input=Args(fruits=[1, 2, 1]),
                expect=3
            ),
            TestCase(
                name="test 2",
                input=Args(fruits=[0, 1, 2, 2]),
                expect=3
            ),
            TestCase(
                name="test 3",
                input=Args(fruits=[1, 2, 3, 2, 2]),
                expect=4
            )
        ]

        for c in cases:
            solution = Solution()

            actual = solution.totalFruit(fruits=c.input.fruits)

            self.assertEqual(
                c.expect,
                actual,
                f"failed test {c.name} expected {c.expect}, actual {actual}"
            )


if __name__ == '__main__':
    unittest.main()
