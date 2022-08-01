# Given a roman numeral, convert it to an integer on the range of [1, 3999].

class Solution:
    def romanToInt(self, s: str) -> int:
        integer_number = 0
        
        conversion_dict = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
        
        # Loop through the string until the last element is reached. 
        # Using indexes because I'm not sure how to enumerate both the current value and the next value.
        for i in range (len (s) - 1):
            # If the current roman value is less than the next roman value (e.g. IV, where I is less than V), subtract it instead of adding it.
            # This works because the next roman numeral afterwards will be added and make up for the lost amount. It pretty much subtracts from the higher value roman numeral.
            # IX in this case would turn 0 into -1, but then get turned into 9 on the next passthrough.
            if conversion_dict[s[i]] < conversion_dict[s[i + 1]]:
                integer_number -= conversion_dict[s[i]] 
            else:
                integer_number += conversion_dict[s[i]] 
        
        integer_number += conversion_dict[s[len (s) - 1]] # Do conversion for the last roman numeral and add it.
        
        return integer_number