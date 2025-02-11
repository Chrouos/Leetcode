class Solution:
    def lengthOfLastWord(self, s: str) -> int:

        split_s = s.split()
        max_len = 0
        for word in split_s:
            max_len = max(max_len, len(word))
            
        return max_len

if __name__ in "__main__":
    
    s = Solution()
    question_list = [
        {"input": "Hello World", "output": 5},
        {"input": " ", "output": 0},
        {"input": "a ", "output": 1},
        {"input": "   fly me   to   the moon  ", "output": 4},
    ]
    
    for question in question_list:
        print(s.lengthOfLastWord(question["input"]) == question["output"])