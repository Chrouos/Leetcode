from typing import List

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        
        '''
        給定一個氣球的區間列表 points，找出最少需要多少支箭才能射爆所有氣球。
        每支箭可以射穿所有與其重疊的氣球。
        
        例如，對於 points = [[10,16],[2,8],[1,6],[7,12]]，返回 2。
        '''
        
        if not points: return 0
        
        # 將氣球按照結束位置排序
        points.sort(key=lambda x: x[1])
        
        arrows = 1 # 至少需要一支箭
        end = points[0][1] # 第一箭會是第一顆氣球的 end
        
        for start, finish in points[1:]:
            # 如果當前氣球的開始位置大於上一支箭的結束位置，則需要新的一支箭
            if start > end:
                arrows += 1
                end = finish

        return arrows
    
if __name__ == "__main__":
    
    s = Solution()
    question_list = [
        {"input": [[[10,16],[2,8],[1,6],[7,12]]], "output": 2},
        # {"input": [[[1,2],[3,4],[5,6],[7,8]]], "output": 4},   
        # {"input": [[[1,2],[2,3],[3,4],[4,5]]], "output": 2},
    ]
    
    for question in question_list:
        input_data = question["input"]
        expected_output = question["output"]
        
        result = s.findMinArrowShots(*input_data)
        print(f"[{result == expected_output}] input: {input_data}, output: {result}, expected_output: {expected_output}")