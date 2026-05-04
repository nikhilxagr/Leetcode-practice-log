# 451. Sort Characters By Frequency
#revised

# Given a string s, sort it in decreasing order based on the frequency of the characters. The frequency of a character is the number of times it appears in the string.

# Return the sorted string. If there are multiple answers, return any of them.

 

# Example 1:

# Input: s = "tree"
# Output: "eert"
# Explanation: 'e' appears twice while 'r' and 't' both appear once.
# So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.
# Example 2:

# Input: s = "cccaaa"
# Output: "aaaccc"
# Explanation: Both 'c' and 'a' appear three times, so both "cccaaa" and "aaaccc" are valid answers.
# Note that "cacaca" is incorrect, as the same characters must be together.
# Example 3:

# Input: s = "Aabb"
# Output: "bbAa"
# Explanation: "bbaA" is also a valid answer, but "Aabb" is incorrect.
# Note that 'A' and 'a' are treated as two different characters.

class Solution(object):
    def frequencySort(self, s):
        
        from collections import Counter
        
        return ''.join(ch * freq for ch, freq in Counter(s).most_common())
    
# Algorithm:
# 1. We use the Counter class from the collections module to count the frequency of each character in the input string s.
# 2. We then use the most_common() method of the Counter object to get a list of tuples, where each tuple contains a character and its corresponding frequency, sorted in decreasing order of frequency.
# 3. Finally, we construct the output string by repeating each character according to its frequency and joining them together using the join() method. The resulting string is returned as the output.