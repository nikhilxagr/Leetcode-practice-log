# Given an integer array nums of length n and an integer target, find three integers at distinct indices in nums such that the sum is closest to target.

# Return the sum of the three integers.

# You may assume that each input would have exactly one solution.

 

# Example 1:

# Input: nums = [-1,2,1,-4], target = 1
# Output: 2
# Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
# Example 2:

# Input: nums = [0,0,0], target = 1
# Output: 0
# Explanation: The sum that is closest to the target is 0. (0 + 0 + 0 = 0).
 

# Constraints:

# 3 <= nums.length <= 500
# -1000 <= nums[i] <= 1000
# -104 <= target <= 104


class Solution(object):
    def threeSumClosest(self, nums, target):
        
        nums.sort()

        closest = nums[0] + nums[1] + nums[2]

        for i in range(len(nums) - 2):
            
            left = i + 1
            right = len(nums) - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                # Update closest if current sum is nearer to target
                
                if abs(target - total) < abs(target - closest):
                    closest = total

                if total < target:
                    left += 1
                elif total > target:
                    right -= 1
                else:
                    return total  # Exact match

        return closest
    
# # Algorithm - 
# 1 . Sort the array first.
# 2 . Fix one number nums[i].
# 3 . Use two pointers to find the other two numbers.
# 4 . Update the closest sum if the current sum is nearer to the target.
# 5 . Return the closest sum after checking all combinations.
# 6 . Time Complexity: O(n^2), where n is the length of the input array.