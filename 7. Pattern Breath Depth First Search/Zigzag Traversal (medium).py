'''
Problem Statement 
Given a binary tree, populate an array to represent its zigzag level order traversal. 
You should populate the values of all nodes of the first level from left to right, 
then right to left for the next level and keep alternating in the same manner for the following levels.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == None:
            return []
        
        result = []
        level = []
        
        import collections
        queue = collections.deque()
        queue.append(root)
        queue.append('R')
        
        while queue:
            current = queue.popleft()
            
            if current == 'R':
                result.append(level)
                level = []
                if len(queue) != 0:
                    queue.append('L')
            elif current == 'L':
                level.reverse()
                result.append(level)
                level = []
                if len(queue) != 0:
                    queue.append('R')
            else:
                level.append(current.val)
                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)
        
        return result

'''
Time complexity 
    The time complexity of the above algorithm is O(N), where ‘N’ is the total number of nodes in the tree. 
    This is due to the fact that we traverse each node once.
Space complexity 
    The space complexity of the above algorithm will be O(N) as we need to return a list containing the level order traversal. 
    We will also need O(N) space for the queue. Since we can have a maximum of N/2 nodes at any level (this could happen only at the lowest level), 
    therefore we will need O(N) space to store them in the queue.
'''