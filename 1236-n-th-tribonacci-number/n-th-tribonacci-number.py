class Solution:
    def tribonacci(self, n: int) -> int:
        # base case
        if n==0:
            return 0
        elif n==1 or n==2:
            return 1
        # iterative approach
        a,b,c = 0,1,1
        for i in range(3,n+1):
            a,b,c = b,c,a+b+c
        return c