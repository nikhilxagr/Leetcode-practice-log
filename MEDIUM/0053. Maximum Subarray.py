# 53. Maximum Subarray

# Revised 
# Given an integer array nums, find the subarray with the largest sum, and return its sum.

# Examples:
"""
Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.
Example 2:

Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum 1.
Example 3:

Input: nums = [5,4,-1,7,8]
Output: 23
Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.
"""

# Solution:

class Solution(object):
    def maxSubArray(self, nums):
        curr_sum = 0
        max_sum =nums[0]
        
        for i in range(len(nums)):
            curr_sum +=nums[i]

            if curr_sum > max_sum:
                max_sum = curr_sum
            if curr_sum<0:
                curr_sum = 0

        return max_sum   

# Algorithm:
# 1. Initialize two variables, curr_sum and max_sum, to keep track of the current sum of the subarray and the maximum sum found so far.
# 2. Iterate through each element in the input array nums.
# 3. For each element, add it to curr_sum.
# 4. If curr_sum is greater than max_sum, update max_sum to be equal to curr_sum.
# 5. If curr_sum becomes negative, reset it to 0, as a negative sum would not contribute to a maximum sum in future iterations.
# 6. After iterating through all elements, return max_sum as the result, which will be the largest sum of a contiguous subarray found in the input array.

