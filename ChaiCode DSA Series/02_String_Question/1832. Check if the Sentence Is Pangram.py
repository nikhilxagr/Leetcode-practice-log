# 1832. Check if the Sentence Is Pangram

# A pangram is a sentence where every letter of the English alphabet appears at least once.

# Given a string sentence containing only lowercase English letters, return true if sentence is a pangram, or false otherwise.

 

# Example 1:

# Input: sentence = "thequickbrownfoxjumpsoverthelazydog"
# Output: true
# Explanation: sentence contains at least one of every letter of the English alphabet.
# Example 2:

# Input: sentence = "leetcode"
# Output: false

from itertools import count


class Solution(object):
    def checkIfPangram (self, sentence):
        seen = [False] * 26
        count = 0
        
        for ch in sentence:
            idx = ord(ch) - ord('a')
            
            if not seen [idx]:
                seen [idx] = True
                count += 1
                if count == 26:
                    return True
        return count == 26