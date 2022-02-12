'''
Problem Statement 
Given a binary tree where each node can only have a digit (0-9) value, 
each root-to-leaf path will represent a number. Find the total sum of all the numbers represented by all paths.
'''

class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0

        paths = []
        def dfs(node, digits):
            if node.left == None and node.right == None:
                digits += [node.val]
                paths.append(int(("").join(map(str,digits))))
                return
            else:
                if node.left:
                    dfs(node.left, digits+[node.val])
                if node.right:
                    dfs(node.right, digits+[node.val])
        dfs(root, [])
        return sum(paths)

# Time: O(n^2) because we visit every node once and at each node we copy the path array, however, if it was a perfectly balanced tree then it would be n*logn
# Space: O(h) where h=height of the tree because when backtracking the nodes are popped off the call stack, therefore, stack will have the height of the tree