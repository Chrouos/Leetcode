from typing import List


class Solution:
    def findLUSlength(self, strs: List[str]) -> int:

        def isSubsequence(s1, s2):
            """
            確認 s1 是否為 s2 的 subsequence
            """
            s1_index = 0
            for s2_character in s2:
                if s1_index < len(s1) and s1[s1_index] == s2_character:
                    s1_index += 1
            return s1_index == len(s1)
        
        # 依照長度排序，長度長的在前面
        strs.sort(key=lambda x: -len(x))
        for index, s in enumerate(strs):
            if all(not isSubsequence(s, strs[j]) for j in range(len(strs)) if j != index):
                return len(s)
        
        return -1


if __name__ == '__main__':  
    
    s = Solution()
    question_list = [
        {"input": ["aba", "cdc", "eae"], "output": 3},
        {"input": ["aaa","aaa","a"], "output": -1},
        {"input": ["aaa","aaa","aa"], "output": -1},
        {"input": ["abcde", "defgk", "hijkl"], "output": 5},
    ]
    
    for question in question_list:
        print(s.findLUSlength(question["input"]), question["output"])

