class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        brac =0 
        
        s_list = list(s)
        i=0 
        n=len(s)
        while i < n:
            if s_list[i] == "(":
                brac +=1
                i+=1
            elif s_list[i] == ")":
                if brac == 0:
                    del s_list[i]
                    n-=1
                else:
                    brac -=1
                    i+=1
            else:
                i+=1
        if brac:
            i= n -1
            while i >= 0:
                if s_list[i] == "(" and brac:
                    brac -=1
                    del s_list[i]
                    n-=1
                    i-=1
                else:
                    i-=1

        return "".join(s_list)
