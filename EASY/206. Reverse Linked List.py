# Given the head of a singly linked list, reverse the list, and return the reversed list.

# Revised the problem statement to be more clear and concise.

# Example 1:


# Input: head = [1,2,3,4,5]
# Output: [5,4,3,2,1]
# Example 2:


# Input: head = [1,2]
# Output: [2,1]
# Example 3:

# Input: head = []
# Output: []
 


class Solution(object):
    def reverseList(self, head):

        prev = None
        curr = head
        
        while curr:

            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        
        return prev
    
# Algorithm :
# 1. Initialize two pointers, `prev` as None and `curr` as the head of the linked list.
# 2. Iterate through the linked list until `curr` is None:
#    a. Store the next node of `curr` in a variable `next_node`.
#    b. Reverse the link by setting `curr.next` to `prev`.
#    c. Move the `prev` pointer to `curr`.
#    d. Move the `curr` pointer to `next_node`.
# 3. After the loop ends, `prev` will be pointing to the new head of the reversed linked list.

