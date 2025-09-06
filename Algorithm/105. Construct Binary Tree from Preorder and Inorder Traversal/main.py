from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
    def list_to_tree(self, lst):
        # （小修）空列表直接回傳 None
        if not lst:
            return None
        
        root = TreeNode(lst[0])
        queue = [root]
        index = 1
        while queue:
            node = queue.pop(0)
            if node is None:
                continue
            if index >= len(lst):
                break
            
            node.left = TreeNode(lst[index]) if lst[index] is not None else None
            queue.append(node.left)
            index += 1
            
            if index >= len(lst):
                break
            node.right = TreeNode(lst[index]) if lst[index] is not None else None
            queue.append(node.right)
            index += 1
                
        return root
    
    def tree_print_list(self, root):
        if not root:
            return []
        
        queue = [root]
        result = []
        while queue:
            node = queue.pop(0)
            if node is None:
                result.append(None)
                continue
            
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        
        # 去除末尾的 None
        while result and result[-1] is None:
            result.pop()
        
        return result
    

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        '''
        preorder: 前序遍歷（根→左→右）
        inorder:  中序遍歷（左→根→右）
        '''
        if not preorder or not inorder:
            return None
        
        # 中序索引表：值 -> 索引（假設節點值唯一）
        idx_map = {val: i for i, val in enumerate(inorder)}
        n = len(preorder)
        pre_idx = 0 
        
        def helper(left: int, right: int) -> Optional[TreeNode]:
            nonlocal pre_idx
            if left > right:
                return None
            
            # 前序的當前元素是根
            root_val = preorder[pre_idx]
            root = TreeNode(root_val)
            pre_idx += 1
            
            # 在中序中定位根，分治左右子樹
            idx = idx_map[root_val]
            root.left = helper(left, idx - 1)
            root.right = helper(idx + 1, right)
            return root
        
        # （關鍵修正）要回傳整棵樹
        return helper(0, n - 1)


if __name__ == "__main__":
    s = Solution()
    question_list = [
        {"input": [[3, 9, 20, 15, 7], [9, 3, 15, 20, 7]], "output": [3, 9, 20, None, None, 15, 7]},
        {"input": [[-1], [-1]], "output": [-1]},
    ]
    
    for q in question_list:
        preorder, inorder = q["input"]
        root = s.buildTree(preorder, inorder)
        output = TreeNode().tree_print_list(root)
        print(f"[{output == q['output']}] input: {q['input']}, output: {output}, expected: {q['output']}")
