from typing import List

# 6361. Minimum Score by Changing Two Elements

class Solution:
    def minimizeSumNaive(self, nums: List[int]) -> int:
        if len(nums) < 4:
            return 0

        nums.sort()
        print(nums)
        div, mod = divmod(len(nums) - 1, 2)
        med = nums[div]

        diff_arr = [abs(v - med) for v in nums]
        print(diff_arr)
        top_two_diff = [-1, -1]
        switch_idx = [-1, -1]
        for i in range(len(diff_arr)):
            print(">", top_two_diff)
            if diff_arr[i] > top_two_diff[0]:
                top_two_diff[1], switch_idx[1] = top_two_diff[0], switch_idx[0]
                print(">>", top_two_diff)
                top_two_diff[0], switch_idx[0] = diff_arr[i], i
                print(">>", top_two_diff)
            elif diff_arr[i] > top_two_diff[1]:
                top_two_diff[1], switch_idx[1] = diff_arr[i], i
        for i in switch_idx:
            diff_arr[i] = 0
            nums[i] = med
        print(diff_arr)

        print(nums)
        return max(nums) - min(nums)

    def minimizeSum(self, nums: List[int]) -> int:
        if len(nums) < 4:
            return 0
        nums.sort()
        case_one = nums[len(nums)-1] - nums[2]
        case_two = nums[len(nums)-2] - nums[1]
        case_thr = nums[len(nums)-3] - nums[0]
        return min(case_one, case_two, case_thr)



if __name__ == "__main__":
    sol = Solution()
    # print(sol.minimizeSum([1,4,3]))
    # print(sol.minimizeSum([1,4,7,8,5]))
    # print(sol.minimizeSum([31,25,72,79,74,65]))
    print(sol.minimizeSumNaive([65,77,1,73,32,43]))
    print(sol.minimizeSum([65,77,1,73,32,43]))
