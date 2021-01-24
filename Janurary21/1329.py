class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        # hashmap to keep the diagonals
        h = defaultdict(list)
        
        # fill the hashmap
        n, m = len(mat), len(mat[0])
        for i in range(n):
            for j in range(m):
                heappush(h[i - j], mat[i][j])

        # build output
        for i in range(n):
            for j in range(m):
                mat[i][j] = heappop(h[i - j])
        
        return mat
