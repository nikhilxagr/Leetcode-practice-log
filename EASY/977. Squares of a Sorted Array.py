# 977. Squares of a Sorted Array
# revised
# Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

# Example 1:

# Input: nums = [-4,-1,0,3,10]
# Output: [0,1,9,16,100]
# Explanation: After squaring, the array becomes [16,1,0,9,100].
# After sorting, it becomes [0,1,9,16,100].
# Example 2:

# Input: nums = [-7,-3,2,3,11]
# Output: [4,9,9,49,121]

# Solution:



from numpy import sort


class Solution(object):
    def sortedSquares(self, nums):
      
        result = []
        
        for num in nums:
            result.append(pow(num ,2))
            
        result.sort()    
            
        return result
            
        
# # Algorithm:
# 1. Initialize an empty list `result` to store the squares of the numbers.
# 2. Iterate through each number `num` in the input list `nums`:
#    a. Calculate the square of `num` using the `pow` function and append it to the `result` list.
# 3. After the loop, sort the `result` list in non-decreasing order using the `sort` method.
# 4. Return the sorted `result` list, which contains the squares of the numbers in non-decreasing order.

# Another Approach:  Using Two Pointers Technique

class Solution(object):
    def sortedSquares(self, nums):
        
        n = len(nums)
        result = [0] * n

        i = 0
        j = n - 1
        pos = n - 1

        while i <= j:
            
            left_sq = nums[i] * nums[i]
            right_sq = nums[j] * nums[j]

            if left_sq > right_sq:
                result[pos] = left_sq
                i += 1
                
            else:
                result[pos] = right_sq
                j -= 1

            pos -= 1

        return result
    
# Approach - use two pointers technique to fill the result array from the end to the beginning.

# Compare the squares of the elements at the left and right pointers, and place the larger square at the current position in the result array.

# Move the corresponding pointer inward and repeat until all elements are processed. This approach has a time complexity of O(n) and does not require additional sorting.