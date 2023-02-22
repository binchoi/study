
# Write an algorithm to determine if a number n is happy.

# A happy number is a number defined by the following process:

# Starting with any positive integer, replace the number by the sum of the squares of its digits.
# Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which
# does not include 1.
# Those numbers for which this process ends in 1 are happy.
# Return true if n is a happy number, and false if not.


class Solution:
    # Time Complexity: O(x) where x = max length of cycle
    # Space Complexity: O(x) where x = max length of cycle
    def isHappy(self, n: int) -> bool:
        seen = {n}
        curr = n
        while curr != 1:
            digits = []
            while curr > 0:
                curr, d = divmod(curr, 10)
                digits.append(d)
            curr = sum(d**2 for d in digits)
            if curr in seen:
                return False
            seen.add(curr)
        return True

# Digits Largest	    Next
# 1  	 9	            81
# 2	     99	            162
# 3	     999	        243
# 4	     9999	        324
# 13	 9999999999999	1053

# it will not go to infinity and keep growing (makes sense because digits are base 10 and the maximum for this numeric
# system is base 9.


if __name__ == "__main__":
    sol = Solution()
    print(sol.isHappy(19))
    print(sol.isHappy(9))
    print(sol.isHappy(2))
    print(sol.isHappy(233))
    print(sol.isHappy(999))

