class Solution:
    def firstUniqChar(self, s: str) -> int:
         dic=Counter(s)
         for j in range(len(s)):
            if dic[s[j]] == 1:
                return j
         return -1   
