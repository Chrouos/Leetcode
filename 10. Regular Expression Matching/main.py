class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        
        m, n = len(s), len(p)
        
        # n 內圈是 len(p), m 外圈是 len(s)
        # dp[i][j] 代表 s[:i] 與 p[:j] 是否匹配
        dp = [[False] * (n + 1) for _ in range(m + 1)] 
        
        # dp[0][0] 代表 s[:0] 與 p[:0] 是否匹配, 也就是空字串與空模式匹配
        dp[0][0] = True
        
        # 處理模式 p 前導的 `*`
        for j in range(2, n + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 2]  # `*` 可以讓前一個字母出現 0 次
        
        # 填充 DP 表
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if p[j - 1] in {s[i - 1], '.'}:  # 直接匹配字母或 `.`
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[j - 1] == '*':  # `*` 處理
                    dp[i][j] = dp[i][j - 2] or (dp[i - 1][j] and p[j - 2] in {s[i - 1], '.'})

        return dp[m][n]
        
        
if __name__ == '__main__':
    s = Solution()
    question_list = [
        {"input": ["aa", "a"], "output": False},
        {"input": ["aa", "a*"], "output": True},
        {"input": ["ab", ".*"], "output": True},
        {"input": ["mississippi", "mis*is*p*."], "output": False},
        {"input": ["aaa", "a*a"], "output": True},  # * 可以匹配多個 a
        {"input": ["aaa", "ab*a*c*a"], "output": True},  # 測試組合模式
        {"input": ["abcd", "d*"], "output": False},  # d* 不能匹配 "abcd"
        {"input": ["", ".*"], "output": True},  # .* 可以匹配空字串
        {"input": ["", ""], "output": True},  # 兩個空字串相匹配
        {"input": ["a", "ab*"], "output": True},  # b* 可以匹配 0 次
        {"input": ["a", ".*..a*"], "output": False},  # 無法匹配
        {"input": ["mississippi", "mis*is*ip*."], "output": True},  # 更完整的匹配測試
    ]

    for question in question_list:
        result = s.isMatch(*question["input"])
        print(f"[ANS] question: {question['input']} => {result} (Expected: {question['output']}) => {'✅' if result == question['output'] else '❌'}")
