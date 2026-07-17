# 209. Minimum Size Subarray Sum

# Given an array of positive integers nums and a positive integer target, return the minimal length of a subarray whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.

 

# Example 1:

# Input: target = 7, nums = [2,3,1,2,4,3]
# Output: 2
# Explanation: The subarray [4,3] has the minimal length under the problem constraint.
# Example 2:

# Input: target = 4, nums = [1,4,4]
# Output: 1
# Example 3:

# Input: target = 11, nums = [1,1,1,1,1,1,1,1]
# Output: 0

class Solution(object):
    def minSubArrayLen(self, target, nums):
        
        n = len(nums)
        left = 0
        total = 0
        min_length = float('inf')

        for right in range(n):
            total += nums[right]

            while total >= target:
                
                min_length = min(min_length, right - left + 1)
                total -= nums[left]
                left += 1

        return min_length if min_length != float('inf') else 0
    
# idea :
# 1. Use two pointers to create a sliding window.
# 2. Expand the window by moving the right pointer and adding the current element to the total sum.
# 3. When the total sum is greater than or equal to the target, update the minimum length and shrink the window by moving the left pointer and subtracting the leftmost element from the total sum.
 