class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        
        def dfs(sub="",i=0):
            if len(S) == len(sub):
                res.append(sub)
                
            else:
                if S[i].isalpha():
                    dfs(sub+S[i].swapcase(),i+1)
                dfs(sub+S[i],i+1)
                
        res=[]
        dfs()
        return res
