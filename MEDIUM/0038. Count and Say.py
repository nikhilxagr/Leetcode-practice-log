# 38. Count and Say

#revised 
# The count-and-say sequence is a sequence of digit strings defined by the recursive formula:

# countAndSay(1) = "1"
# countAndSay(n) is the run-length encoding of countAndSay(n - 1).
# Run-length encoding (RLE) is a string compression method that works by replacing consecutive identical characters (repeated 2 or more times) with the concatenation of the character and the number marking the count of the characters (length of the run). For example, to compress the string "3322251" we replace "33" with "23", replace "222" with "32", replace "5" with "15" and replace "1" with "11". Thus the compressed string becomes "23321511".

# Given a positive integer n, return the nth element of the count-and-say sequence.

 

# Example 1:

# Input: n = 4

# Output: "1211"

# Explanation:

# countAndSay(1) = "1"
# countAndSay(2) = RLE of "1" = "11"
# countAndSay(3) = RLE of "11" = "21"
# countAndSay(4) = RLE of "21" = "1211"
# Example 2:

# Input: n = 1

# Output: "1"

# Explanation:

# This is the base case.

class Solution(object):
    def countAndSay(self, n):
        
        
        if n == 1:
            return "1"
        
        prev = self.countAndSay(n - 1)
        count = 1
        ans = ""
        
        for i in range(1, len(prev)):
            
            if prev[i] == prev[i - 1]:
                count = count + 1
            else:
                ans += str(count) + prev[i - 1]
                count = 1
        
        ans += str(count) + prev[-1]
        
        return ans
    
# Algorithm in short :
# 1. Base case: if n == 1, return "1"
# 2. Recursive case: get the (n-1)th element and apply run-length encoding
# 3. For each group of consecutive identical characters, append the count and the character to the result