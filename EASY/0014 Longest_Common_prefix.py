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
    
    
# Algorithm:
# 1. Initialize an empty string `prefix` to store the longest common prefix.
# 2. Take the first string from the array as a reference (let's call it `first`).
# 3. Iterate through each character of the `first` string using its index `i`.
# 4. For each character, check if it matches the corresponding character in all other strings in the array.
# 5. If any string does not have the character at index `i` or if the character does not match, return the current `prefix` as the longest common prefix.
# 6. If all strings have the same character at index `i`, append that character to the `prefix`.
