from typing import List

class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        
        left = []
        right = []
        middle = []
        for num in nums:
            if num < pivot:
                left.append(num)
            elif num > pivot:
                right.append(num)
            else:
                middle.append(num)
                
        return left + middle + right
        
if __name__ == "__main__":
    s = Solution()
    question_list = [
        {"input": [[9,12,5,10,14,3,10], 10], "output": [9,5,3,10,10,12,14]},
        {"input": [[1,2,3,4,5], 3], "output": [1,2,3,4,5]},
    ]
    
    for question in question_list:
        output = s.pivotArray(question["input"][0], question["input"][1])
        print(f"[{output == question['output']}], input: {question['input']}, output: {output}, expected: {question['output']}")