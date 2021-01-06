class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        c_s=Counter(s)
        c_t=Counter(t)
        for char in t:
            if char not in c_s:
                return char
            elif c_s[char] !=c_t[char]:
                return char
        return ""
