# 3024. Type of Triangle

# revised 
# You are given a 0-indexed integer array nums of size 3 which can form the sides of a triangle.

# A triangle is called equilateral if it has all sides of equal length.
# A triangle is called isosceles if it has exactly two sides of equal length.
# A triangle is called scalene if all its sides are of different lengths.
# Return a string representing the type of triangle that can be formed or "none" if it cannot form a triangle.

# Example 1:
"""
Input: nums = [3,3,3]
Output: "equilateral"
Explanation: Since all the sides are of equal length, therefore, it will form an equilateral triangle.
Example 2:

Input: nums = [3,4,5]
Output: "scalene"
Explanation: 
nums[0] + nums[1] = 3 + 4 = 7, which is greater than nums[2] = 5.
nums[0] + nums[2] = 3 + 5 = 8, which is greater than nums[1] = 4.
nums[1] + nums[2] = 4 + 5 = 9, which is greater than nums[0] = 3. 
Since the sum of the two sides is greater than the third side for all three cases, therefore, it can form a triangle.
As all the sides are of different lengths, it will form a scalene triangle.

 """
 
#  Solution

class Solution(object):
    def triangleType(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        a, b, c = sorted(nums)
        if a + b <= c:
            return "none"
        elif a == b == c:
            return "equilateral"
        elif a == b or b == c or a == c:
            return "isosceles"
        else:
            return "scalene"
        
sol = Solution()
print(sol.triangleType([3, 3, 3]))

# Algorithm:
# 1. Sort the input list `nums` to ensure that the sides are in non-decreasing order.
# 2. Assign the sorted sides to variables `a`, `b`, and `c`.
# 3. Check if the sum of the two smaller sides `a` and `b` is less than or equal to the largest side `c`. If this condition is true, it means that the sides cannot form a triangle, so return "none".
# 4. If all sides are equal (`a == b == c`), return "equilateral".
# 5. If exactly two sides are equal (i.e., `a == b` or `b == c` or `a == c`), return "isosceles".
# 6. If none of the above conditions are met, it means all sides are of different lengths, so return "scalene".
