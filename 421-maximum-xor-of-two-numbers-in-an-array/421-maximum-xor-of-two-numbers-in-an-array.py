class TrieNode:
    def __init__(self, val=None):
        self.children = [None, None]
        self.val = None

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, num: str) -> None:
        node = self.root
        mask = 1 << 30
        for i in range(30, -1, -1):
            bit = (mask) & num != 0
            if not node.children[bit]:
                node.children[bit] = TrieNode()
            node = node.children[bit]
            mask >>= 1
        node.val = num
                
    def search(self, num: str) -> bool:
        node = self.root
        mask = 1 << 30
        for i in range(30, -1, -1):
            bit = (mask) & num == 0
            if node.children[bit]:
                node = node.children[bit]
            else:
                node = node.children[1-bit]
            mask >>= 1
        return node.val

class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        trie = Trie()
        
        for num in nums:
            trie.insert(num)
        ans = float('-inf')
        
        for num in nums:
            ans = max(ans, trie.search(num)^num)
        
        return ans
