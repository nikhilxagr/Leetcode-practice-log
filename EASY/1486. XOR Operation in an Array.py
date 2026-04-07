# 1486. XOR Operation in an Array

# revised

# You are given an integer n and an integer start.

# Define an array nums where nums[i] = start + 2 * i (0-indexed) and n == nums.length.

# Return the bitwise XOR of all elements of nums.



# Examples:
"""
Example 1:

Input: n = 5, start = 0
Output: 8
Explanation: Array nums is equal to [0, 2, 4, 6, 8] where (0 ^ 2 ^ 4 ^ 6 ^ 8) = 8.
Where "^" corresponds to bitwise XOR operator.
Example 2:

Input: n = 4, start = 3
Output: 8
Explanation: Array nums is equal to [3, 5, 7, 9] where (3 ^ 5 ^ 7 ^ 9) = 8.
"""

# Solution:

class Solution(object):
    def xorOperation(self, n, start):
        ans = 0
        for i in range(n):
            ans ^= start + 2 * i
        return ans
    
# Algorithm:
# 1. Initialize a variable ans to 0 to store the cumulative XOR result.
# 2. Iterate through the range of n (from 0 to n-1).
# 3. For each index i, calculate the value of nums[i] as start + 2 * i and perform a bitwise XOR operation with ans.
# 4. After the loop, return the final value of ans, which is the XOR
#    of all elements in the array nums.