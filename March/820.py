class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        hashset = set(words)
       
        for word in words:
            for j in range(1,len(word)):
                hashset.discard(word[j:])
       
        return sum(len(word)+1 for word in hashset)
