# 238. Product of Array Except Self

#revised 

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
    
# Algorithm:
# 1. Initialize an array ans of the same length as nums to store the final results.
# 2. Use a variable left_prod to keep track of the product of all elements to the left of the current index. Initialize it to 1.
# 3. Iterate through the nums array from left to right:
#    a. For each index i, set ans[i] to left_prod (the product of all elements to the left of i).
#    b. Update left_prod by multiplying it with nums[i] to include the current element for the next iteration.
# 4. Use a variable right_prod to keep track of the product of all elements to the right of the current index. Initialize it to 1.
# 5. Iterate through the nums array from right to left:
#    a. For each index i, multiply ans[i] by right_prod (the product of all elements to the right of i).
#    b. Update right_prod by multiplying it with nums[i] to include the current element for the next iteration.
# 6. Return the ans array, which now contains the product of all elements except itself for each index.
