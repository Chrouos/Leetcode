class Solution:
    def shortestPalindrome(self, s: str) -> str:
      # 1. 判斷是否回文
      def is_palindrome(s):
          return s == s[::-1]
      
      # 2. 找出最長的前綴
      n = len(s)
      i = 0 
      for j in range(n, 0, -1): 
        if is_palindrome(s[:j]):
          i = j
          break
        
      return s[i:][::-1] + s

if __name__ == '__main__':
    question_list = [
        {'s': 'aacecaaa', 'answer': 'aaacecaaa'},
        {'s': 'abcd', 'answer': 'dcbabcd'}
    ]
    
    s = Solution()
    for question in question_list:
        print(s.shortestPalindrome(question['s']) == question['answer'])