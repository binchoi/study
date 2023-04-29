from typing import List


# Given an array of integers nums and an integer k. A continuous subarray is called nice if
# there are k odd numbers on it.
# Return the number of nice sub-arrays.

class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        odd_indices = self.get_odd_idx(nums)
        if len(odd_indices) < k:
            return 0

        res = 0
        for l_idx in range(len(odd_indices)-k+1):
            left, right = odd_indices[l_idx], odd_indices[l_idx+k-1]
            lo = odd_indices[l_idx-1]+1 if l_idx>0 else 0
            hi = odd_indices[l_idx+k]-1 if l_idx+k<len(odd_indices) else len(nums)-1
            res += ((left-lo+1)*(hi-right+1))
        return res

    def get_odd_idx(self, nums: List[int]) -> List[int]:
        return [i for i in range(len(nums)) if nums[i]%2==1]


if __name__ == "__main__":
    sol = Solution()
    nums = [1, 1, 2, 1, 1]
    k = 3
    print(sol.numberOfSubarrays(nums, k))

    nums2 = [2, 2, 2, 1, 2, 2, 1, 2, 2, 2]
    k2 = 2
    print(sol.numberOfSubarrays(nums2, k2))

