# 118. Pascal's Triangle

# Example 1:

# Input: numRows = 5
# Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

# Example 2:

# Input: numRows = 1
# Output: [[1]]

from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        triangle = []
        
        # Build each row
        
        for i in range(numRows):
            
            # Start each row with 1
            row = [1] * (i + 1)
            
            # Fill in the middle values
            
            for j in range(1, i):
                row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
            
            # Add the row to the triangle
            
            triangle.append(row)
        
        return triangle