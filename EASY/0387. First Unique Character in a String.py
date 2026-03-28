#Problem:
# 387. First Unique Character in a String

# Revised 

# Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

"""
Example 1:

Input: s = "leetcode"

Output: 0

Explanation:

The character 'l' at index 0 is the first character that does not occur at any other index.

Example 2:

Input: s = "loveleetcode"

Output: 2

Example 3:

Input: s = "aabb"

Output: -1
"""

# Solution

# Algorithm Steps
# Create a frequency map (dictionary).
# Loop through the string and count each character.
# Loop through the string again:
# If a character’s count is 1, return its index.
# If no unique character is found, return -1.

# class Solution(object):
#     def firstUniqChar(self, s):
#         """
#         :type s: str
#         :rtype: int
#         """
       
#         freq = {}
#         for ch in s:
#             freq[ch] = freq.get(ch, 0) + 1

#         for i, ch in enumerate(s):
#             if freq[ch] == 1:
#                 return i

#         return -1
    
# solve = Solution()
# print(solve.firstUniqChar("leetcode"))
# print(solve.firstUniqChar("loveleetcode"))
# print(solve.firstUniqChar("aabb"))

# Another Easy Approach

class Solution(object):
    def firstUniqChar(self, s):
       
        for i in range(len(s)):
            
            if s.index(s[i]) == s.rindex(s[i]):
                
                return i
        return -1
    
# Algorithm 
# Loop through the string:
# For each character, check if its first occurrence index is the same as its last occurrence index.
# If they are the same, it means the character is unique, and we return its index.
# If we finish the loop without finding a unique character, we return -1.