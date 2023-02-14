from typing import List


# Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and
# return an array of the non-overlapping intervals that cover all the intervals in the input.


class Solution:
    # Time Complexity: O(n)
    # Space Complexity: O(1) excluding output array
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        intervals.sort(key=lambda x: x[0])
        curr = intervals[0]
        for i in range(1, len(intervals)):
            if curr[1] >= intervals[i][0]:
                curr[1] = max(curr[1], intervals[i][1])
            else:
                res.append(curr)
                curr = intervals[i]
        res.append(curr)
        return res


if __name__ == "__main__":
    sol = Solution()
    print(sol.merge([[1, 3], [2, 6], [8, 10], [15, 18]]))
