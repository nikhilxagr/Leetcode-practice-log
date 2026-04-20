# 3232. Find if Digit Game Can Be Won
# revised 
# You are given an array of positive integers nums.

# Alice and Bob are playing a game. In the game, Alice can choose either all single-digit numbers or all double-digit numbers from nums, and the rest of the numbers are given to Bob. Alice wins if the sum of her numbers is strictly greater than the sum of Bob's numbers.

# Return true if Alice can win this game, otherwise, return false.

# Example 1:

# Input: nums = [1,2,3,4,10]

# Output: false

# Explanation:

# Alice cannot win by choosing either single-digit or double-digit numbers.

# Example 2:

# Input: nums = [1,2,3,4,5,14]

# Output: true

# Explanation:

# Alice can win by choosing single-digit numbers which have a sum equal to 15.

# Example 3:

# Input: nums = [5,5,5,25]

# Output: true

# Explanation:

# Alice can win by choosing double-digit numbers which have a sum equal to 25.

from typing import List


class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        single_sum = 0
        double_sum = 0

        for num in nums:
            if num < 10:
                single_sum += num
                
            elif num < 100:
                double_sum += num

        total = single_sum + double_sum

        # Alice chooses single-digit numbers
        
        if single_sum > total - single_sum:
            return True

        # Alice chooses double-digit numbers
        
        if double_sum > total - double_sum:
            return True

        return False
    
# Algorithm:
# 1. Initialize two variables, single_sum and double_sum, to store the sum of single-digit and double-digit numbers, respectively.
# 2. Iterate through the nums array and update single_sum and double_sum based on whether the number is a single-digit or double-digit number.
# 3. Calculate the total sum of all numbers in the nums array.
# 4. Check if Alice can win by choosing single-digit numbers. If single_sum is greater than the sum of the remaining numbers (total - single_sum), return True.
# 5. Check if Alice can win by choosing double-digit numbers. If double_sum is greater than the sum of the remaining numbers (total - double_sum), return True.
# 6. If neither condition is satisfied, return False, indicating that Alice cannot win the game.
