'''
Problem Statement
Find the minimum depth of a binary tree. The minimum depth is the number of nodes along 
the shortest path from the root node to the nearest leaf node.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        
        import collections
        queue = collections.deque()
        queue.append((root, 1))
        
        while queue:
            currNode, currDepth = queue.popleft()
            
            # check if currNode is a leaf
            if currNode.left == None and currNode.right == None:
                return currDepth
            
            if currNode.left:
                queue.append((currNode.left, currDepth+1))
            if currNode.right:
                queue.append((currNode.right, currDepth+1))
'''
Time complexity #
    The time complexity of the above algorithm is O(N)O(N), where ‘N’ is the total number of nodes in the tree. 
    This is due to the fact that we traverse each node once.

Space complexity #
    The space complexity of the above algorithm will be O(N) which is required for the queue. 
    Since we can have a maximum of N/2N/2 nodes at any level (this could happen only at the lowest level),
    therefore we will need O(N) space to store them in the queue.
'''