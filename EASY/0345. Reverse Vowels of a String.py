# 345. Reverse Vowels of a String

# Given a string s, reverse only all the vowels in the string and return it.

# The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

 

# Example 1:

# Input: s = "IceCreAm"

# Output: "AceCreIm"

# Explanation:

# The vowels in s are ['I', 'e', 'e', 'A']. On reversing the vowels, s becomes "AceCreIm".

# Example 2:

# Input: s = "leetcode"

# Output: "leotcede"

class Solution(object):
    def reverseVowels(self, s):
        
        vowels = set('aeiouAEIOU')
        s = list(s)
        
        left = 0
        right =len(s) - 1
        
        while left < right:
            if s[left] not in vowels:
                left += 1
                continue
            
            if s[right] not in vowels:
                right -= 1
                continue
            
            s[left],s[right] = s[right], s[left]
            
            left += 1
            right -= 1
        
        return ''.join(s)