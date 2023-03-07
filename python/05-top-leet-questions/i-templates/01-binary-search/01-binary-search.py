from typing import List

# lo represents the lowest possible idx output
# hi represents the highest possible idx output


# Find index of target in a sorted array
# left-most idx & where it should be (even if non-existent)
def binary_search(nums: List[int], target: int) -> int:
    lo, hi = 0, len(nums)  # hi = len(nums) such that res==len(nums) if target>max(nums)
    while lo < hi:
        mid = (lo + hi) // 2
        print(f"{lo=}, {hi=}, {mid=}")
        if nums[mid] < target:
            lo = mid + 1
        else:
            hi = mid
    return lo


# return -1 if not exists
def binary_search_equality(nums: List[int], target: int) -> int:
    lo, hi = 0, len(nums)-1
    while lo <= hi:
        mid = (lo + hi) // 2
        print(f"{lo=}, {hi=}, {mid=}")
        if nums[mid] < target:
            lo = mid + 1
        elif nums[mid] > target:
            hi = mid - 1
        else:
            return mid
    return -1


# right-most idx & where it should be (even if non-existent)
def binary_search_rightmost(nums: List[int], target: int) -> int:
    lo, hi = 0, len(nums)
    while lo < hi:
        mid = (lo + hi) // 2
        print(f"{lo=}, {hi=}, {mid=}")
        if nums[mid] > target:
            hi = mid
        else:
            lo = mid + 1
    return hi - 1 if nums[hi-1] == target else hi


if __name__ == "__main__":
    nums = [1, 3, 4, 5, 3, 3, 2, 65, 6, 3, 3, 4, 5, 2653, 4]
    nums.sort()
    print(nums)
    print(f"{binary_search(nums, 65)=}")
    print(f"{binary_search(nums, 2653)=}")
    print(f"{binary_search(nums, -1)=}")
    print(f"{binary_search(nums, 3000)=}")

    print(f"{binary_search_equality(nums, 65)=}")
    print(f"{binary_search_equality(nums, 2653)=}")
    print(f"{binary_search_equality(nums, -1)=}")
    print(f"{binary_search_equality(nums, 3000)=}")

    print(f"{binary_search_rightmost(nums, 65)=}")
    print(f"{binary_search_rightmost(nums, 2653)=}")
    print(f"{binary_search_rightmost(nums, -1)=}")
    print(f"{binary_search_rightmost(nums, 3000)=}")

