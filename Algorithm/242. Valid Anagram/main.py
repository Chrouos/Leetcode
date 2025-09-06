class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        '''
        給予兩個字串 s 和 t，判斷它們是否為字母異位詞。
        字母異位詞的定義是：如果 s 中的每個字母都可以重新排列成 t 中的字母，
        那麼這兩個字串就是字母異位詞。
        '''
        
        if len(s) != len(t):
            return False
        
        
        '''
        使用計數器來記錄每個字母的出現次數。
        如果兩個字串的計數器相同，則它們是字母異位詞。
        '''
        count = [0] * 26
        for ch in s:
            count[ord(ch) - ord('a')] += 1
        for ch in t:
            count[ord(ch) - ord('a')] -= 1
            
        return all(c == 0 for c in count)

if __name__ == "__main__":
    s = Solution()
    question_list = [
        {"input": ["anagram", "nagaram"], "output": True},
        {"input": ["rat", "car"], "output": False},
        {"input": ["a", "a"], "output": True},
    ]
    
    for question in question_list:
        input_data = question["input"]
        expected_output = question["output"]

        result = s.isAnagram(*input_data)
        print(f"[{result == expected_output}] input: {input_data}, output: {result}, expected_output: {expected_output}")