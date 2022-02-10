'''
Problem Statement 
Given a binary tree, populate an array to represent the averages of all of its levels.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        result = []
        level = []
        
        import collections
        queue = collections.deque()
        queue.append(root)
        queue.append(None)
        
        while queue:
            current = queue.popleft()
            
            if current:
                level.append(current.val)
                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)
            else:
                result.append(sum(level)/len(level))
                level = []
                if len(queue) != 0:
                    queue.append(None)
                    
        return result

'''
Time complexity 
    The time complexity of the above algorithm is O(N), where ‘N’ is the total number of nodes in the tree. 
    This is due to the fact that we traverse each node once.
Space complexity 
    The space complexity of the above algorithm will be O(N)O which is required for the queue. 
    Since we can have a maximum of N/2 nodes at any level (this could happen only at the lowest level), 
    therefore we will need O(N) space to store them in the queue.
'''