class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        def no_of_words(sen):
            word = list(sen.split(" "))
            return len(word)
        l = []
        for i in sentences:
            l.append(no_of_words(i))
        return max(l)