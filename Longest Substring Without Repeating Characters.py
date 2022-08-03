# Given a string s, find the length of the longest substring without repeating characters.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        distinct_characters = [] # Current substring of distinct characters
        current_result = [] # Current result to return the length of
        
        for char in s:
            if char in distinct_characters:
                # Set the value of the current substring to be every character after the repeating character.
                # Example: "0123453" will set the current substring to "45" if char is "3" and it passed if check.
                distinct_characters = distinct_characters[distinct_characters.index (char) + 1:]
                
            distinct_characters += char    
            
            if len (distinct_characters) > len (current_result):
                current_result = distinct_characters
       
        return len (current_result)