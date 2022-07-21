class Solution:
    def myAtoi(self, s: str) -> int: 
        import re
   
        limit = pow (2,31)
        s = s.lstrip (' ') # Removes leading spaces
    
        if s == "":
            return 0
        elif s[0] == '-': # Check if first character is a negative sign
            # Match all numbers after the sign notation until a non-numerical number is found.
            # Match nothing if there is no numerical charcter directly after the notation. 
            # Tags a negative sign at the beginning
            resulting_number_string = "-" + re.split (r'[^0-9]', s)[1] 
        elif s[0] == '+': # Check if the first character is a positive sign
            resulting_number_string = re.split (r'[^0-9]', s)[1] # Same here, but positive
        else: 
            resulting_number_string = re.split (r'[^0-9]', s)[0] # Same here, but match from the very beginning of the word.

        try:
            resulting_number = int (resulting_number_string.lstrip ('0')) # Remove leading zeroes and convert to int
        except:
            return 0
        
        # Clamp the final result if needed.
        if resulting_number < -limit:
            return -limit
        elif resulting_number > limit - 1:
            return limit - 1
        
        return resulting_number