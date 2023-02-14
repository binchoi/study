from typing import List


# Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return
# the number of islands.

# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
# You may assume all four edges of the grid are all surrounded by water.


class Solution:
    # Time Complexity: O(n*m)
    # Space Complexity: O(n*m) (-> can make O(1) if grid table is used to record visited)
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = [[False] * len(grid[0]) for _ in range(len(grid))]
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1" and not visited[i][j]:
                    res += 1
                    self.dfs(j, i, grid, visited)
        return res

    def dfs(self, x: int, y: int, grid: List[List[str]], visited: List[List[bool]]):
        if x < 0 or y < 0 or x >= len(grid[0]) or y >= len(grid) or visited[y][x] or grid[y][x] == "0":
            return

        visited[y][x] = True  # IDEA: can overwrite the grid table (with # for e.g.) to indicate visited.

        self.dfs(x - 1, y, grid, visited)
        self.dfs(x + 1, y, grid, visited)
        self.dfs(x, y - 1, grid, visited)
        self.dfs(x, y + 1, grid, visited)


if __name__ == "__main__":
    sol = Solution()
    print(sol.numIslands(
        [
            ["1", "1", "1", "1", "0"],
            ["1", "1", "0", "1", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "0", "0", "0"]
        ]
    ))
    print(sol.numIslands(
        [
            ["1", "1", "0", "0", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "1", "0", "0"],
            ["0", "0", "0", "1", "1"]
        ]
    ))
