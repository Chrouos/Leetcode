from typing import Optional, List

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
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def isBST(node, low, high):
            if not node: 
                return True
            if not (low < node.val < high): 
                return False
            return isBST(node.left, low, node.val) and isBST(node.right, node.val, high)

        return isBST(root, float('-inf'), float('inf'))

if __name__ == "__main__":
    
    s = Solution()
    question_list = [
        {"input": [2, 1, 3], "output": True},
        {"input": [5, 1, 4, None, None, 3, 6], "output": False},
        {"input": [5,4,6,None,None,3,7], "output": False}
    ]

    for question in question_list:
        p = TreeNode().list_to_tree(question['input'])
        output = s.isValidBST(p)

        print(f"[{output == question['output']}] input: {question['input']}, output: {output}, expected: {question['output']}")