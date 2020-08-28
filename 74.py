class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        rowl,coll = len(matrix) , len(matrix[0])
       
        row =0
        for i in range(rowl):
            if target <= matrix[i][coll-1]:
                row=i
                break
        for j in range(coll):
            if target == matrix[row][j]:
                return True
        return False
