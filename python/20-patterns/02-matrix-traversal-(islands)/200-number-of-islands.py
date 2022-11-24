from dataclasses import dataclass
from typing import List
import unittest


# https://leetcode.com/problems/number-of-islands/

# Given an m x n 2D binary grid which represents a map of '1's (land) and '0's (water), return
# the number of islands.

# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You
# may assume all four edges of the grid are all surrounded by water.

# Constraints:
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 300
# grid[i][j] is '0' or '1'.

# QnA: would it be correct to say that the minimum output is 1 (even if all values are 1) given that the four edges of
# the grid are surrounded by water? No. if all values are 0, then there would be 0 islands

class Solution:
    # Time Complexity:  O(n)
    # Space Complexity: O(n)
    def numIslands(self, grid: List[List[str]]) -> int:
        # add validation of grid

        res = 0

        # init island_map matrix
        island_map = len(grid) * [[0]*len(grid[0])]
        for y in range(len(grid)):
            for x in range(len(grid[y])):
                if grid[y][x] != 0 and island_map[y][x] == 0:  # previously undiscovered
                    res += 1
                    self.explore_island(grid, island_map, (x, y))
        return res

    def explore_island(self, grid, island_map, coord):
        coord_queue = [coord]
        while len(coord_queue) > 0:
            curr_coord = coord_queue.pop()
            x, y = curr_coord[0], curr_coord[1]
            print(f"Found island in coord: {x}, {y}")
            island_map[y][x] = 1  # this land is found

            # check land around (x, y)
            if x > 1 and island_map[y][x-1] == 0:
                coord_queue.append((x-1, y))
            if y > 1 and island_map[y-1][x] == 0:
                coord_queue.append((x, y-1))
            if x < len(grid[0])-1 and island_map[y][x+1] == 0:
                coord_queue.append((x+1, y))
            if y < len(grid)-1 and island_map[y+1][x] == 0:
                coord_queue.append((x, y+1))


# Test
class TestSolution(unittest.TestCase):
    def test_solution(self):
        @dataclass
        class Args:
            grid: List[List[str]]

        @dataclass
        class TestCase:
            name: str
            input: Args
            expect: int

        cases = [
            TestCase(
                name="test 1",
                input=Args(grid=[
                    ["1", "1", "1", "1", "0"],
                    ["1", "1", "0", "1", "0"],
                    ["1", "1", "0", "0", "0"],
                    ["0", "0", "0", "0", "0"]
                ]),
                expect=1
            ),
            TestCase(
                name="test 2",
                input=Args(grid=[
                    ["1", "1", "0", "0", "0"],
                    ["1", "1", "0", "0", "0"],
                    ["0", "0", "1", "0", "0"],
                    ["0", "0", "0", "1", "1"]
                ]),
                expect=3
            ),
        ]

        for c in cases:
            solution = Solution()

            actual = solution.numIslands(grid=c.input.grid)

            self.assertEqual(
                c.expect,
                actual,
                f"failed {c.name} expected {c.expect}, actual {actual}"
            )


if __name__ == '__main__':
    unittest.main()
