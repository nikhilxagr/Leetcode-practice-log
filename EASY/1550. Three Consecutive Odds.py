# 1550. Three Consecutive Odds
# revised 
# Given an integer array arr, return true if there are three consecutive odd numbers in the array. Otherwise, return false.

# Example 1:

# Input: arr = [2,6,4,1]
# Output: false
# Explanation: There are no three consecutive odds.
# Example 2:

# Input: arr = [1,2,34,3,4,5,7,23,12]
# Output: true
# Explanation: [5,7,23] are three consecutive odds.

# Solution:

class Solution(object):
    def threeConsecutiveOdds(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        
        Count = 0
        
        for num in arr:
            
            if num % 2 != 0:
                Count = Count + 1
                if Count == 3:
                    return True
            else:
                Count = 0
        return False

# Algorithm:
# 1. Initialize a variable Count to 0 to keep track of the number of consecutive odd numbers.
# 2. Iterate through each number in the input array arr.
# 3. For each number, check if it is odd (i.e., num % 2 != 0).
# 4. If the number is odd, increment the Count by 1. If Count reaches 3, return True, indicating that three consecutive odd numbers have been found.
# 5. If the number is even, reset the Count to 0, as the sequence of consecutive odd numbers is broken.
# 6. If the loop completes without finding three consecutive odd numbers, return False.