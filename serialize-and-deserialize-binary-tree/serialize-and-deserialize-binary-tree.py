# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque
class Codec:

    def serialize(self, root):
        ans = []
        if not root:
            return ''
        temp = deque()
        temp.append(root)
        while temp:
            for _ in range(len(temp)):
                node = temp.popleft()
                if node:
                    ans.append(str(node.val))
                else:
                    ans.append('None')
                if node:
                    temp.append(node.left)
                    temp.append(node.right)
        
        while ans[-1] == 'None':
            ans.pop()
        return ','.join(ans)
        

    def deserialize(self, data):
        '''
        0,1,2,3,4,5,6
        1,2,3,4,5,6,7
        
        '''
        if not data:
            return []
        data = data.split(',')
        if data:
            val = data[0]
            val = None if val=='None' else int(val)
            root = TreeNode(val)

        def helper(root,i):
            left = i*2 +1
            right = i*2 +2
            if left<len(data):
                val = data[left]
                val = 'null' if val=='None' else int(val)
                node = TreeNode(val)
                root.left = node
                helper(node, left)
            if right<len(data):
                val = data[right]
                val = 'null' if val=='None' else int(val)
                node = TreeNode(val)
                root.right = node
                helper(node, right)
        
        helper(root,0)
        return root
                
        
        
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))