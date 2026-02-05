# 1550. Three Consecutive Odds

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