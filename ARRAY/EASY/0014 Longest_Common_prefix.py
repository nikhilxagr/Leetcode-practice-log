# 14. Longest Common Prefix

# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

class Solution(object):
    def longestCommonPrefix(self, strs):
         """
        :type strs: List[str]
        :rtype: str
         """
         prefix = ""
         for i in range(len(strs[0])):
             
            char = strs[0][i]
            for s in strs[1:]:
                if i >= len(s) or s[i] != char:
                    return prefix
                
            prefix += char
         return prefix
 
           
           
# Solve by another approach
           
#   class Solution(object):
#     def longestCommonPrefix(self, strs):
#         """
#         :type strs: List[str]
#         :rtype: str
#         """
#         first = strs[0]
#         prefix = ""
#         print(first)
#         for i in range(0, len(first)):
#             for j in range(1, len(strs)):
#                 print("1. ", str(first[:i]))
#                 print("2. ", str(strs[j]))
#                 currPre = str(first[:(i + 1)])
#                 thisStr = str(strs[j])[:(i+1)]
#                 if currPre != thisStr:
#                     return prefix
#             prefix = prefix + first[i]
#         return prefix             