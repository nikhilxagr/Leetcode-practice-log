# 485. Max Consecutive Ones

# revised 
# Given a binary array nums, return the maximum number of consecutive 1's in the array.

 

# Example 1:

# Input: nums = [1,1,0,1,1,1]
# Output: 3
# Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.
# Example 2:

# Input: nums = [1,0,1,1,0,1]
# Output: 2

# Algorithm:
# 1. Initialize two variables, count and ans, to keep track of the current count of consecutive 1's and the maximum count found so far.
# 2. Iterate through each element in the input array nums.
# 3. If the current element is 1, increment the count variable and update ans with the maximum of count and ans.
# 4. If the current element is 0, reset the count variable to 0.
# 5. After the loop, return the value of ans, which will be the maximum
# number of consecutive 1's in the array.


class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        ans = 0

        for i in range(len(nums)):
    
            if nums[i] == 1:
                count += 1
                ans = max(count,ans)
            else:
                count = 0
        return ans        
        
  
# Test Case   
        
# nums = [1,1,0,1,1,1]
# count = 0
# ans = 0

# for i in range(len(nums)):
    
#     if nums[i] == 1:
#         count += 1
#         ans = max(count,ans)
#     else:
#         count = 0
        
# print(ans)