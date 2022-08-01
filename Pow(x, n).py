# Implement pow(x, n), which calculates x raised to the power n (i.e., x^n) where x is a floating point number and n is an integer.

class Solution:
    def myPow(self, x: float, n: int) -> float:
        # Note: 0/0 is an indeterminate and therefore undefined in most circumstances.
        if x == 1 or n == 0:
            return 1
        elif x == 0 or n == 1:
            return x
        # Simple (-1)^x conversion
        elif x == -1:
            if n % 2 == 0:
                return 1
            return -1
        # x^(-n) is really just 1/x^n
        elif n < 0:
            return 1 / self.myPow (x, -n)
        
        # Recursively traverse this function halving the value of n each time.
        # This works by making use of the following functions derived from exponetial multiplcation:
        #   1. If n is even, x^n = x^(n/2) * x^(n/2)
        #   2. If n is odd, x^n = x * x^(n-1) = x * x^((n-1)/2) * x^((n-1)/2) 
        # 
        # If n = 1, this will simply return x, which is the defined stopping point in recursion.
        # If n is odd, int (n/2) will floor the resulting value. This causes the implied identity int (n/2) == (n-1)/2 to be true for all odd values of n.
        # Example breakdown: 2^7 = 2 * 2^3 * 2^3 = 2 * (2 * 2^1 * 2^1) * (2 * 2^1 * 2^1) = 2 * 8 * 8 = 128
        result = self.myPow (x, int (n / 2))

        if n % 2 == 0:
            return  result * result
        return x * result * result