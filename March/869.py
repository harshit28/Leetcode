from itertools import permutations
class Solution:
    def isPower(self,n, base):
        if base == 1 and n != 1:
            return False
        if base == 1 and n == 1:
            return True
        if base == 0 and n != 1:
            return False
        power = int (math.log(n, base) + 0.5)
        return base ** power == n

    def reorderedPowerOf2(self, N: int) -> bool:
        
        if self.isPower(N,2):
            return True
        
        else:
            orig = str(N)
            per = list(permutations(orig,len(orig)))
            for i in range(len(per)):
                tocheck = "".join(per[i])
                if tocheck[0] == "0":
                    continue
                    # return False
                if self.isPower(int(tocheck),2):
                    return True
            
            return False
