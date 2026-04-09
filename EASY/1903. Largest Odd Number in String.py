# 1903. Largest Odd Number in String

# revised 

# You are given a string num, representing a large integer. Return the largest-valued odd integer (as a string) that is a non-empty substring of num, or an empty string "" if no odd integer exists.

# A substring is a contiguous sequence of characters within a string.

 

# Example 1:

# Input: num = "52"
# Output: "5"
# Explanation: The only non-empty substrings are "5", "2", and "52". "5" is the only odd number.
# Example 2:

# Input: num = "4206"
# Output: ""
# Explanation: There are no odd numbers in "4206".
# Example 3:

# Input: num = "35427"
# Output: "35427"
# Explanation: "35427" is already an odd number.

class Solution(object):
    def largestOddNumber(self, num):
        """
        :type num: str
        :rtype: str
        """
        for i in range(len(num)-1, -1, -1):
            
            if int(num[i]) % 2 == 1:
                
                return num[:i+1]
            
        return ""
    
# Algorithm:
# 1. We will iterate through the string num from the end to the beginning.
# 2. For each character, we will check if it is an odd digit (i.e., if the integer value of the character modulo 2 is equal to 1).   
# 3. If we find an odd digit, we will return the substring of num from the beginning to the current index (inclusive).
# 4. If we finish iterating through the string without finding any odd digit, we will return an empty string "".
