# 1. Two Sum

# You are given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

 

# Example 1:

# Input: nums = [2,7,11,15], target = 9

# Output: [0,1]

# Explanation:

# The sum of nums[0] and nums[1] is 2 + 7 = 9, which equals the target. Therefore, the indices [0, 1] are returned.

# Example 2:

# Input: nums = [3,2,4], target = 6

# Output: [1,2]

# Explanation:

# The sum of nums[1] and nums[2] is 2 + 4 = 6, which equals the target. Therefore, the indices [1, 2] are returned.

# Example 3:

# Input: nums = [3,3], target = 6

# Output: [0,1]

# Explanation:

# The sum of nums[0] and nums[1] is 3 + 3 = 6, which equals the target. Therefore, the indices [0, 1] are returned.

class Solution(object):
    def twoSum(self, nums, target):
        map = {}
        
        for i in range(len(nums)):
            complement = target - nums[i]
            
            if complement in map:
                return [map[complement], i]
            map[nums[i]] = i
        
        return []