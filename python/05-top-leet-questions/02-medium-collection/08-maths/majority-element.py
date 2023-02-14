from typing import List, Tuple


# Given an array nums of size n, return the majority element.

# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element
# always exists in the array.

# Follow-up: Could you solve the problem in linear time and in O(1) space?


class Solution:
    # Idea: consider the majority element to represent +1 and everything else to represent -1
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def majorityElement(self, nums: List[int]) -> int:
        cand, count = None, 0
        for n in nums:
            if count == 0:
                cand, count = n, 1
            elif cand == n:
                count += 1
            else:
                count -= 1
        return cand


if __name__ == "__main__":
    sol = Solution()
    print(sol.majorityElement([2, 2, 1, 1, 1, 2, 2]))
    print(sol.majorityElement([2, 2, 4, 4, 4]))
