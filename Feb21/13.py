class Solution:

    def romanToInt(self, s: str) -> int:
        hashmap={ "I":1,"V": 5,"X": 10,"L": 50,"C": 100,"D":500,"M":1000}
        
        count = hashmap[s[-1]]
        for i in range(len(s)-2,-1,-1):
            if hashmap[s[i]] >= hashmap[s[i+1]]:
                count+= hashmap[s[i]]
            else:
                count-= hashmap[s[i]]
        return count
