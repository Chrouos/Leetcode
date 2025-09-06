class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        
        '''
        解題思路：
        判斷字串 s 是否符合模式 pattern。
        '''
        
        s = s.split()
        if len(pattern) != len(s): return False
        
        s2t = {}
        t2s = {}
        
        for i in range(len(pattern)):
            p_char = pattern[i]
            s_char = s[i]
            
            if p_char not in s2t and s_char not in t2s:
                s2t[p_char] = s_char
                t2s[s_char] = p_char
            elif s2t.get(p_char) != s_char or t2s.get(s_char) != p_char:
                return False
    
        return True


if __name__ == "__main__":
    
    s = Solution()
    question_list = [
        {"input": ["abba", "dog cat cat dog"], "output": True}, 
        {"input": ["abba", "dog cat cat fish"], "output": False},
    ]

    for question in question_list:
        input_data = question["input"]
        expected_output = question["output"]

        result = s.wordPattern(*input_data)
        print(f"[{result == expected_output}] input: {input_data}, output: {result}, expected_output: {expected_output}")