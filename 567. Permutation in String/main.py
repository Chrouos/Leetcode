from collections import Counter


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        # Sliding Window
        n, m = len(s1), len(s2)
        if n > m: return False
        
        s1_counter = Counter(s1)
        s2_counter = Counter(s2[:n])
        if s1_counter == s2_counter: return True
        for i in range(n, m):
            s2_counter[s2[i]] += 1
            s2_counter[s2[i - n]] -= 1
            print(f"s2[i]: {s2[i]}, s2[i - n]: {s2[i - n]}")
            print(s2_counter)
            if s1_counter == s2_counter: return True
            
        '''
        順序可以不同
        '''
        
        return False
        
if __name__ == "__main__":
    s = Solution()
    question_list = [
        {"input": ["ab", "cobaoo"], "output": True},
        {"input": ["ab", "eidbaooo"], "output": True},
        {"input": ["ab", "eidboaoo"], "output": False},
        {"input": ["adc", "dcda"], "output": True},
    ]
    
    for question in question_list:
        output = s.checkInclusion(*question["input"])
        print(f"[{question['output'] == output}] input: {question['input']}, output: {output}, expect: {question['output']}")