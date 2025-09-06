from typing import List
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        '''
        給定一個區間列表的 intervals，合併所有重疊的區間
        
        例如，對於 intervals = [[1,3],[2,6],[8,10],[15,18]]，返回 [[1,6],[8,10],[15,18]]。        
        '''
        
        if not intervals: return []

        # 將第一個數字進行排序
        intervals.sort(key=lambda x: x[0])
        merged = [intervals[0]]
        
        # 從第二個區間開始遍歷
        for current in intervals[1:]:
            last_merged = merged[-1]

            # 如果當前區間的開始小於等於最後合併區間的結束，則合併它們
            if current[0] <= last_merged[1]: 
                last_merged[1] = max(last_merged[1], current[1])
            else: 
                merged.append(current)

        return merged

if __name__ == "__main__":
    
    s = Solution()
    question_list = [
        {"input": [[1,3],[2,6],[8,10],[15,18]], "output": [[1,6],[8,10],[15,18]]},
        # {"input": [[1,4],[4,5]], "output": [[1,5]]},
        # {"input": [[1,4],[0,4]], "output": [[0,4]]},
        # {"input": [[1,2],[3,4],[5,6],[7,8]], "output": [[1,2],[3,4],[5,6],[7,8]]},
        # {"input": [[1,4],[2,3]], "output": [[1,4]]},
        
    ]
    
    for question in question_list:
        input_data = question["input"]
        expected_output = question["output"]
        
        result = s.merge(input_data)
        print(f"[{result == expected_output}] input: {input_data}, output: {result}, expected_output: {expected_output}")
    
    