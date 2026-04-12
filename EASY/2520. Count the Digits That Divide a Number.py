# Problem 

# revised

# 2520. Count the Digits That Divide a Number

# Given an integer num, return the number of digits in num that divide num.

# An integer val divides nums if nums % val == 0.\
    
# Example

"""
Example 1:

Input: num = 7
Output: 1
Explanation: 7 divides itself, hence the answer is 1.

Example 2:

Input: num = 121
Output: 2
Explanation: 121 is divisible by 1, but not 2. Since 1 occurs twice as a digit, we return 2.

Example 3:

Input: num = 1248
Output: 4
Explanation: 1248 is divisible by all of its digits, hence the answer is 4.    

"""

# Solution

class Solution(object):
    def countDigits(self, num):
        
        count = 0
        
        digits = str(num)

        for d in digits:
            
            digit = int(d)
            if digit == 0:
                continue
            
            if num % digit == 0:
                count += 1

        return count

sol = Solution()    
print(sol.countDigits(7))   
print(sol.countDigits(121))
print(sol.countDigits(1248))

# Algorithm:
# 1. Convert the number to a string to access each digit.
# 2. Initialize a count variable to keep track of the number of digits that divide the number.
# 3. Iterate through each character (digit) in the string representation of the number.
# 4. Convert the character back to an integer.
# 5. If the digit is zero, skip it to avoid division by zero.
# 6. Check if the original number is divisible by the digit. If it is, increment the count.
# 7. Return the final count after iterating through all digits.