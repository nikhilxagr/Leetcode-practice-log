# 34. Find First and Last Position of Element in Sorted Array

# Revised
# Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

# If target is not found in the array, return [-1, -1].

# You must write an algorithm with O(log n) runtime complexity.

 

# Example 1:

# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]
# Example 2:

# Input: nums = [5,7,7,8,8,10], target = 6
# Output: [-1,-1]
# Example 3:

# Input: nums = [], target = 0
# Output: [-1,-1]

class Solution(object):
    def searchRange(self, nums, target):
       
        ans = [-1, -1]
        
        for i in range(len(nums)):
            
            if nums[i] == target:
                ans[0]  = i
                break
            
        for i in range(len(nums)-1, -1, -1): 
            
            if nums[i] == target:
                ans[1] = i
                break
            
        return ans



# nums = [5,7,7,8,8,10]
# target  = 8

# ans  = [-1, -1]

# for i in range(len(nums)):
#     if nums[i] == target:
#         ans[0]  = i
#         break
        
# for i in range(len(nums)-1, -1, -1): 
#     if nums[i] == target:
#         ans[1] = i
#         break
# print(ans)

# Algorithm:
# 1. Initialize an answer list with [-1, -1] to store the starting and ending positions of the target.
# 2. Iterate through the nums array from the beginning to find the first occurrence of the target:
#    a. If the current element is equal to the target, update ans[0] with the current index and break the loop.
# 3. Iterate through the nums array from the end to find the last occurrence of the
#    a. If the current element is equal to the target, update ans[1] with the current index and break the loop.
# 4. Return the ans list, which contains the starting and ending positions of the target. If the target is not found, ans will remain [-1, -1].