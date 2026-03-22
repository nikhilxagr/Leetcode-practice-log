# 169. Majority Element
# revised

# Given an array nums of size n, return the majority element.

# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

# Example:

"""
Example 1:

Input: nums = [3,2,3]
Output: 3
Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2

"""

# class Solution(object):
#     def majorityElement(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         count = {}
#         for num in nums:
#             if num in count:
#                 count[num] += 1
#             else:
#                 count[num] = 1
#             if count[num] > len(nums) // 2:
#                 return num
            
            
#Another Approach  By Maximum Occurrence    
            
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = {}
        
        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
        return max(count, key=count.get)

# Algorithm:
# 1. We create a dictionary to count the occurrences of each element in the list.
# 2. We iterate through the list of numbers, updating the count for each number in the dictionary
# 3. Finally, we return the key with the maximum value in the dictionary, which is the majority element.
