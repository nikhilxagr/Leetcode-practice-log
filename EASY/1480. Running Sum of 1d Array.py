# 1480. Running Sum of 1d Array
# revised
# Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

# Return the running sum of nums.

# Examples:
"""
Example 1:

Input: nums = [1,2,3,4]
Output: [1,3,6,10]
Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].
Example 2:

Input: nums = [1,1,1,1,1]
Output: [1,2,3,4,5]
Explanation: Running sum is obtained as follows: [1, 1+1, 1+1+1, 1+1+1+1, 1+1+1+1+1].
Example 3:

Input: nums = [3,1,2,10,1]
Output: [3,4,6,16,17]
"""

# Solution:

class Solution(object):
    def runningSum(self, nums):
        n = len(nums)
        
        ans =  []
        ans.append(nums[0]) 
        
        for i in range(1, n):
            x = ans[i-1] + nums[i]
            ans.append(x)
        return ans

# Example usage:
sol = Solution()    
print(sol.runningSum([1,2,3,4])) 
print(sol.runningSum([1,1,1,1,1]))
        
# Algorithm:
# 1. Initialize an empty list ans and append the first element of nums to it.
# 2. Iterate through nums starting from the second element (index 1) to the end of the list.
# 3. For each element at index i, calculate the running sum by adding the previous
#    running sum (ans[i-1]) to the current element (nums[i]) and append the result to ans.
# 4. Return the list ans containing the running sums.