'''
Problem Statement 
Given a binary tree and a number ‘S’, 
find all paths from root-to-leaf such that the sum of all the node values of each path equals ‘S’.
'''

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if root == None:
            return []
            
        result = []
        path = []
        def dfs(node, currSum, path):
            if node.left == None and node.right == None and currSum+node.val == targetSum:
                result.append(path+[node.val])
                return
            else:
                # recursive case
                path = path + [node.val]
                if node.left:
                    dfs(node.left, currSum+node.val, path)
                if node.right:
                    dfs(node.right, currSum+node.val, path)
                
        dfs(root, 0, [])
        return result

# Time: O(n^2) because we visit every node once and at each node we copy the path array
# Space: O(h) where h=height of the tree because when backtracking the nodes are popped off the call stack, therefore, stack will have the height of the tree