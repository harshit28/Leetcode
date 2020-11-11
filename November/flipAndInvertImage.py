class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        row,col = len(A), len(A[0])
        for i in range(row):
            for j in range(col//2):
                A[i][j],A[i][col-1-j]= A[i][col-1-j] ,A[i][j]
        for i in range(row):
            for j in range(col):
                if A[i][j] == 1:
                    A[i][j] = 0
                else:
                    A[i][j] = 1
        return A
