# Given a signed 32-bit integer x, return x with its digits reversed. 
# If reversing x causes the value to go outside the signed 32-bit integer range [-2^31, 2^31 - 1], then return 0.

class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            result = -int (str (x)[:0:-1])
        else:
            result = int (str (x)[::-1])
                
        limit = pow (2,31)
        
        if result >= -limit and result <= limit - 1:
            return result
        
        return 0
        
        