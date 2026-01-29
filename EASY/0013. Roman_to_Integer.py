# 13. Roman to Integer
# Easy
# Topics
# premium lock icon
# Companies
# Hint
# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000

# For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

# Examples

"""
Example 1:

Input: s = "III"
Output: 3
Explanation: III = 3.
Example 2:

Input: s = "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.
Example 3:

Input: s = "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
"""

class Solution(object):
    def romanToInt(self, s):
        
        roman_no = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        total = 0
        prev_val = 0
        
        for i in range(len(s)):
            current_val = roman_no[s[i]]
            
            if current_val > prev_val:
                total += current_val - 2 * prev_val
            
            else :
                total += current_val
                
            prev_val = current_val
            
        return total
    
sol = Solution()
print(sol.romanToInt("MCMXCIV"))
    
    
                     
                