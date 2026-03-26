# 344. Reverse String

# revised 
# Write a function that reverses a string. The input string is given as an array of characters s.

# You must do this by modifying the input array in-place with O(1) extra memory.
"""
Example 1:

Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
Example 2:

Input: s = ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]

"""

# Solution:

class Solution(object):
    def reverseString(self, s):
        
        # s.reverse()
        i = 0
        j = len(s) -1

        while i<j:
            temp = s[i]
            s[i] = s[j]
            s[j] = temp

            i += 1
            j -= 1

# Algprithm:
# 1. We can use the built-in reverse() method to reverse the list in-place.
# 2. Alternatively, we can use two pointers, one starting at the beginning of the   
#    list and the other starting at the end. We can swap the elements at these two pointers and then move the pointers towards each other until they meet.