# 1605. Find Valid Matrix Given Row and Column Sums

You are given two arrays `rowSum` and `colSum` of non-negative integers
where `rowSum[i]` is the sum of the elements in the `i`<sup>`th`</sup>
row and `colSum[j]` is the sum of the elements of the `j`<sup>`th`</sup>
column of a 2D matrix. In other words, you do not know the elements of
the matrix, but you do know the sums of each row and column.

Find any matrix of **non-negative** integers of size
`rowSum.length x colSum.length` that satisfies the `rowSum` and `colSum`
requirements.

Return *a 2D array representing **any** matrix that fulfills the
requirements*. It's guaranteed that **at least one** matrix that
fulfills the requirements exists.

**Example 1:**

    Input: rowSum = [3,8], colSum = [4,7]
    Output: [[3,0],
             [1,7]]
    Explanation: 
    0th row: 3 + 0 = 3 == rowSum[0]
    1st row: 1 + 7 = 8 == rowSum[1]
    0th column: 3 + 1 = 4 == colSum[0]
    1st column: 0 + 7 = 7 == colSum[1]
    The row and column sums match, and all matrix elements are non-negative.
    Another possible matrix is: [[1,2],
                                 [3,5]]

**Example 2:**

    Input: rowSum = [5,7,10], colSum = [8,6,8]
    Output: [[0,5,0],
             [6,1,0],
             [2,0,8]]

**Constraints:**

- `1 <= rowSum.length, colSum.length <= 500`
- `0 <= rowSum[i], colSum[i] <= 10`<sup>`8`</sup>
- `sum(rowSum) == sum(colSum)`

## Greedy -  O(m * n), O(m*n)

# Intuition
To solve the problem of finding a matrix where the sums of the rows and columns match given row and column sums, we can apply the greedy algorithm. The matrix is filled cell by cell with the minimum value between the current sums so that the constraints are maintained.

# Approach
1. **Initialize the matrix**: Create a `matrix` of zeros with dimensions based on the lengths of the given row and column `sums`.
2. **Iterate through the matrix**: Loop through the rows and columns using two pointers `row_index` and `col_index`:
    - Set the cell value to the minimum of the current `rowSum` and `colSum`.
    - Subtract this value from the corresponding `rowSum` and `colSum`.
    - If the `rowSum` becomes zero, move to the next row. Otherwise, move to the next column.
3. **Return the matrix**: Return the `matrix` after filling all required cells.

# Complexity
- **Time complexity:** The time complexity of this solution is $O(m * n)$, where $m$ is the number of rows and n is the number of columns in the matrix. This is because we iterate through all cells of the matrix once to assign values based on the minimum of the current row and column sums.
- **Space complexity:** The space complexity is $O( m * n)$ as well, as we create a matrix of size $m * n$ to store the values.

# Code
```python
class Solution:
    def restoreMatrix(self, rowSum: list[int], colSum: list[int]) -> list[list[int]]:
        # Initialize the matrix with zeros
        num_rows = len(rowSum)
        num_cols = len(colSum)
        matrix = [[0] * num_cols for _ in range(num_rows)]

        # Loop through all cells of the matrix
        row_index, col_index = 0, 0
        while row_index < num_rows and col_index < num_cols:
            # Set the current cell to the minimum of the current sums
            matrix[row_index][col_index] = min(rowSum[row_index], colSum[col_index])

            # Subtract the assigned value from both rowSum and colSum
            rowSum[row_index] -= matrix[row_index][col_index]
            colSum[col_index] -= matrix[row_index][col_index]

            # Move to the next row if the current row sum is zero
            # Move to the next column otherwise
            if rowSum[row_index] == 0:
                row_index += 1
            else:
                col_index += 1

        # Return the matrix
        return matrix
```
