# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
# Revised 
# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
 
 
#  Examples: 
"""
Example 1:

Input: s = "()"

Output: true

Example 2:

Input: s = "()[]{}"

Output: true

Example 3:

Input: s = "(]"

Output: false

Example 4:

Input: s = "([])"

Output: true

Example 5:

Input: s = "([)]"

Output: false
"""

class Solution(object):
    def isValid(self, s):
        stack = []

        for char in s:
            if char == '(' or char == '{' or char == '[':
                stack.append(char)
            else:
                if not stack:
                    return False

                last = stack.pop()

                if char == ')' and last != '(':
                    return False
                if char == '}' and last != '{':
                    return False
                if char == ']' and last != '[':
                    return False

        return len(stack) == 0

# Logic :
    
# - Initialize an empty stack to keep track of opening brackets.
# - Iterate through each character in the input string:
#   - If the character is an opening bracket ('(', '{', '['), push it onto the stack.
#   - If the character is a closing bracket (')', '}', ']'):
#     - Check if the stack is empty. If it is, return False (indicating an invalid string).
    
#     - Pop the last opening bracket from the stack and check if it matches the corresponding opening bracket for the current closing bracket. If it doesn't match, return False.
# - After iterating through all characters, check if the stack is empty. If it is, return True (indicating a valid string); otherwise, return False (indicating an invalid string).
