class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a_num = int(a,2)
        b_num = int(b,2)
        return str(bin(a_num+b_num))[2:]