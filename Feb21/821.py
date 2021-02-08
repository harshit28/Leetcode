class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        result = [0] * len(s)
        indexc= []
        
        
        for i in range(len(s)):
            if s[i] == c:
                indexc.append(i)
                
                
        for i in range(len(s)):
            if s[i]!=c:
                result[i]=min(abs(index-i) for index in indexc)
            
        return result
            
