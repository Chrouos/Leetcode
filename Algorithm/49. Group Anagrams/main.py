from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        '''
        給予一個字串列表 strs，將其中的字串按照字母異位詞分組。
        '''

        anagrams = defaultdict(list)
        for s in strs:
            cnt = [0] * 26
            for ch in s:
                cnt[ord(ch) - ord('a')] += 1
            anagrams[tuple(cnt)].append(s)

        return [sorted(v) for v in anagrams.values()]


if __name__ == "__main__":
    s = Solution()
    question_list = [
        {"input": [["eat", "tea", "tan", "ate", "nat", "bat"]], "output": [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]},
    ]
    
    for question in question_list:
        input_data = question["input"]
        expected_output = question["output"]
        
        result = s.groupAnagrams(*input_data)
        print(f"[{result == expected_output}] input: {input_data}, output: {result}, expected_output: {expected_output}")