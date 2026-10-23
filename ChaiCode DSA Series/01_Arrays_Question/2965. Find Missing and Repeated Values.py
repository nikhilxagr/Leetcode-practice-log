# 2965. Find Missing and Repeated Values

# You are given a 0-indexed 2D integer matrix grid of size n * n with values in the range [1, n2]. Each integer appears exactly once except a which appears twice and b which is missing. The task is to find the repeating and missing numbers a and b.

# Return a 0-indexed integer array ans of size 2 where ans[0] equals to a and ans[1] equals to b.

 

# Example 1:

# Input: grid = [[1,3],[2,2]]
# Output: [2,4]
# Explanation: Number 2 is repeated and number 4 is missing so the answer is [2,4].
# Example 2:

# Input: grid = [[9,1,7],[8,9,2],[3,4,6]]
# Output: [9,5]
# Explanation: Number 9 is repeated and number 5 is missing so the answer is [9,5].
 
 
from typing import List

class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        N = n * n
        count = [0] * (N + 1)

        # Count occurrences of each number
        for row in grid:
            for num in row:
                count[num] += 1

        repeated = -1
        missing = -1

        # Find the repeated and missing numbers
        for i in range(1, N + 1):
            if count[i] == 2:
                repeated = i
            elif count[i] == 0:
                missing = i

        return [repeated, missing]