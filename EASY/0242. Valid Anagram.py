# 242. Valid Anagram

# revised 
# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

 

# Example 1:

# Input: s = "anagram", t = "nagaram"

# Output: true

# Example 2:

# Input: s = "rat", t = "car"

# Output: false


class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        for i in s:
            if i in t:
                t = t.replace(i, "", 1)
            else:
                return False
        return len(t) == 0

# s = "anagram"
# t = "nagaram"   

# for i in s:
#     if i in t:
#         t = t.replace(i, "", 1)
#     else:
#         print(False)
#         break
# else:
#     print(True)


# SOLUTION Approach 
# 1. Check if the lengths of the two strings are equal. If not, return False.
# 2. Create a dictionary to count the occurrences of each character in the first string.
# 3. Iterate through the second string and decrement the count for each character in the dictionary.
# 4. If any character count goes below zero or if a character is not found in the dictionary, return False.
# 5. If all character counts are zero after processing both strings, return True, indicating that the second string is an anagram of the first.


