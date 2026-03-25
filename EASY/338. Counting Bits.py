# 338. Counting Bits

# revised
# Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.

 

# Example 1:

# Input: n = 2
# Output: [0,1,1]
# Explanation:
# 0 --> 0
# 1 --> 1
# 2 --> 10
# Example 2:

# Input: n = 5
# Output: [0,1,1,2,1,2]
# Explanation:
# 0 --> 0
# 1 --> 1
# 2 --> 10
# 3 --> 11
# 4 --> 100
# 5 --> 101

# Algorithm:
# 1. Create an array ans of length n + 1 and initialize all elements to 0.
# 2. Iterate through the numbers from 1 to n (inclusive):
#    a. For each number i, calculate half as i // 2 and last_bit as i % 2.
#    b. Update ans[i] as the sum of ans[half] and last_bit
# 3. Return the ans array.

from ast import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0] * (n + 1)

        for i in range(1, n + 1):
            half = i // 2
            last_bit = i % 2

            ans[i] = ans[half] + last_bit

        return ans
    
# Another approach
# class Solution:
#     def countBits(self, n: int) -> List[int]:
#         ans = [0] * (n + 1)

#         for i in range(1, n + 1):
#             ans[i] = ans[i >> 1] + (i & 1)

#         return ans