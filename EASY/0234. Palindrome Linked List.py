# 234. Palindrome Linked List
# revised 
# Given the head of a singly linked list, return true if it is a palindrome or false otherwise.

 

# Example 1:


# Input: head = [1,2,2,1]
# Output: true
# Example 2:


# Input: head = [1,2]
# Output: false


class Solution(object):
    def isPalindrome(self, head):
        
        if not head:
            return True
        
        point_1 = head
        point_2 = head

        while point_2 and point_2.next:
            point_1 = point_1.next
            point_2 = point_2.next.next

        prev = None
        curr = point_1

        while curr:
            
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        left, right = head, prev

        while right:
            
            if left.val != right.val:
                return False
            left = left.next
            right = right.next

        return True
    
# Algorithm :
# 1. Use the fast and slow pointer technique to find the middle of the linked list.
# 2. Reverse the second half of the linked list.
# 3. Compare the first half and the reversed second half of the linked list.