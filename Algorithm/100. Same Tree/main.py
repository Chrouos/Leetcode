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
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        if not p and not q: return True
        if not p or not q: return False
        
        return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
    
if __name__ == "__main__":
    s = Solution()
    question_list = [
        {"input": [[1,2,3], [1,2,3]], "output": True},
        {"input": [[1,2], [1,None,2]], "output": False},
        {"input": [[1,2,1], [1,1,2]], "output": False},
    ]
    
    for question in question_list:
        p = TreeNode().list_to_tree(question['input'][0])
        q = TreeNode().list_to_tree(question['input'][1])
        
        output = s.isSameTree(p, q)
        print(f"[{output == question['output']}] input: {question['input']}, output: {output}, expected: {question['output']}")