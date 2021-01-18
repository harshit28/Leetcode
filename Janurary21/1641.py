class Solution:
    def countVowelStrings(self, n: int) -> int:
        dp = {'a':1,'e':1,"i":1,"o":1,"u":1}
        p = 1 
        while p < n:
            new_dp = {'a':0,'e':0,"i":0,"o":0,"u":0}
            for x in 'aeiou':
                for y in 'aeiou':
                    if x <= y:
                        new_dp[y] += dp[x]
                    print(new_dp)

            dp = new_dp
            p += 1
        
        return sum(dp.values())
        
