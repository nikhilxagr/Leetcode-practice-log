# 3. Longest Substring Without Repeating Characters

# Given a string s, find the length of the longest substring without duplicate characters.

 

# Example 1:

# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3. Note that "bca" and "cab" are also correct answers.
# Example 2:

# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Example 3:

# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        
        char_Set = set()
        left = 0
        max_length = 0
        
        for right in range(len(s)):
            
            while s[right] in char_Set:
                char_Set.remove(s[left])
                left += 1
                
            char_Set.add(s[right])
            
            max_length = max(max_length, right - left + 1)
        
        return max_length

# Approach - we can use a sliding window technique to solve this problem. We maintain a set to keep track of the characters in the current window. We use two pointers, `left` and `right`, to represent the current window of characters.