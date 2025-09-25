class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        # seen=set()
        if not words:
            return []
        new_set = []
        new_set = [words[0]]
        for i in range(1,len(words)):
            if sorted(words[i]) != sorted(new_set[-1]):
                new_set.append(words[i])
            
        return new_set