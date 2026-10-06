class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        prod_of_digits=1
        sum_of_digits=0
        while n>0:
            r=n%10
            prod_of_digits=prod_of_digits*r
            sum_of_digits=sum_of_digits+r
            n=n//10
        ans = prod_of_digits-sum_of_digits     
        return ans       