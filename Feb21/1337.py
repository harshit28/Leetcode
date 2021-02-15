class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        row = {}
        output=[]
        for i in range(len(mat)):
            row[i]=sum(mat[i])
            
        # output=row.items()
        return sorted(row, key=row.get)[:k]
