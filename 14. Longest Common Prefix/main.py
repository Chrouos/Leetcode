class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        
        if not strs: return ''
        
        result_prefix = ''
        for i in range(len(strs[0])):
            for j in range(1, len(strs)):
                if i >= len(strs[j]) or strs[j][i] != strs[0][i]:
                    return result_prefix
            result_prefix += strs[0][i]
        
        return result_prefix
    
    
if __name__ == '__main__':
    strs = ["flower","flow","flight"]
    s = Solution()
    print(s.longestCommonPrefix(strs)) # 'fl'
    