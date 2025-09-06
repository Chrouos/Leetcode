from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        '''
        給定一個區間列表 intervals 和一個新的區間 newInterval，將 newInterval 插入到 intervals 中並合併所有重疊的區間。
        
        1. 左側安全區：完全在 newInterval 左邊、且不重疊的區間 → 直接加入結果。
        2. 重疊合併區：與 newInterval 相交或相接（閉區間） → 不斷更新 newInterval = [minL, maxR]。
        3. 右側安全區：完全在（合併後的）newInterval 右邊 → 直接加入結果。
        '''
        
        if not intervals: return [newInterval]
        
        merged = []
        i = 0
        n = len(intervals)
        
        # 將所有在 newInterval 之前的區間添加到結果中
        while i < n and intervals[i][1] < newInterval[0]:
            merged.append(intervals[i])
            i += 1
            
        # 合併所有與 newInterval 重疊的區間
        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1

        merged.append(newInterval)

        # 將所有在 newInterval 之後的區間添加到結果中
        while i < n:
            merged.append(intervals[i])
            i += 1

        return merged

if __name__ == "__main__":
    
    s = Solution()
    question_list = [
        {"input": [[[1,3],[6,9]], [2,5]], "output": [[1,5],[6,9]]},
        {"input": [[[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8]], "output": [[1,2],[3,10],[12,16]]},
    ]
    
    for question in question_list:
        input_data = question["input"]
        expected_output = question["output"]
        
        result = s.insert(*input_data)
        print(f"[{result == expected_output}] input: {input_data}, output: {result}, expected_output: {expected_output}")