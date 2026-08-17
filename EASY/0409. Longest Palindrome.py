# 409. Longest Palindrome

# Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters.

# Letters are case sensitive, for example, "Aa" is not considered a palindrome.

 

# Example 1:

# Input: s = "abccccdd"
# Output: 7
# Explanation: One longest palindrome that can be built is "dccaccd", whose length is 7.
# Example 2:

# Input: s = "a"
# Output: 1
# Explanation: The longest palindrome that can be built is "a", whose length is 1.

from collections import Counter

class Solution(object):
    def longestPalindrome(self, s):
        count = Counter(s)

        len = 0
        has_odd = False

        for freq in count.values():
            len += (freq // 2) * 2

            if freq % 2 == 1:
                has_odd = True

        if has_odd:
            len += 1

        return len