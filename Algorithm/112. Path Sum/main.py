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
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        def dfs(node, target):
            if not node: return False
            
            if not node.left and not node.right: return target == node.val
            return dfs(node.left, target - node.val) or dfs(node.right, target - node.val)

        return dfs(root, targetSum)

if __name__ == "__main__":
    s = Solution()
    question_list = [
        {"input": [[5,4,8,11,None,13,4,7,2,None,None,None,1], 22], "output": True},
        {"input": [[1,2,3], 5], "output": False},
    ]

    for question in question_list:
        p = TreeNode().list_to_tree(question['input'][0])
        output = s.hasPathSum(p, question['input'][1])
        
        print(f"[{question['output'] == output}] input: {question['input']}, output: {output}, expected: {question['output']}")