# 242. Valid Anagram

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


