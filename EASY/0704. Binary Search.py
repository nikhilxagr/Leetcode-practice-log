# 704. Binary Search

# Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

# You must write an algorithm with O(log n) runtime complexity.

 

# Example 1:

# Input: nums = [-1,0,3,5,9,12], target = 9
# Output: 4
# Explanation: 9 exists in nums and its index is 4
# Example 2:

# Input: nums = [-1,0,3,5,9,12], target = 2
# Output: -1
# Explanation: 2 does not exist in nums so return -1

# Solution:

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        ans = -1

        for i in range(len(nums)):
            if nums[i] == target:
                ans = i
                break 
        return ans
    
    
# Solve and debug:    
    
# nums = [-1,0,3,5,9,12]
# target = 9

# ans = -1

# for i in range(len(nums)):
#     if nums[i] == target:
#         print(i)
#         break        
# else:
#     print(ans)