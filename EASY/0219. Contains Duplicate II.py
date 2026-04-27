# 219. Contains Duplicate II

# Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

 

# Example 1:

# Input: nums = [1,2,3,1], k = 3
# Output: true
# Example 2:

# Input: nums = [1,0,1,1], k = 1
# Output: true
# Example 3:

# Input: nums = [1,2,3,1,2,3], k = 2
# Output: false
 
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        last_seen = {}  # stores number -> last index

        for i in range(len(nums)):
            num = nums[i]

            # check if we've seen this number before
            if num in last_seen:
                if i - last_seen[num] <= k:
                    return True

            # update last seen index
            last_seen[num] = i

        return False
    
# Algorithm:
# 1. Initialize an empty dictionary `last_seen` to store the last index of each number.
# 2. Iterate through the array `nums` using a loop.
# 3. For each number, check if it has been seen before by looking it up in `last_seen`.
# 4. If it has been seen, check if the difference between the current index and the last seen index is less than or equal to `k`. If it is, return `True`.
# 5. Update the last seen index of the current number in the `last_seen` dictionary.