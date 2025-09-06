from typing import Optional

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
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self.prev = None
        self.min_diff = float('inf')
        
        def inorder(node):
            if not node:
                return
            
            # Traverse left subtree
            inorder(node.left)
            
            # Process current node
            if self.prev is not None:
                self.min_diff = min(self.min_diff, node.val - self.prev)
            self.prev = node.val
            
            # Traverse right subtree
            inorder(node.right)
        
        inorder(root)
        return self.min_diff
        

if __name__ == "__main__":
    s = Solution()
    question_list = [
        {"input": [4,2,6,1,3], "output": 1},
        {"input": [1,0,48,None,None,12,49], "output": 1},
    ]
    
    for question in question_list:
        root = TreeNode().list_to_tree(question['input'])
        
        output = s.getMinimumDifference(root)
        print(f"[{output == question['output']}] input: {question['input']}, output: {output}, expected: {question['output']}")