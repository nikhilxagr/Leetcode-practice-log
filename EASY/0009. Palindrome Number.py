# 9. Palindrome Number
# Revised
# Given an integer x, return true if x is a palindrome, and false otherwise.

# Example 1:

# Input: x = 121
# Output: true
# Explanation: 121 reads as 121 from left to right and from right to left.
# Example 2:

# Input: x = -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
# Example 3:

# Input: x = 10
# Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a palindrome.


# class Solution:
#     def isPalindrome(self, x: int) -> bool:
#         if x < 0:
#             return False
    
#         num_str = str(x)
#         rev_str = num_str[::-1]

#         return num_str == rev_str

# Another Approach:
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        real = x
        rev_num = 0
        
        while x > 0:
            digit = x % 10
            rev_num = rev_num * 10 + digit
            x //= 10
        
        return real == rev_num
    
# Algorithm in short:
# 1. We first check if the number is negative. If it is, we return False since negative numbers cannot be palindromes.
# 2. We store the original number in a variable called real and initialize rev_num to 0, which will hold the reversed number.
# 3. We use a while loop to reverse the number. In each iteration, we extract the last digit of x using x % 10 and add it to rev_num after shifting rev_num left by one digit (rev_num * 10). We then remove the last digit from x using integer division (x //= 10).
# 4. Finally, we compare the original number (real) with the reversed number (rev_num). If they are equal, we return True, indicating that the number is a palindrome; otherwise, we return False.