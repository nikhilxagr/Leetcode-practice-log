# 14. Longest Common Prefix
# Revised
# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        prefix = ""
        first = strs[0]

        for i in range(len(first)):
            char = first[i]

            for s in strs:
                if i >= len(s) or s[i] != char:
                    return prefix

            prefix += char

        return prefix