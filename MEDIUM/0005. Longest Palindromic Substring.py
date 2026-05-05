# 5. Longest Palindromic Substring

# Given a string s, return the longest palindromic substring in s.

 

# Example 1:

# Input: s = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer.
# Example 2:

# Input: s = "cbbd"
# Output: "bb"

class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""

        for i in range(len(s)):
            for j in range(i, len(s)):
                sub = s[i:j+1]

                # check palindrome
                if sub == sub[::-1]:
                    if len(sub) > len(res):
                        res = sub

        return res