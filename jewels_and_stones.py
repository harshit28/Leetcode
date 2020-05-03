from collections import Counter
class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        # dic=Counter(S)
        count=0
        for i in S:
            if i in J:
                count+=1
        return count        
        
