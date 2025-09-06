class Solution:
    def simplifyPath(self, path: str) -> str:
        
        '''
        給定一個 Unix 路徑，簡化它並返回最簡化的路徑。
        '''
        
        stack = []
        parts = path.split('/')
        
        for part in parts:
            if part == '' or part == '.': continue # 忽略空部分和當前目錄
            if part == '..':
                if stack: stack.pop() # 回到上一級目錄
            else:
                stack.append(part)
                
        return '/' + '/'.join(stack)
        

if __name__ == "__main__":
        s = Solution()
        question_list = [
            {"input": ["/a/./b/../../c/"], "output": "/c"},
            {"input": ["/../"], "output": "/"},
            {"input": ["/home//foo/"], "output": "/home/foo"},
            {"input": ["/a/../../b/../c//.//"], "output": "/c"},
            {"input": ["/a//b////c/d//././/.."], "output": "/a/b/c"}
        ]
        
        for question in question_list:
            input_data = question["input"]
            expected_output = question["output"]
            
            result = s.simplifyPath(*input_data)
            print(f"[{result == expected_output}] input: {input_data}, output: {result}, expected_output: {expected_output}")