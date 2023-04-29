from collections import defaultdict
from typing import List


# Given an integer array of even length arr, return true if it is possible to reorder arr such that
# arr[2 * i + 1] = 2 * arr[2 * i] for every 0 <= i < len(arr) / 2, or false otherwise.

class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        arr.sort(key=lambda x: abs(x))
        d = defaultdict(int)

        for a in arr:
            # is there half of me?
            if a % 2 == 0 and d[a // 2] > 0:
                d[a / 2] -= 1
            else:
                # looking for twice me
                d[a] += 1
        return all([cnt == 0 for cnt in d.values()])


if __name__ == "__main__":
    sol = Solution()
    arr = [4, -2, 2, -4]
    print(sol.canReorderDoubled(arr))
