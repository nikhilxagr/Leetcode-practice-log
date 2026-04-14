# 2652. Sum Multiples
# revised 
# Given a positive integer n, find the sum of all integers in the range [1, n] inclusive that are divisible by 3, 5, or 7.

# Return an integer denoting the sum of all numbers in the given range satisfying the constraint.

# Examples:

"""
Example 1:

Input: n = 7
Output: 21
Explanation: Numbers in the range [1, 7] that are divisible by 3, 5, or 7 are 3, 5, 6, 7. The sum of these numbers is 21.
Example 2:

Input: n = 10
Output: 40
Explanation: Numbers in the range [1, 10] that are divisible by 3, 5, or 7 are 3, 5, 6, 7, 9, 10. The sum of these numbers is 40.
Example 3:

Input: n = 9
Output: 30
Explanation: Numbers in the range [1, 9] that are divisible by 3, 5, or 7 are 3, 5, 6, 7, 9. The sum of these numbers is 30.
"""
# Solution:

class Solution(object):
    def sumOfMultiples(self, n):
        
        total_sum = 0
        
        for i in range(1, n + 1):
            if i % 3 == 0 or i % 5 == 0 or i % 7 == 0:
                
                total_sum += i
        return total_sum
        
sol = Solution()
print(sol.sumOfMultiples(7))


# Algorithm:
# 1. Initialize a variable `total_sum` to 0 to keep track of the sum of multiples.
# 2. Iterate through all integers from 1 to n (inclusive). 
# 3. For each integer i, check if it is divisible by 3, 5, or 7 using the modulus operator (%).
# 4. If i is divisible by any of these numbers, add it to `total_sum`.
# 5. After the loop, return the value of `total_sum` as the result.