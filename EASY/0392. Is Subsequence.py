# 392. Is Subsequence

# Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

# A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

 

# Example 1:

# Input: s = "abc", t = "ahbgdc"
# Output: true
# Example 2:

# Input: s = "axc", t = "ahbgdc"
# Output: false

class Solution(object):
    def isSubsequence(self, s, t):
        
        i, j = 0, 0

        while i < len(s) and j < len(t):
            
            if s[i] == t[j]:
                i += 1
            j += 1

        return i == len(s)
    
# Approach :
# 1. Use two pointers, one for each string.
# 2. Iterate through both strings, comparing characters.
# 3. If characters match, move the pointer for s forward.
# 4. Always move the pointer for t forward.
# 5. If the pointer for s reaches the end of s, it means all characters of s have been found in t in order, so return True. Otherwise, return False.