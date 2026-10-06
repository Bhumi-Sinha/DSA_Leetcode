class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        maxCandies=max(candies)
        ans=[]
        for i in candies:
            summed_candies=i+extraCandies
            if summed_candies>=maxCandies:
                ans.append(True)
            else:
                ans.append(False)
        return ans