# 83. Remove Duplicates from Sorted List
#revised by myself
# Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.

# Examples:

"""
Input: head = [1,1,2]
Output: [1,2]

Example 2:

Input: head = [1,1,2,3,3]
Output: [1,2,3]
"""

# Solution:

from tracemalloc import start


class Solution:
    def deleteDuplicates(self, head):
        if not head:
            return None
        
        current = head
        
        while current and current.next:
            if current.val == current.next.val:
                current.next = current.next.next
            else:
                current = current.next
        
        return head
        


sol = Solution()    
print(sol.deleteDuplicates([1,1,2])) 
print(sol.deleteDuplicates([1,1,2,3,3])) 
        
        
# Algprithm:
# 1. Check if the head is None, if it is, return None.
# 2. Initialize a variable current to the head of the linked list.
# 3. While current is not None and current.next is not None:
#    a. If the value of current is equal to the value of current.next, it means we have found a duplicate. In this case, we skip the next node by setting current.next to current.next.next.
#    b. If the value of current is not equal to the value of current.next, it means we have found a unique element. In this case, we move the current pointer to the next node.
# 4. After the loop, we return the head of the modified linked list, which now contains only unique elements.
