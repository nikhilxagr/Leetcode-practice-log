# 21. Merge Two Sorted Lists

# Revised
# You are given the heads of two sorted linked lists list1 and list2.

# Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

# Return the head of the merged linked list.

# Example 1:


# Input: list1 = [1,2,4], list2 = [1,3,4]
# Output: [1,1,2,3,4,4]
# Example 2:

# Input: list1 = [], list2 = []
# Output: []
# Example 3:

# Input: list1 = [], list2 = [0]
# Output: [0]
 
 
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        temp = ListNode()
        
        curr = temp
        while list1 and list2:
            
            if list1.val < list2.val:
                curr.next = list1
                list1 = list1.next
                
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next
        curr.next = list1 or list2
        return temp.next
        
# Algorithm:
# 1. Create a temporary node to hold the merged list and a current pointer to traverse it.
# 2. While both list1 and list2 are not empty:
#    - Compare the values of the current nodes in both lists.
#    - Attach the node with the smaller value to the merged list.
#    - Move the pointer of the list from which the node was attached.
# 3. After one of the lists is exhausted, attach the remaining nodes from the other list to the merged list.
# 4. Return the head of the merged list.