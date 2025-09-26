class Solution:
    def triangleNumber(self, arr: List[int]) -> int:
        arr.sort()
        cnt = 0
        n = len(arr)

        for i in range(n-1,1,-1):
            j = 0
            k = i-1
            while j<k:
                if arr[j]+arr[k] > arr[i]:
                    cnt+= (k-j)
                    k-=1
                else:
                    j+=1
    
        return cnt
        