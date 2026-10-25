# You are given an integer n and a 2D array requirements, where requirements[i] = [endi, cnti] represents the end index and the inversion count of each requirement.

# A pair of indices (i, j) from an integer array nums is called an inversion if:

# i < j and nums[i] > nums[j]
# Return the number of permutations perm of [0, 1, 2, ..., n - 1] such that for all requirements[i], perm[0..endi] has exactly cnti inversions.

# Since the answer may be very large, return it modulo 109 + 7.

 

# Example 1:

# Input: n = 3, requirements = [[2,2],[0,0]]

# Output: 2

# Explanation:

# The two permutations are:

# [2, 0, 1]
# Prefix [2, 0, 1] has inversions (0, 1) and (0, 2).
# Prefix [2] has 0 inversions.
# [1, 2, 0]
# Prefix [1, 2, 0] has inversions (0, 2) and (1, 2).
# Prefix [1] has 0 inversions.
# Example 2:

# Input: n = 3, requirements = [[2,2],[1,1],[0,0]]

# Output: 1

# Explanation:

# The only satisfying permutation is [2, 0, 1]:

# Prefix [2, 0, 1] has inversions (0, 1) and (0, 2).
# Prefix [2, 0] has an inversion (0, 1).
# Prefix [2] has 0 inversions.
# Example 3:

# Input: n = 2, requirements = [[0,0],[1,0]]

# Output: 1

# Explanation:

# The only satisfying permutation is [0, 1]:

# Prefix [0] has 0 inversions.
# Prefix [0, 1] has no inversions.


from typing import List

class Solution:
    def numberOfPermutations(self, n: int, requirements: List[List[int]]) -> int:
        MOD = 10**9 + 7

        req = {end: cnt for end, cnt in requirements}

        dp = [1]

        for i in range(n):
            new = [0] * (len(dp) + i)

            for inv in range(len(new)):
                for x in range(min(i, inv) + 1):
                    if inv - x < len(dp):
                        new[inv] += dp[inv - x]
                new[inv] %= MOD

            if i in req:
                cnt = req[i]
                dp = [new[cnt] if cnt < len(new) else 0]
            else:
                dp = new

        return dp[0] if dp else 0
