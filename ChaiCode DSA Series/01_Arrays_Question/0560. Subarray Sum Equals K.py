# 560. Subarray Sum Equals K

# Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

# A subarray is a contiguous non-empty sequence of elements within an array.

 

# Example 1:

# Input: nums = [1,1,1], k = 2
# Output: 2
# Example 2:

# Input: nums = [1,2,3], k = 3
# Output: 2

from typing import List
from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        # Dictionary to store prefix sum frequencies
        
        prefix_sum_count = defaultdict(int)
        prefix_sum_count[0] = 1
        
        current_sum = 0
        count = 0
        
        for num in nums:
            # Update the running prefix sum
            
            current_sum += num
            
            # Check if there is a prefix sum that matches current_sum - k
            
            count += prefix_sum_count[current_sum - k]
            
            # Update the frequency of the current prefix sum
            
            prefix_sum_count[current_sum] += 1
            
        return count