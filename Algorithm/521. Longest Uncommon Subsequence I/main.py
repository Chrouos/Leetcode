class Solution:
    def findLUSlength(self, a: str, b: str) -> int:
        
        if a == b:
            return -1
        else:
            return max(len(a), len(b))
        
    
if __name__ == '__main__':
    
    s = Solution()
    question_list = [
        {"input": ("aba", "cdc"), "output": 3},
        {"input": ("aaa","aaa"), "output": -1},
        {"input": ("aaa","aaa"), "output": -1},
        {"input": ("abcde", "defgk"), "output": 5},
    ]
    
    for question in question_list:
        print(s.findLUSlength(*question['input']) == question['output'])