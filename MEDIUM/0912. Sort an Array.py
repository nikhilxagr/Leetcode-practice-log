# 912. Sort an Array

# revised 
# Given an array of integers nums, sort the array in ascending order and return it.

# You must solve the problem without using any built-in functions in O(nlog(n)) time complexity and with the smallest space complexity possible.

 

# Example 1:

# Input: nums = [5,2,3,1]
# Output: [1,2,3,5]

# Explanation: After sorting the array, the positions of some numbers are not changed (for example, 2 and 3), while the positions of other numbers are changed (for example, 1 and 5).

# Example 2:

# Input: nums = [5,1,1,2,0,0]
# Output: [0,0,1,1,2,5]
# Explanation: Note that the values of nums are not necessarily unique.

class Solution(object):
    def sortArray(self, nums):

        def heapify(n, i):
            largest = i
            left = 2 * i + 1
            right = 2 * i + 2

            if left < n and nums[left] > nums[largest]:
                largest = left

            if right < n and nums[right] > nums[largest]:
                largest = right

            if largest != i:
                nums[i], nums[largest] = nums[largest], nums[i]
                heapify(n, largest)

        n = len(nums)

        # Build Max Heap
        for i in range(n // 2 - 1, -1, -1):
            heapify(n, i)

        # Extract elements one by one
        for i in range(n - 1, 0, -1):
            nums[0], nums[i] = nums[i], nums[0]
            heapify(i, 0)

        return nums

# Algorithm:
# 1. Build a Max Heap from the input array.
# 2. Swap the root of the Max Heap (the largest element) with the last element of the heap.
# 3. Reduce the size of the heap by one and heapify the root element to maintain the Max Heap property.
# 4. Repeat steps 2 and 3 until the heap is empty.
