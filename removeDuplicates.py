class Solution:
    def removeDuplicates(self, S: str) -> str:
        st = []
        for i in range(len(S)):
            if len(st)==0:
                st.append(S[i])             
            elif S[i]!=st[-1]:
                st.append(S[i])
            else:
                st.pop(-1)
        return "".join(st)       
            
            
        
