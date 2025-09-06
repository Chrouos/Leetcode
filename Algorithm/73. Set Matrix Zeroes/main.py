from typing import List
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        
        This function sets the entire row and column to zero if an element is zero.
        """
        
        if not matrix or not matrix[0]: return 
        
        rows, cols = len(matrix), len(matrix[0])
        
        # Step 0: 檢查第一列、第一行是否原本就有 0（因為等下會把它們當標記用）
        first_row_zero = any(matrix[0][j] == 0 for j in range(cols))
        first_col_zero = any(matrix[i][0] == 0 for i in range(rows))

        # Step 1: 使用第一列和第一行作為標記
        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        
        # Step 2: 根據標記將對應的行和列設為 0
        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
                    
        # Step 3: 處理第一列和第一行
        if first_row_zero:
            for j in range(cols):
                matrix[0][j] = 0
        if first_col_zero:
            for i in range(rows):
                matrix[i][0] = 0

        return matrix

if __name__ == "__main__":
    
    s = Solution()
    question_list = [
        {"input": [[1, 1, 1], [1, 0, 1], [1, 1, 1]], "output": [[1, 0, 1], [0, 0, 0], [1, 0, 1]]},
    ]
    
    for question in question_list:
        input_matrix = question["input"]
        expected_output = question["output"]
        
        # Call the function with the input data
        s.setZeroes(input_matrix)
        print(f"[{input_matrix == expected_output}] Input: {input_matrix}, Output: {input_matrix}, Expected: {expected_output}")