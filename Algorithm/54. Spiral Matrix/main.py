from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        # 螺旋的移動方式：右、下、左、上
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        result = []
        if not matrix or not matrix[0]:
            return result
        
        rows, cols = len(matrix), len(matrix[0])
        visited = [[False] * cols for _ in range(rows)] # 訪問過的位置稱為 True
        
        x, y = 0, 0  # 起始位置
        direction_index = 0  # 初始方向為右
        for _ in range(rows * cols):
            
            result.append(matrix[x][y])
            visited[x][y] = True
            
            # 計算下一個位置
            next_x = x + directions[direction_index][0]
            next_y = y + directions[direction_index][1]
            
            # 如果下一個位置超出邊界或已經訪問過，則改變方向
            if (0 <= next_x < rows and 0 <= next_y < cols and not visited[next_x][next_y]):
                x, y = next_x, next_y
            else:
                direction_index = (direction_index + 1) % 4
                
                x += directions[direction_index][0]
                y += directions[direction_index][1]

        return result


if __name__ == "__main__":
    sol = Solution()
    question_list = [
        {"input": [[1, 2, 3], [4, 5, 6], [7, 8, 9]], "output": [1, 2, 3, 6, 9, 8, 7, 4, 5]},
        {"input": [[1, 2], [3, 4]], "output": [1, 2, 4, 3]},
        {"input": [[1]], "output": [1]},
        {"input": [], "output": []},
    ]
    
    for question in question_list:
        input_matrix = question["input"]
        expected_output = question["output"]
        result = sol.spiralOrder(input_matrix)
        
        print(f"[{result == expected_output}] Input: {input_matrix}, Output: {result}, Expected: {expected_output}")