class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        '''
        sliding window
        '''

        chart_set = set()
        left = 0
        max_length = 0
        
        for right in range(len(s)):
            while s[right] in chart_set:
                chart_set.remove(s[left])
                left += 1
            
            chart_set.add(s[right])
            max_length = max(max_length, right - left + 1)

        return max_length


if __name__ == "__main__":
    s = Solution()
    question_list = [
        {"input": ["abcabcbb"], "output": 3},
        {"input": ["bbbbb"], "output": 1},
        {"input": ["pwwkew"], "output": 3},
        {"input": ["a"], "output": 1},
        {"input": ["dvdf"], "output": 3},
    ]
    
    for question in question_list:
        input_data = question["input"]
        expected_output = question["output"]
        result = s.lengthOfLongestSubstring(*input_data)

        print(f"[{result == expected_output}] input: {input_data}, output: {result}, expected_output: {expected_output}")