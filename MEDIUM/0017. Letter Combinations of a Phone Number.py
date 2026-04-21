# 17. Letter Combinations of a Phone Number
# revised 
# Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

# A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

# Examples
"""
Example 1:

Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
Example 2:

Input: digits = "2"
Output: ["a","b","c"]
"""

# Solution:

class Solution(object):
    def letterCombinations(self, digits):
        if digits == "":
            return []

        phone = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        ans = [""]

        for digit in digits:
            temp = []
            letters = phone[digit]

            for r in ans:
                for char in letters:
                    temp.append(r + char)

            ans = temp

        return ans
    
# Algorithm:
# 1. Create a mapping of digits to letters based on the telephone buttons.
# 2. Initialize an answer list with an empty string to store the combinations.
# 3. Iterate through each digit in the input string:
#    a. For each digit, create a temporary list to store the new combinations.
#    b. For each existing combination in the answer list, append each corresponding letter from the mapping to create new combinations and add them to the temporary list.
#    c. Update the answer list with the new combinations from the temporary list.
# 4. Return the final answer list containing all possible letter combinations.
