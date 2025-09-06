class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        '''
        給予 s, t 兩個字串，判斷它們是否為同構字串。
        同構字串的定義是：如果 s 中的每個字母都可以被唯一地映射到 t 中的字母，且反之亦然，
        那麼這兩個字串就是同構的。
        '''
        
        if len(s) != len(t): return False
        
        s2t = [-1] * 256
        t2s = [-1] * 256
        for i in range(len(s)):
            s_char = ord(s[i])
            t_char = ord(t[i])
            
            if s2t[s_char] == -1 and t2s[t_char] == -1:
                s2t[s_char] = t_char
                t2s[t_char] = s_char
            elif s2t[s_char] != t_char or t2s[t_char] != s_char:
                return False

        return True

if __name__ == "__main__":
    
    s = Solution()
    question_list = [
        {"input": ["egg", "add"], "output": True},
        {"input": ["foo", "bar"], "output": False},
        {"input": ["paper", "title"], "output": True},
        {"input": ["ab", "aa"], "output": False},
        {"input": ["a", "b"], "output": True},
        {"input": ["a", "a"], "output": True},
        {"input": ["abc", "def"], "output": True},
        {"input": ["ab", "cd"], "output": True},
    ]
    
    for question in question_list:
        input_data = question["input"]
        expected_output = question["output"]
        
        result = s.isIsomorphic(*input_data)
        print(f"[{result == expected_output}] input: {input_data}, output: {result}, expected_output: {expected_output}")
        
    
    
