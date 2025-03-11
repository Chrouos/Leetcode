class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        
        last_seen = {'a': -1, 'b': -1, 'c': -1}  # 記錄 a, b, c 最近出現的位置
        total = 0
        
        for right in range(len(s)):
            last_seen[s[right]] = right  

            if -1 not in last_seen.values():
                total += min(last_seen.values()) + 1  # 由 min(last_seen.values()) 計算可行起點數量

        return total
        
    # def numberOfSubstrings(self, s: str) -> int:
        
    #     count = {'a': 0, 'b': 0, 'c': 0}
    #     left_pointer = 0
    #     result = 0
    #     n = len(s)
        
    #     for right in range(n):
    #         count[s[right]] += 1
            
    #         while count['a'] > 0 and count['b'] > 0 and count['c'] > 0:
    #             result += n - right
    #             count[s[left_pointer]] -= 1
    #             left_pointer += 1
    #             print(f"{result} += {n} - {right}")
                
    #     return result
        


if __name__ == "__main__":
    s = Solution()
    question_list = [
        # {"input": "abcabc", "output": 10},
        {"input": "aaacb", "output": 3}
    ]
    
    for question in question_list:
        output_data = s.numberOfSubstrings(question["input"])
        print(f"[{question['output'] == output_data}], input: {question['input']}, output: {output_data}")
        