# 217. Contains Duplicate

# Revised 
# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

# Example

"""
Example 1:

Input: nums = [1,2,3,1]

Output: true

Explanation:

The element 1 occurs at the indices 0 and 3.

Example 2:

Input: nums = [1,2,3,4]

Output: false

Explanation:

All elements are distinct.

Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]

Output: true
"""

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        seen = set()

        for num in nums:
            if num in seen:
                return True
            seen.add(num)

        return False
    
# Algorithm:
# 1. Initialize an empty set called `seen` to keep track of the unique numbers encountered in the array.
# 2. Iterate through each number `num` in the input array `nums`.
#     a. For each number, check if it is already present in the `seen` set.
#     b. If it is present, this means we have encountered a duplicate, so return `True`.
#     c. If it is not present, add the number to the `seen` set.
# 3. If the loop completes without finding any duplicates, return `False`, indicating that all elements are distinct.