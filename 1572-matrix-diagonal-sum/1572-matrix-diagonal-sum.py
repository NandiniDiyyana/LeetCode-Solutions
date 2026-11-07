class Solution:
    def diagonalSum(self, mat: list[list[int]]) -> int:
        rows = len(mat)
        cols = len(mat[0])
        count = 0
        '''for i in range(rows):
            for j in range(cols):
                if i == j or j == cols - 1 - i:
                    count += mat[i][j]
        return count'''

        for i in range(rows):
            count += mat[i][i]
            if i != rows-1-i:
                count += mat[i][rows-1-i]
        return count
        