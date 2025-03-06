from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
    def list_to_tree(self, lst):
        if not list: None
        
        root = TreeNode(lst[0])
        queue = [root]
        index = 1
        while queue:
            node = queue.pop(0)
            if node is None: continue
            if index >= len(lst): break
            
            node.left = TreeNode(lst[index]) if lst[index] is not None else None
            queue.append(node.left)
            index += 1
            
            if index >= len(lst): break
            node.right = TreeNode(lst[index]) if lst[index] is not None else None
            queue.append(node.right)
            index += 1
                
        return root
    
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        size = 0
        if not root: return size
        
        def dfs(node, depth):
            nonlocal size
            if not node: return
            
            size = max(size, depth)
            
            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)
        
        dfs(root, 1)
        return size
        
if __name__ == "__main__":
    s = Solution()
    question_list = [
        {"input": [[3,9,20,None,None,15,7]], "output": 3},
        {"input": [[1,None,2]], "output": 2},
    ]
    
    for question in question_list:
        p = TreeNode().list_to_tree(question['input'][0])
        
        output = s.maxDepth(p)
        print(f"[{output == question['output']}] input: {question['input']}, output: {output}, expected: {question['output']}")
        