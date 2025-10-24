class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s=""
        for i in digits:
            s+=str(i)
        num = int(s)
        num_str = str(num+1)
        lis = []
        for i in num_str:
            lis.append(int(i))
        return lis
    
        