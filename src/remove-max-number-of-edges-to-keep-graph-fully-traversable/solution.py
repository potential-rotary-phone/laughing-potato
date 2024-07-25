class Solution:
    def restoreMatrix(self, rowSum: list[int], colSum: list[int]) -> list[list[int]]:
        num_rows = len(rowSum)
        num_cols = len(colSum)
        matrix = [[0] * num_cols for _ in range(num_rows)]

        row_index, col_index = 0, 0
        while row_index < num_rows and col_index < num_cols:
            matrix[row_index][col_index] = min(rowSum[row_index], colSum[col_index])

            rowSum[row_index] -= matrix[row_index][col_index]
            colSum[col_index] -= matrix[row_index][col_index]

            if rowSum[row_index] == 0:
                row_index += 1
            else:
                col_index += 1

        return matrix


solution = Solution()
print(solution.restoreMatrix([3, 8], [4, 7]))
print(solution.restoreMatrix([5, 7, 10], [8, 6, 8]))
