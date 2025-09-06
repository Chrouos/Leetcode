class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        if not s: return True
        if not t: return False

        s_len = len(s)
        index = 0
        for current_t in t:
            if index < s_len and current_t == s[index]: index += 1

        return index == s_len
        
if __name__ == "__main__":
    
    s = Solution()
    question_list = [
        {"input": ["abc", "ahbgdc"], "output": True},
        {"input": ["axc", "ahbgdc"], "output": False},
        {"input": ["", ""], "output": True},
        {"input": ["abc", ""], "output": False},
        {"input": ["", "abc"], "output": True},
    ]
    
    for question in question_list:
        input_data = question["input"]
        expected_output = question["output"]
        
        # Call the function with the input data
        result = s.isSubsequence(*input_data)
        print(f"[{result == expected_output}] input: {input_data}, output: {result}, expected_output: {expected_output}")