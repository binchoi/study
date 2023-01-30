from typing import List

# Given an integer numRows, return the first numRows of Pascal's triangle.
# In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:


class Solution:
    # Time Complexity: O(n^2)
    # Space Complexity: O(n^2)
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]
        for i in range(1, numRows):
            res.append([a+b for a, b in zip([0]+res[-1], res[-1]+[0])])
        return res


if __name__ == "__main__":
    sol = Solution()
    print(sol.generate(10))
    print(sol.generate(5))

