class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        freq,n,candy=Counter(candyType),len(candyType)//2,0
        
        for elem in freq:
            if n <= 0:
                return candy
            candy+=1
            n-=1
            
        return candy
            
