class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)
        i=1
        cn = n-i
        while i < n:
            sub = s[:i]
            index= n // len(sub)
            to_check = sub * index
            if to_check == s :
                return True
            i+=1
        return False
