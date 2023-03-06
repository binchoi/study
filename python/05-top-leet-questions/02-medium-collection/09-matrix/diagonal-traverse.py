from typing import List
from collections import defaultdict

# Given an m x n matrix mat, return an array of all the elements of the array in a diagonal order


class Solution:
    UP = 0
    DOWN = 1

    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        curr = [0,0]
        state = self.UP
        res = []

        while curr[0] < len(mat) and curr[1] < len(mat[0]):
            res.append(mat[curr[0]][curr[1]])

            if state == self.UP:
                if curr[1] == len(mat[0])-1:
                    curr[0] += 1
                    state = self.DOWN
                elif curr[0] == 0:
                    curr[1] += 1
                    state = self.DOWN
                else:
                    curr[0] -= 1
                    curr[1] += 1
            else:
                if curr[0] == len(mat)-1:
                    curr[1] += 1
                    state = self.UP
                elif curr[1] == 0:
                    curr[0] += 1
                    state = self.UP
                else:
                    curr[0] += 1
                    curr[1] -= 1
        return res

    # simplified solution using the fact that "sum of indices on all diagonals are equal"
    def findDiagonalOrderSimplified(self, mat: List[List[int]]) -> List[int]:
        res = []

        d = defaultdict(list)
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                d[i + j].append(mat[i][j])

        for k, v in d.items():
            if k % 2 == 0:
                v.reverse()
            res += v

        return res


if __name__ == "__main__":
    sol = Solution()
    mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    mat_2 = [[1, 2], [3, 4]]

    print(sol.findDiagonalOrder(mat))
    print(sol.findDiagonalOrder(mat_2))
    print(sol.findDiagonalOrderSimplified(mat))
    print(sol.findDiagonalOrderSimplified(mat_2))
