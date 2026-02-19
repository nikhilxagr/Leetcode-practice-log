# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.


# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
# Example 2:

# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# Example 3:

# Input: nums = [3,3], target = 6
# Output: [0,1]
 

class Solution(object):
    def twoSum(self, nums, target):
        for i in range(0,len(nums)):
            for j in range(i , len(nums)):
                if nums[i] + nums[j] == target and i != j :
                    return [i,j]





# nums = [3,3]
# target = 6

# for i in range(0,len(nums)):
#     for j in range(i , len(nums)):
#         if nums[i] + nums[j] == target and i != j :
#             print([i,j])
            

# Another Way 

class Solution(object):
    def twoSum(self, nums, target):
        
        for i in range(len(nums)):
            
            for j in range(i + 1 , len(nums)):
                
                if nums[i] + nums[j] == target :
                    
                    return [i,j]        
    
#Explanation in short :
# We have two loops, the outer loop iterates through each element in the nums array, while the inner loop starts from the next element (i + 1) to avoid using the same element twice.
# Inside the inner loop, we check if the sum of the current elements (nums[i] and nums[j]) equals the target. If it does, we return the indices [i, j].
    
            