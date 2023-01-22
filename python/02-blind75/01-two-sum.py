from typing import List

# https://leetcode.com/problems/two-sum/


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i, v in enumerate(nums):
            if v in hashmap.keys():
                return [hashmap[v], i]
            hashmap[target-v] = i
        return [-1, -1]


# Test
if __name__ == '__main__':
    mySol = Solution()

    assert mySol.twoSum([2, 7, 11, 15], 9) == [0, 1]
    assert mySol.twoSum([3, 2, 4], 6) == [1, 2]
    assert mySol.twoSum([3, 3], 6) == [0, 1]
    assert mySol.twoSum([-1, 100, -50], 50) == [1, 2]

