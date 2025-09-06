

class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        words = sentence.split(" ")
        if words[0][0] != words[-1][-1]:
            return False
        
        for i in range(len(words) - 1):
            if words[i][-1] != words[i+1][0]:
                return False
        return True
        
if __name__ == "__main__":
    s = Solution()
    question_list = [
        {"input": "leetcode exercises sound delightful", "output": True},
        {"input": "eetcode", "output": True},
        {"input": "Leetcode is cool", "output": False},
        {"input": "leetcode", "output": True},
    ]

    for question in question_list:
        output = s.isCircularSentence(question['input'])
        print(f"[{question['output'] == output}] input: {question['input']}, output: {output}, expected: {question['output']}")
