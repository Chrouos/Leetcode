class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
      
      for i in range(len(haystack) - len(needle) + 1):
          if haystack[i:i+len(needle)] == needle:
              return i
      return -1
        
        
        
if __name__ == '__main__':
    question_list = [
        {'haystack': 'hello', 'needle': 'll', 'answer': 2},
        {'haystack': 'aaaaa', 'needle': 'bba', 'answer': -1},
        {'haystack': '', 'needle': '', 'answer': 0}
    ]
    
    s = Solution()
    for question in question_list:
        print(s.strStr(question['haystack'], question['needle']) == question['answer'])