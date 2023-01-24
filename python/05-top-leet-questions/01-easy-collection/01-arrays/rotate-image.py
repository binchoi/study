from typing import List


# You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

# You have to rotate the image in-place, which means you have to modify the input 2D matrix directly.
# DO NOT allocate another 2D matrix and do the rotation.


class Solution:
    # Time Complexity: O(m*n)
    # Space Complexity: O(1)
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # 1. transpose [swap (x,y)->(y,x)]
        for i in range(len(matrix)):
            for j in range(i + 1, len(matrix[i])):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # 2. reflection on left y-axis
        for i in range(len(matrix)):
            for j in range(len(matrix[i]) // 2):
                matrix[i][j], matrix[i][len(matrix[i]) - 1 - j] = matrix[i][len(matrix[i]) - 1 - j], matrix[i][j]


if __name__ == "__main__":
    sol = Solution()
    matrix = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
    print(matrix)
    sol.rotate(matrix)
    print(matrix)
