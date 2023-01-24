from collections import deque
from typing import List


# Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

class Solution:
    def simple_rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        first_k = nums[-k:]
        last_n_minus_k = nums[:len(nums) - k]

        nums[:k] = first_k
        nums[k:] = last_n_minus_k

    def buffer_rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        if k == 0:
            return
        n = len(nums)
        buffer = deque()

        for i in range(n):
            if i < k:
                buffer.append(nums[i])
                nums[i] = nums[n - k + i]
            else:
                buffer.append(nums[i])
                nums[i] = buffer.popleft()

    def rotate(self, nums: List[int], k: int) -> None:
        k = k % len(nums)
        if k == 0:
            return

        self.reverse_slice(nums, 0, len(nums) - 1)
        self.reverse_slice(nums, 0, k - 1)
        self.reverse_slice(nums, k, len(nums) - 1)

    def reverse_slice(self, nums: List[int], start: int, end: int):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1


if __name__ == "__main__":
    sol = Solution()
    nums = [-1, -100, 3, 99]
    print(nums)
    sol.rotate(nums, 2)
    print(nums)
