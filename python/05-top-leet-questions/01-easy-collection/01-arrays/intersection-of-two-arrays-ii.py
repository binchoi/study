from collections import Counter
from typing import List, Dict


# Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must
# appear as many times as it shows in both arrays and you may return the result in any order.


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        shorter_nums, longer_nums = (nums1, nums2) if len(nums1) < len(nums2) else (nums2, nums1)
        res = []
        removed = set()
        for n in shorter_nums:
            for i, v in enumerate(longer_nums):  # Time Complexity: O(n*m)
                if v == n and i not in removed:
                    res.append(v)
                    removed.add(i)
                    break
        return res

    # Follow-up: What if the given array is already sorted? How would you optimize your algorithm?
    def intersectSortedArgs(self, nums1: List[int], nums2: List[int]) -> List[int]:
        shorter_nums, longer_nums = (nums1, nums2) if len(nums1) < len(nums2) else (nums2, nums1)
        res = []
        removed = set()
        for n in shorter_nums:
            for i, v in enumerate(longer_nums):
                if v > n:
                    break
                if v == n and i not in removed:
                    res.append(v)
                    removed.add(i)
                    break
        return res

    def intersect_hash(self, nums1: List[int], nums2: List[int]) -> List[int]:  # Time Complexity: O(n+m)
        res = []
        freq1 = self.get_frequency_map(nums1)  # O(n)
        freq2 = self.get_frequency_map(nums2)  # O(m)

        fst, snd = (freq1, freq2) if len(freq1) < len(freq2) else (freq2, freq1)  # O(1)
        for k, v in fst.items():  # O(max(n, m))
            if k in snd:
                res += [k] * min(snd.get(k), v)
        return res

    def get_frequency_map(self, nums: List[int]) -> Dict[int, int]:
        res = {}
        for n in nums:
            res[n] = res.get(n, 0) + 1
        return res

    def intersect_hash_optimized(self, nums1: List[int], nums2: List[int]) -> List[int]:  # Time Complexity: O(n+m)
        freq_nums1 = Counter(nums1)

        res = []
        for n in nums2:
            if freq_nums1.get(n, 0) > 0:
                freq_nums1[n] -= 1
                res.append(n)

        return res

    def intersect_two_pointer(self, nums1: List[int], nums2: List[int]) -> List[int]:  # O((n+m)(log nm))
        # sort -> O(n log n + m log m)
        nums1.sort()
        nums2.sort()

        res = []
        i, j = 0, 0
        while i < len(nums1) and j < len(nums2):  # O(n + m)
            if nums1[i] < nums2[j]:
                i += 1
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                res.append(nums1[i])
                i += 1
                j += 1
        return res


# What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into
# the memory at once?
    # make one counter (freq dict) and process num2 sequentially (by comparing to this counter)


if __name__ == "__main__":
    sol = Solution()
    nums = [-1, -100, 3, 99]
    nums2 = [-1, -1, 3, 99]
    print(sol.intersect_two_pointer(nums, nums2))

