# 283. Move  Zeroes

# Given an integer array nums,  all 0's to the end of it while maintaining the relative order of the non-zero elements.

# Note that you must do this in-place without making a copy of the array.

# Example

"""
Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
Example 2:

Input: nums = [0]
Output: [0]

"""

# class Solution(object):
#     def Zeroes(self, nums):
#         index = 0
        
#         for num in nums:
#             if num != 0:
#                 nums[index] = num
#                 index += 1
        
#         while index < len(nums):
#             nums[index] = 0
#             index += 1
            
                  
class Solution(object):
    def moveZeroes(self, nums):
        arr1 =[]
        arr2 = []
        
        for num in nums:

            if num != 0:
                arr1.append(num)
            else :
                arr2.append(num)
        nums[:]= arr1 + arr2
        return nums            
                                        
                  