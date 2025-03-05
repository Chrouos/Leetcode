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
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root: return True
        
        def isMirror(left, right):
            if not left and not right: return True
            if not left or not right: return False
            
            return (left.val == right.val) and isMirror(left.left, right.right) and isMirror(left.right, right.left)
        
        return isMirror(root.left, root.right)
        
        
    
if __name__ == "__main__":
    s = Solution()
    question_list = [
        {"input": [[1,2,2,3,4,4,3]], "output": True},
        {"input": [[1,2,2,None,3,None,3]], "output": False},
    ]
    
    for question in question_list:
        p = TreeNode().list_to_tree(question['input'][0])
        output = s.isSymmetric(p)
        
        print(f"[{output == question['output']}] input: {question['input']}, output: {output}, expected: {question['output']}")