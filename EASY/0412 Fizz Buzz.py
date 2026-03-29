# Given an integer n, return a string array answer (1-indexed) where:
# revised 
# answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
# answer[i] == "Fizz" if i is divisible by 3.
# answer[i] == "Buzz" if i is divisible by 5.
# answer[i] == i (as a string) if none of the above conditions are true.

# Example 
"""
Example 1:

Input: n = 3
Output: ["1","2","Fizz"]
Example 2:

Input: n = 5
Output: ["1","2","Fizz","4","Buzz"]
Example 3:

Input: n = 15
Output: ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]
"""

# Solution:

class Solution(object):
    def fizzBuzz(self, n):
        ans = []

        for i in range (1, n+1):
            if i%3==0 and i%5==0:
                ans.append("FizzBuzz")
            elif i%3==0:
                ans.append("Fizz")
            elif i%5==0:
                ans.append("Buzz")
            else:
                ans.append(str(i))   
        return ans                                                

# Algorithm:
# 1. Create an empty list ans to store the results.
# 2. Loop through the numbers from 1 to n (inclusive).
# 3. For each number i, check the following conditions:
#    a. If i is divisible by both 3 and 5, append "FizzBuzz" to ans.
#    b. If i is divisible by 3, append "Fizz" to ans.
#    c. If i is divisible by 5, append "Buzz" to ans.
#    d. If none of the above conditions are true, append the string representation of i
#       to ans.
# 4. After the loop, return the ans list containing the results.
