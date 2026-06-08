# 58. Length of Last Word
#revised
# Given a string s consisting of words and spaces, return the length of the last word in the string.

# A word is a maximal substring consisting of non-space characters only.


# Example

"""
Example 1:

Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.
Example 2:

Input: s = "   fly me   to   the moon  "
Output: 4
Explanation: The last word is "moon" with length 4.
Example 3:

Input: s = "luffy is still joyboy"
Output: 6
Explanation: The last word is "joyboy" with length 6.
"""

class Solution(object):
    def lengthOfLastWord(self, s):
        words = s.split()   
        
        last_word = words[-1]      
        length = len(last_word)    
        
        return length     
  
    
# ALgorithm:
# 1. Split the input string s into a list of words using the split() method, which automatically handles multiple spaces.
# 2. Access the last word in the list using words[-1].
# 3. Calculate the length of the last word using the len() function.
# 4. Return the length of the last word as the final result.