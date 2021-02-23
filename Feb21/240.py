class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row,col=len(matrix[0]),len(matrix)
        
        if not row or not col:
            return False
        j = col - 1
        i = 0
        while i < row and j >= 0:
                if matrix[j][i] == target:
                    return True
                elif matrix[j][i] < target:
                    i+=1
                else:
                    j-=1
        return False
