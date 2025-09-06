from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        n = len(matrix) # Accroding to the problem, matrix is always a square matrix
        
        # Step 1: Transpose the matrix
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # Step 2: Reverse each row
        for i in range(n):
            matrix[i] = matrix[i][::-1]

        return matrix
    
if __name__ == "__main__":
    
    s = Solution()
    question_list = [
        {"input": [[[1, 2, 3], [4, 5, 6], [7, 8, 9]]], "output": [[7, 4, 1], [8, 5, 2], [9, 6, 3]]},
        {"input": [[[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]], "output": [[15, 13, 2, 5], [14, 3, 4, 1], [12, 6, 8, 9], [16, 7, 10, 11]]}
    ]
    
    for question in question_list:
        input_matrix = question["input"][0]
        expected_output = question["output"]
        
        # Call the function with the input data
        s.rotate(input_matrix)
        print(f"[{input_matrix == expected_output}] Input: {input_matrix}, Output: {input_matrix}, Expected: {expected_output}")