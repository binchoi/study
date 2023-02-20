from typing import List


# 6361. Minimum Score by Changing Two Elements


class Solution:
    def minImpossibleOR(self, nums: List[int]) -> int:
        curr = 1
        while True:
            sub_list = [n for n in nums if n | curr == curr]
            cand = 0
            for n in sub_list:
                cand |= n
            if curr != cand:
                return curr
            curr += 1


    def minImpossibleORSimplified(self, nums: List[int]) -> int:
        curr = 1
        while curr in nums:
            curr *= 2
        return curr


if __name__ == "__main__":
    sol = Solution()
    print(sol.minImpossibleOR([2, 1]))
    print(sol.minImpossibleORSimplified([2, 1]))
    print(sol.minImpossibleOR([5, 3, 2]))
    print(sol.minImpossibleORSimplified([5, 3, 2]))
    print(sol.minImpossibleORSimplified(
        [8388608, 131072, 128, 2097152, 65536, 2048, 438, 1048576, 8192, 32, 8, 64, 1024, 2244, 512, 262144, 4096,
         16384, 4, 256, 2, 4194304, 2203, 16, 32768, 410, 524288, 765, 1]))
    print(sol.minImpossibleOR(
        [8388608, 131072, 128, 2097152, 65536, 2048, 438, 1048576, 8192, 32, 8, 64, 1024, 2244, 512, 262144, 4096,
         16384, 4, 256, 2, 4194304, 2203, 16, 32768, 410, 524288, 765, 1]))
