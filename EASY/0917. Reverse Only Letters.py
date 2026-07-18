# 917. Reverse Only Letters

# Given a string s, reverse the string according to the following rules:

# All the characters that are not English letters remain in the same position.
# All the English letters (lowercase or uppercase) should be reversed.
# Return s after reversing it.

 

# Example 1:

# Input: s = "ab-cd"
# Output: "dc-ba"
# Example 2:

# Input: s = "a-bC-dEf-ghIj"
# Output: "j-Ih-gfE-dCba"
# Example 3:

# Input: s = "Test1ng-Leet=code-Q!"
# Output: "Qedo1ct-eeLg=ntse-T!"



class Solution(object):
    def reverseOnlyLetters(self, s):
        
        # Collect all letters
        
        letters = []
        
        for char in s:
            if char.isalpha():
                letters.append(char)
        
        # Reverse 
    
        letters.reverse()
        
        # Build result with reversed letters in place
        
        ans = []
        letter_ind = 0
        
        for char in s:
            if char.isalpha():
                ans.append(letters[letter_ind])
                letter_ind += 1
            else:
                ans.append(char)
        
        # Convert list back to string
        
        return ''.join(ans)
    
# Algorithm:
# Step 1: Collect all letters
# Step 2: Reverse the letters list
# Step 3: Build result with reversed letters in place
# Step 4: Convert list back to string