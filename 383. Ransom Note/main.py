class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        '''
        解題思路：
        解釋是否能夠使用 magazine 的字母來組成 ransomNote(來源)
        '''
        
        count = [0] * 26 # 字母表
        for ch in magazine:
            count[ord(ch) - ord('a')] += 1
        
        for ch in ransomNote:
            if count[ord(ch) - ord('a')] == 0:
                return False
            count[ord(ch) - ord('a')] -= 1  
        
        return True
        
if __name__ == "__main__":
    
    s = Solution()
    question_list = [
        {"input": ["aa", "a"], "output": False},
        {"input": ["aa", "aab"], "output": True},
        {"input": ["a", "b"], "output": False},
    ]
    
    for question in question_list:
        input_data = question["input"]
        expected_output = question["output"]
        
        result = s.canConstruct(*input_data)
        print(f"[{result == expected_output}] input: {input_data}, output: {result}, expected_output: {expected_output}")
        