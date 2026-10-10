import math
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n==1:
            return True
        else:
            if n>0 and math.log2(n).is_integer():
                return True
            else:
                return False