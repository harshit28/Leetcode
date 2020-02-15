class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        st=[]
        idx=[]
        j=1
        for i in range(len(S)):
            if S[i] == "(":
                st.insert(0,i)
            elif S[i]== ")":
                if len(st)!=1:
                    st.pop()
                else:
                    idx.append(S[j:i])    
                    j=i+2
                    st.pop()
        return ''.join(idx)       
        """ runtime 36ms """        
