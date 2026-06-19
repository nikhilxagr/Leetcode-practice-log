# 26. Remove Duplicates from Sorted Array
# Revised
"""
Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same.

Consider the number of unique elements in nums to be k​​​​​​​​​​​​​​. After removing duplicates, return the number of unique elements k.

The first k elements of nums should contain the unique numbers in sorted order. The remaining elements beyond index k - 1 can be ignored.
"""

# Example 2:
"""
 Input: nums = [0,0,1,1,1,2,2,3,3,4]
 Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
 Explanation: Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.
 It does not matter what you leave beyond the returned k (hence they are underscores).
 
 """
 
# nums = [0, 0 , 1, 1 , 2, 3, 3, 4]

# for i in range(len(nums)):
#     print(nums[i])      
    
# def removeDuplicates(nums):
#     if not nums:
#         return 0

#     write_index = 1 

#     for i in range(1, len(nums)):
#         if nums[i] != nums[i - 1]: 
#             nums[write_index] = nums[i] 
#             write_index += 1  

#     return write_index  


# SOlve with pop method
from ast import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        while i < len(nums) - 1:
            if nums[i] == nums[i + 1]:
                nums.pop(i)
            else:
                i += 1
        return len(nums)
    
# ALgorithm:
# 1. Initialize a variable write_index to 1, which will keep track of the position where the next unique element should be written.
# 2. Iterate through the array starting from the second element (index 1) to the end of the array.
# 3. For each element, compare it with the previous element (nums[i - 1]).
# 4. If the current element is different from the previous element, it means it's a unique element. Write this unique element to the position indicated by write_index and increment write_index by 1.
# 5. After the loop, write_index will indicate the number of unique elements in the array, and the first write_index elements of the array will contain the unique elements in sorted order.



# Solve using 2 pointers
class Solution(object):
    def removeDuplicates(self, nums):
        if not nums:
            return 0

        low = 0  # Pointer for the position of the last unique element
        high = 1  # Pointer for traversing the array
        result = 1  # Count of unique elements
        
        while high < len(nums):
            
            if nums[low] != nums[high]:
                low += 1
                
                nums[low] = nums[high]
                result += 1
                
            high += 1
            
        return result
    
# Approach - use two pointers, one for the current position and one for the next unique element. Iterate through the array, and whenever a new unique element is found, move it to the next position indicated by the first pointer. Finally, return the count of unique elements.
