# 238. Product of Array Except Self

# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

# You must write an algorithm that runs in O(n) time and without using the division operation.

 

# Example 1:

# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]

# Example 2:

# Input: nums = [-1,1,0,-3,3]
# Output: [0,0,9,0,0]
 
class Solution(object):
    def productExceptSelf(self, nums):
        
        n = len(nums)
        ans = [0] * n

        # Calculate the product of all elements to the left of each index
        
        left_prod = 1
        
        for i in range(n):
            ans[i] = left_prod
            left_prod *= nums[i]

        # Calculate the product of all elements to the right of each index
        
        right_prod = 1
        
        for i in range(n - 1, -1, -1):
            ans[i] *= right_prod
            right_prod *= nums[i]

        return ans