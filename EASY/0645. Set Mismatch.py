# 645. Set Mismatch

# REVISED 

# You have a set of integers s, which originally contains all the numbers from 1 to n. Unfortunately, due to some error, one of the numbers in s got duplicated to another number in the set, which results in repetition of one number and loss of another number.

# You are given an integer array nums representing the data status of this set after the error.

# Find the number that occurs twice and the number that is missing and return them in the form of an array.

 

# Example 1:

# Input: nums = [1,2,2,4]
# Output: [2,3]
# Example 2:

# Input: nums = [1,1]
# Output: [1,2]

        
# Approach :  using a set to find the duplicate and missing numbers

class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        num_set = set()
        duplicate = -1
        missing = -1
        
        for num in nums:
            if num in num_set:
                duplicate = num
            else:
                num_set.add(num)
        
        for i in range(1, n + 1):
            if i not in num_set:
                missing = i
                break
        
        return [duplicate, missing]
    
# Algorithm - 
# 1. Initialize an empty set to keep track of seen numbers, and variables for duplicate and missing numbers.
# 2. Iterate through the input array nums:
#    - If the current number is already in the set, it is the duplicate number. Store it in the duplicate variable.
#    - Otherwise, add the current number to the set.
# 3. After processing all numbers, iterate through the range from 1 to n:
#    - If a number is not found in the set, it is the missing number. Store it in the missing variable and break the loop.
# 4. Return the duplicate and missing numbers as a list.