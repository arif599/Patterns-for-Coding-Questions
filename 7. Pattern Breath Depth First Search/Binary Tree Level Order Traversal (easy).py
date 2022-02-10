"""
Problem Statement 
Given a binary tree, populate an array to represent its level-by-level traversal. 
You should populate the values of all nodes of each level from left to right in separate sub-arrays.
"""

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


def traverse(root):
    result = []
    level = []

    # level order traversal (BFS)
    import collections
    queue = collections.deque()
    queue.append(root)
    queue.append(None) # used to indicate the end of a level

    while queue:
        current = queue.popleft()

        if current:
            level.append(current.val)
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
        else:
            result.append(level) # add the level to the result
            level = []
            if len(queue) != 0: # only add None if the queue is not empty
                 queue.append(None)
    
    return result
    


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Level order traversal: " + str(traverse(root)))


main()
'''
Time complexity 
    The time complexity of the above algorithm is O(N), where ‘N’ is the total number of nodes in the tree. 
    This is due to the fact that we traverse each node once.
Space complexity 
    The space complexity of the above algorithm will be O(N) as we need to return a list containing the level order traversal. 
    We will also need O(N) space for the queue. Since we can have a maximum of N/2 nodes at any level (this could happen only at the lowest level), 
    therefore we will need O(N) space to store them in the queue.
'''