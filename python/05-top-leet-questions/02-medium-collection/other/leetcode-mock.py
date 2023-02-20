from collections import Counter
from typing import List, Dict


class Solution:
    def largestTimeFromDigits(self, arr: List[int]) -> str:
        choices = Counter(arr)
        try:
            fst_h = self.select_max_under_n(choices, 2)
            return f"{fst_h}{self.select_max_under_n(choices, 3, fst_h)}:{self.select_max_under_n(choices, 5)}{self.select_max_under_n(choices, 9)}"
        except Exception as e:
            return ""

    def select_max_under_n(self, choices: Dict[int, int], n: int, fst_h: int = -1) -> int:
        print(fst_h)
        max_val = 9 if -1 < fst_h < 2 else n
        for i in range(max_val, -1, -1):
            print(f"> n= {n}; max= {max_val} {choices}")
            if i in choices and choices[i] > 0:
                print(f"found {i}")
                choices[i] -= 1
                return i
        raise Exception("No valid choice")


class Solution:
    def largestTimeFromDigits(self, arr: List[int]) -> str:
        choices = Counter(arr)
        res = [""]
        self.largestTimeFromDigitsBacktrack("", choices, res)
        return res[0]

    def largestTimeFromDigitsBacktrack(self, so_far: str, choices: Dict[int, int], res: List[str]):
        stage = len(so_far)  # 0, 1, 2 (:), 3, 4
        if stage == 0:
            for i in range(2, -1, -1):
                if i in choices and choices[i] > 0:
                    choices[i] -= 1
                    self.largestTimeFromDigitsBacktrack(f"{i}", choices, res)
                    choices[i] += 1
        elif stage == 1:
            max_val = 9 if so_far[0] < "2" else 3
            for i in range(max_val, -1, -1):
                if i in choices and choices[i] > 0:
                    choices[i] -= 1
                    self.largestTimeFromDigitsBacktrack(f"{so_far}{i}", choices, res)
                    choices[i] += 1
        elif stage == 2:
            self.largestTimeFromDigitsBacktrack(f"{so_far}:", choices, res)
        elif stage == 3:
            for i in range(5, -1, -1):
                if i in choices and choices[i] > 0:
                    choices[i] -= 1
                    self.largestTimeFromDigitsBacktrack(f"{so_far}{i}", choices, res)
                    choices[i] += 1
        elif stage == 4:
            for i in range(9, -1, -1):
                if i in choices and choices[i] > 0:
                    choices[i] -= 1
                    self.largestTimeFromDigitsBacktrack(f"{so_far}{i}", choices, res)
                    choices[i] += 1
        else:
            res[0] = max(res[0], so_far)
            return


class NumArray:

    def __init__(self, nums: List[int]):
        self.arr = nums
        self.calibrate = {}
        self.cum_sum = [0]
        for n in nums:
            self.cum_sum.append(self.cum_sum[-1] + n)

    def update(self, index: int, val: int) -> None:
        diff_to_add = val - self.arr[index]
        self.arr[index] = val
        self.calibrate[index] = diff_to_add if index not in self.calibrate else self.calibrate[index] + diff_to_add

    def sumRange(self, left: int, right: int) -> int:
        res = self.cum_sum[right + 1] - self.cum_sum[left]
        for k in self.calibrate:
            if left <= k <= right:
                res += self.calibrate[k]
        return res



if __name__ == "__main__":
    sol = Solution()
    # print(sol.largestTimeFromDigits([0,4,0,0]))
    print(sol.largestTimeFromDigits([2,0,6,6]))
