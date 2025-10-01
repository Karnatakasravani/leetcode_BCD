class Solution:
    def numWaterBottles(self, n: int, k: int) -> int:
        # numBottles = n
        # numExchange = k
        s = n
        while n>=k:
            # print(n//k,s)
            r=n//k
            s+=r
            n=n%k+r
        return s