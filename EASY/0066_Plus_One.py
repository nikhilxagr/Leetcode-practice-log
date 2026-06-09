# Q-66. Plus One

#REVISED 
"""
You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.

Example 1:

Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Incrementing by one gives 123 + 1 = 124.
Thus, the result should be [1,2,4].
Example 2:

Input: digits = [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
Incrementing by one gives 4321 + 1 = 4322.
Thus, the result should be [4,3,2,2].
Example 3:

Input: digits = [9]
Output: [1,0]
Explanation: The array represents the integer 9.
Incrementing by one gives 9 + 1 = 10.
Thus, the result should be [1,0].

"""



class Solution(object):
    def plusOne(self, digits):
        
        num = len(digits)
        
        for i in range(num-1, -1, -1): 
            
            if digits[i] < 9:  
                digits[i] = digits[i] + 1  
                
                return digits
            
            else:
             digits[i] = 0
        
        return [1] + digits
    
# ALGORITHM:

# 1. We start iterating from the end of the list of digits.
# 2. If the current digit is less than 9, we can simply increment it by 1 and return the modified list of digits.
# 3. If the current digit is 9, we set it to 0 and continue to the next digit to the left.
# 4. If we finish the loop and all digits were 9, we need to add a new digit '1' at the beginning of the list and return it, since the result would be 100...0 (with as many zeros as there were digits in the original list).