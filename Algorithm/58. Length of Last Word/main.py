class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # 回字串中最後一個單詞的長度
        
        split_s = s.split()
        return len(split_s[-1]) if split_s else 0
        
        
        

if __name__ in "__main__":
    
    s = Solution()
    question_list = [
        {"input": "Hello World", "output": 5},
        {"input": " ", "output": 0},
        {"input": "a ", "output": 1},
        {"input": "   fly me   to   the moon  ", "output": 4},
        {"input": "luffy is still joyboy", "output": 6},
        {"input": "Today is a nice day", "output": 3},
    ]
    
    for question in question_list:
        print(s.lengthOfLastWord(question["input"]) == question["output"])