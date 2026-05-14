# 45. Jump Game II

# revised 

# You are given a 0-indexed array of integers nums of length n. You are initially positioned at index 0.

# Each element nums[i] represents the maximum length of a forward jump from index i. In other words, if you are at index i, you can jump to any index (i + j) where:

# 0 <= j <= nums[i] and
# i + j < n
# Return the minimum number of jumps to reach index n - 1. The test cases are generated such that you can reach index n - 1.

 

# Example 1:

# Input: nums = [2,3,1,1,4]
# Output: 2
# Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.

# Example 2:

# Input: nums = [2,3,0,1,4]
# Output: 2

class Solution(object):
    def jump(self, nums):
      
        jumps = 0
        current_end = 0
        farthest = 0

        for i in range(len(nums) - 1):
            farthest = max(farthest, i + nums[i])

            if i == current_end:
                jumps += 1
                current_end = farthest

        return jumps
    
# Algorithm :
# 1. Keep track of the farthest index that can be reached with the current number of jumps.
# 2. When the current index reaches the end of the range for the current number of jumps, increment the jump count and update the range.
# Time complexity: O(n) where n is the length of the input array nums.
