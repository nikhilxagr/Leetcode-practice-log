# 118. Pascal's Triangle
# revised 
#Revisit
"""
Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:
"""

# Examples

"""
Example 1:

Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

Example 2:

Input: numRows = 1
Output: [[1]]
"""


class Solution(object):
    def generate_alternate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        
        triangle = []

        for row_num in range(numRows):
            row = [1] * (row_num + 1)

            for j in range(1, row_num):
                row[j] = triangle[row_num - 1][j - 1] + triangle[row_num - 1][j]

            triangle.append(row)

        return triangle
    
# Algorithm:
# 1. Initialize an empty list called triangle to store the rows of Pascal's triangle.
# 2. Loop through each row number from 0 to numRows - 1.
# 3. For each row, create a list called row initialized with 1's, where the length of the row is row_num + 1.
# 4. For each element in the row (except the first and last), calculate its value as the sum of the two elements directly above it from the previous row in the triangle.
# 5. Append the completed row to the triangle list.