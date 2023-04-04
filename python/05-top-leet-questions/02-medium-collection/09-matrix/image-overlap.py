from collections import Counter
from typing import List, Tuple, Dict, Set


# You are given two images, img1 and img2, represented as binary, square matrices of size n x n. A binary matrix
# has only 0s and 1s as values.

# We translate one image however we choose by sliding all the 1 bits left, right, up, and/or down any number of units.
# We then place it on top of the other image. We can then calculate the overlap by counting the number of positions
# that have a 1 in both images.

# Note also that a translation does not include any kind of rotation. Any 1 bits that are translated outside of the
# matrix borders are erased.
# Return the largest possible overlap.


class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        res = 0

        s1, s2 = self.get_coord_set(img1), self.get_coord_set(img2)
        if len(s1) == 0 or len(s2) == 0:
            return res

        memo = {}
        for c1 in s1:
            for c2 in s2:
                diff = (c2[0] - c1[0], c2[1] - c1[1])
                res = max(res, self.overlap_if_translated(s1, s2, diff, memo))
        return res

    def overlap_if_translated(self, s1: Set[Tuple[int]], s2: Set[Tuple[int]], diff: Tuple[int],
                              memo: Dict[Tuple[int], int]) -> int:
        if diff in memo:
            return memo[diff]

        res = 0
        for c in s1:
            if (diff[0] + c[0], diff[1] + c[1]) in s2:
                res += 1
        memo[diff] = res
        return res

    def get_coord_set(self, img: List[List[int]]) -> Set[Tuple[int]]:
        res = set()
        for i in range(len(img)):
            for j in range(len(img[0])):
                if img[i][j] == 1:
                    res.add((i, j))
        return res

    # Counter of the translation constant/shift will result in diff->overlaps
    def largestOverlapOptimized(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        l1, l2 = self.get_coords(img1), self.get_coords(img2)
        counter = Counter([(i[0]-j[0], i[1]-j[1]) for i in l1 for j in l2])
        return max(counter.values() or [0])

    def get_coords(self, img: List[List[int]]) -> List[Tuple[int, int]]:
        res = []
        for i in range(len(img)):
            for j in range(len(img[0])):
                if img[i][j] == 1:
                    res.append((i, j))
        return res


if __name__ == "__main__":
    sol = Solution()
    img1 = [[1, 1, 0], [0, 1, 0], [0, 1, 0]]
    img2 = [[0, 0, 0], [0, 1, 1], [0, 0, 1]]

    print(sol.largestOverlapOptimized(img1, img2))

