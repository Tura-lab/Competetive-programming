# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
        levels = defaultdict(int)
        max_height = defaultdict(int)
        max_without = defaultdict(list)
        heights = defaultdict(list)
        answers = defaultdict(int)
        
        def dfs(node, count):
            if not node:
                return count - 1
            heights[count].append(node.val)
            levels[node.val] = count
            left = dfs(node.left, count + 1)
            right = dfs(node.right, count + 1)
            max_height[node.val] = max(left, right)
            
            return max_height[node.val]
        
        dfs(root, 0)
        for level in levels.keys():
            cur = -float('inf')
            for i in range(len(heights[level])):
                max_without[level].append(cur)
                cur = max(cur, max_height[heights[level][i]])
                
        for level in levels.keys():
            cur = -float('inf')
            for i in range(len(heights[level])-1 ,-1, -1):
                max_without[level][i] = max(max_without[level][i], cur)
                answers[heights[level][i]] = max_without[level][i]
                cur = max(cur, max_height[heights[level][i]])

        ans = []
        for q in queries:
            level = levels[q]
            if len(heights[level]) == 1:
                ans.append(level - 1)
            else:
                ans.append(answers[q])
        return ans