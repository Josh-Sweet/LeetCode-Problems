# Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer (similar to C/C++'s atoi function).
#
# The algorithm for myAtoi(string s) is as follows:
#    1. Read in and ignore any leading whitespace.
#    2. Check if the next character (if not already at the end of the string) is '-' or '+'. Read this character in if it is either. This determines if the final result is negative or positive respectively. Assume the result is positive if neither is present.
#    3. Read in next the characters until the next non-digit character or the end of the input is reached. The rest of the string is ignored.
#    4. Convert these digits into an integer (i.e. "123" -> 123, "0032" -> 32). If no digits were read, then the integer is 0. Change the sign as necessary (from step 2).
#    5. If the integer is out of the 32-bit signed integer range [-231, 231 - 1], then clamp the integer so that it remains in the range. Specifically, integers less than -231 should be clamped to -231, and integers greater than 231 - 1 should be clamped to 231 - 1.
#    6. Return the integer as the final result.
# Note:
#    • Only the space character ' ' is considered a whitespace character.
#    • Do not ignore any characters other than the leading whitespace or the rest of the string after the digits.


class Solution:
    def myAtoi(self, s: str) -> int: 
        import re
   
        limit = pow (2,31)
        s = s.lstrip (' ') # Removes leading spaces
    
        if s == "":
            return 0
        elif s[0] == '-': # Check if first character is a negative sign
            # Match all numbers after the sign notation until a non-numerical number is found.
            # Match nothing if there is no numerical character directly after the notation. 
            # Tags a negative sign at the beginning
            resulting_number_string = "-" + re.split (r'[^0-9]', s)[1] 
        elif s[0] == '+': # Check if the first character is a positive sign
            resulting_number_string = re.split (r'[^0-9]', s)[1] # Same here, but positive
        else: 
            resulting_number_string = re.split (r'[^0-9]', s)[0] # Same here, but match from the very beginning of the word.

        # Remove leading zeroes and convert to int, or returns 0 if an improper match was found.
        try:
            resulting_number = int (resulting_number_string.lstrip ('0'))
        except:
            return 0
        
        # Clamp the final result if needed.
        if resulting_number < -limit:
            return -limit
        elif resulting_number > limit - 1:
            return limit - 1
        
        return resulting_number