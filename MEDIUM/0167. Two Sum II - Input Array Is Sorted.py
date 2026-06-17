# 167. Two Sum II - Input Array Is Sorted

# Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

# Return the indices of the two numbers index1 and index2, each incremented by one, as an integer array [index1, index2] of length 2.

# The tests are generated such that there is exactly one solution. You may not use the same element twice.

# Your solution must use only constant extra space.

 

# Example 1:

# Input: numbers = [2,7,11,15], target = 9
# Output: [1,2]
# Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].
# Example 2:

# Input: numbers = [2,3,4], target = 6
# Output: [1,3]
# Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We return [1, 3].
# Example 3:

# Input: numbers = [-1,0], target = -1
# Output: [1,2]
# Explanation: The sum of -1 and 0 is -1. Therefore index1 = 1, index2 = 2. We return [1, 2].
 

# Constraints:

# 2 <= numbers.length <= 3 * 104
# -1000 <= numbers[i] <= 1000
# numbers is sorted in non-decreasing order.
# -1000 <= target <= 1000
# The tests are generated such that there is exactly one solution.

class Solution(object):
    def twoSum(self, numbers, target):
        
        p1 = 0
        p2 = len(numbers) - 1

        while p1 < p2:
            sum = numbers[p1] + numbers[p2]

            if sum == target:
                return [p1 + 1, p2 + 1]
            elif sum < target:
                p1 += 1
            else:
                p2 -= 1
                
        return []
    
# Approach: 
# 1. We can use two pointers, one starting at the beginning of the array and the other starting at the end of the array.
# 2. We calculate the sum of the two numbers at the pointers. If the sum is equal to the target, we return the indices of the two numbers.
# 3. If the sum is less than the target, we move the left pointer to the right to increase the sum.
# 4. If the sum is greater than the target, we move the right pointer to the left to decrease the sum.
# 5. We continue this process until we find the two numbers that add up to the target.
