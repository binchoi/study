from collections import defaultdict
from typing import List

# Given an m x n matrix, return true if the matrix is Toeplitz. Otherwise, return false.
# A matrix is Toeplitz if every diagonal from top-left to bottom-right has the same elements.


class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        d = defaultdict(set)
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                k = j-i
                d[k].add(matrix[i][j])
                if len(d[k]) > 1:
                    return False
        return True

    # space optimized
    def isToeplitzMatrixOptimized(self, matrix: List[List[int]]) -> bool:
        for i in range(len(matrix)-1):
            for j in range(len(matrix[0])-1):
                if matrix[i][j] != matrix[i+1][j+1]:
                    return False
        return True


if __name__ == "__main__":
    sol = Solution()
    matrix = [[1, 2, 3, 4], [5, 1, 2, 3], [9, 5, 1, 2]]

    print(matrix, sol.isToeplitzMatrix(matrix))
    print(matrix, sol.isToeplitzMatrixOptimized(matrix))
