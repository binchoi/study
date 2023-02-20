from typing import List
import heapq


# Given an integer array nums and an integer k, return the kth largest element in the array.
# Note that it is the kth largest element in the sorted order, not the kth distinct element.
# You must solve it in O(n) time complexity.


class Solution:
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def findKthLargest(self, nums: List[int], k: int) -> int:
        for i in range(len(nums)):
            nums[i] *= -1  # heapq only provides minHeap

        heapq.heapify(nums)
        while k > 1:
            heapq.heappop(nums)
            k -= 1

        return -1 * heapq.heappop(nums)


if __name__ == "__main__":
    sol = Solution()
    print(sol.findKthLargest(nums=[3, 2, 1, 5, 6, 4], k=2))
    print(sol.findKthLargest(nums=[3, 2, 3, 1, 2, 4, 5, 5, 6], k=4))
