# Q-136. Single Number

# revised
"""
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.

"""
# Examples:
"""
Example 1:

Input: nums = [2,2,1]

Output: 1

Example 2:

Input: nums = [4,1,2,1,2]

Output: 4

Example 3:

Input: nums = [1]

Output: 1

"""

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 0
        for num in nums:
            result ^= num
        return result
        
# ALgorithm:
# 1. Initialize a variable `result` to 0.
# 2. Iterate through each number `num` in the input list `nums`.
#     a. For each number, perform a bitwise XOR operation between `result` and `num`, and update `result` with the result of the XOR operation.
# 3. After iterating through all the numbers, `result` will hold the value of the single number that appears only once in the list.
# 4. Return the value of `result` as the output.  
