class Solution:
    def firstUniqChar(self, s: str) -> int:
        d={}
        new_lis = []
        for i in s:
            if i not in d:
                d[i] = 1
            else:
                d[i]+=1
        for i in d:
            if d[i] == 1:
                new_lis.append(s.index(i))
        if len(new_lis)==0:
            return -1
        return new_lis[0]