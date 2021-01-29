class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        k-=n
        comb,i=['a']*n,n-1
        while i >=0 and k > 0:
            
            comb[i] = chr(ord(comb[i]) + min(k,25))
            k-=min(k,25)
            i-=1
            
        return "".join(comb)
