# 46. Permutations

# Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

# revised 

# Example 1:

"""
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
Example 2:

Input: nums = [0,1]
Output: [[0,1],[1,0]]
Example 3:

Input: nums = [1]
Output: [[1]]
 """
 
#  Solution:

class Solution:
    def permute(self, nums):
        ans = []
        
        def backtrack(start=0):
            if start == len(nums):
                ans.append(nums[:])
                return
            
            for i in range(start, len(nums)):
                nums[i], nums[start] = nums[start], nums[i]  # Swap
                backtrack(start + 1)
                nums[start], nums[i] = nums[i], nums[start]  # Backtrack
        
        backtrack()
        return ans
    
# Algorithm :
# 1. We define a helper function `backtrack` that takes an optional parameter `start` which indicates the current index we are working on.
# 2. If `start` is equal to the length of `nums`, it means we have generated a complete permutation, and we append a copy of `nums` to the answer list `ans`.
# 3. We iterate through the indices from `start` to the end of the list, swapping the current index with the `start` index to generate a new permutation.
# 4. We then call `backtrack` recursively with `start + 1` to continue generating permutations for the next index.
# 5. After the recursive call, we swap back the elements to restore the original order (backtracking) before the next iteration.