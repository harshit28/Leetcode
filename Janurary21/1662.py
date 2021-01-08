class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
#         string1 = ""
#         string2 = ""
        
#         for char in word1:
#             string1+=char
            
#         for char in word2:
#             string2+=char
        return "".join(word1) == "".join(word2)
