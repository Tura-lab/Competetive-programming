class TrieNode:
    def __init__(self, val=None):
        self.val = val 
        self.children = [None]*26
        self.isEnd = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for i in range(len(word)):
            c = word[i]
            if node.children[ord(c)-ord('a')] == None:
                n = TrieNode(val=c)
                node.children[ord(c)-ord('a')] = n
            node = node.children[ord(c)-ord('a')]
        node.isEnd=True

    def search(self, word: str) -> bool:
        node = self.root
        for i in range(len(word)):
            c = word[i]
            if not node.children[ord(c) - ord('a')] or node.children[ord(c) - ord('a')].val != c:
                return False
            node = node.children[ord(c) - ord('a')]
        
        return node.isEnd

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for i in range(len(prefix)):
            c = prefix[i]
            if not node.children[ord(c) - ord('a')] or node.children[ord(c) - ord('a')].val != c:
                return False
            node = node.children[ord(c) - ord('a')]
        
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)